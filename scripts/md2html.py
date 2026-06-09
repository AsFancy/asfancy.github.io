#!/usr/bin/env python3
"""
将结构化的 Markdown API 文档转换为 HTML。

解析遵循 UCFPlugin API 文档规范的 .md 文件，生成嵌入 JavaScript GRP/API对象的 .html 文件。

使用方法：
    python md2html.py input.md [output.html]
    python md2html.py input.md              # 输出到 input.html
    python md2html.py *.md                  # 批量转换

配置文件 (.env)：
    在脚本同目录下创建 .env 文件来配置默认路径。执行时不传参数时，脚本会从 .env 读取配置。

    MD_PATH    - 包含 .md 文件的文件夹路径（必填）
    HTML_PATH  - 输出 .html 文件的文件夹路径（可选，默认为 MD_PATH）

    示例 .env：
        MD_PATH=../pages/apipages
        HTML_PATH=../pages/apipages

    配置好后直接运行：python md2html.py
"""

import re
import sys
import os
import json
import glob as glob_mod
from pathlib import Path


def load_env(env_path):
    """Load variables from a .env file."""
    env_vars = {}
    if not os.path.isfile(env_path):
        return env_vars
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                env_vars[key.strip()] = val.strip()
    return env_vars


def get_default_paths():
    """Get MD_PATH and HTML_PATH from .env file if present."""
    script_dir = Path(__file__).parent
    env_path = script_dir / '.env'
    env_vars = load_env(env_path)
    md_path = env_vars.get('MD_PATH', '')
    html_path = env_vars.get('HTML_PATH', '')
    return md_path, html_path


# ── Color palette for groups (cycled) ──────────────────────────────────
GROUP_COLORS = ["#34d399", "#60a5fa", "#fbbf24", "#a78bfa", "#f472b6",
                "#fb923c", "#38bdf8", "#a3e635", "#f87171", "#c084fc"]

# Default callback fields - if cf matches this, it's omitted from output
DEFAULT_CF = [
    ["ExecutionID", "String", "执行ID"],
    ["Interface", "String", "接口名称"],
    ["Status", "Boolean", "操作是否成功"],
    ["DebugInfo", "String", "调试信息"],
    ["Params", "Object", "参数对象"],
]


# ── Markdown Parser ────────────────────────────────────────────────────

def parse_md(filepath):
    """Parse a UCFPlugin API markdown file into structured data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')

    data = {
        'title': '',
        'description': '',
        'groups': [],       # [{id, label, apis: [name, ...]}]
        'apis': {},         # {name: {t, title, notes, pf, pi, req, cb, ...}}
        'api_order': [],    # ordered list of API names
        '_api_data_list': [],  # temp: parsed API data in order
    }

    # State
    state = 'init'          # init, after_title, overview, api_detail
    current_group = None
    current_api = None      # current API name being parsed
    current_api_data = None
    in_overview_table = False
    in_params_table = False
    in_inner_params = False
    in_cb_table = False
    in_cb_inner = False
    in_tips = False
    tips_list = []
    table_rows = []
    table_ctx = None         # 'overview', 'pf', 'pi', 'cf', 'cbi'
    table_past_sep = False   # True after separator row seen
    code_block = ''
    in_code_block = False
    subsection = None        # current subsection heading
    in_callback = False      # True when parsing callback params section
    description_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block detection
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                in_code_block = False
                if subsection == 'req_example':
                    current_api_data['req'] = code_block.strip()
                elif subsection == 'cb_example':
                    current_api_data['cb'] = code_block.strip()
                code_block = ''
                subsection = None
            else:
                in_code_block = True
                code_block = ''
            i += 1
            continue

        if in_code_block:
            if code_block:
                code_block += '\n'
            code_block += line
            i += 1
            continue

        stripped = line.strip()

        # ── Title (h1) ──
        if state == 'init' and stripped.startswith('# '):
            data['title'] = stripped[2:].strip()
            state = 'after_title'
            i += 1
            continue

        # ── Description (first non-empty paragraph after title) ──
        if state == 'after_title':
            if stripped == '':
                if description_lines:
                    data['description'] = ' '.join(description_lines)
                    state = 'body'
                i += 1
                continue
            if not stripped.startswith('#'):
                description_lines.append(stripped)
                i += 1
                continue
            else:
                if description_lines:
                    data['description'] = ' '.join(description_lines)
                state = 'body'

        # ── Overview section ──
        if stripped == '## 接口一览':
            state = 'overview'
            i += 1
            continue

        if state == 'overview':
            if stripped.startswith('### '):
                # New group
                group_label = stripped[4:].strip()
                current_group = {
                    'label': group_label,
                    'apis': []
                }
                data['groups'].append(current_group)
                in_overview_table = False
                i += 1
                continue

            if stripped.startswith('|') and current_group is not None:
                if in_overview_table and not stripped.startswith('| :'):
                    # Parse overview table row
                    cells = _parse_table_row(stripped)
                    if len(cells) >= 1:
                        # Extract API name from link: [UCFView/SetDPPosition](...)
                        api_name = _extract_link_text(cells[0])
                        if api_name:
                            current_group['apis'].append(api_name)
                elif stripped.startswith('|') and ('---' in stripped or ':---' in stripped):
                    in_overview_table = True
                i += 1
                continue

            if stripped.startswith('<a id=') or stripped.startswith('## '):
                state = 'api_detail'
                # Fall through to api_detail handling
            else:
                i += 1
                continue

        # ── API detail sections ──
        if state == 'api_detail':
            # Anchor tag: <a id="..."></a>
            if stripped.startswith('<a id='):
                i += 1
                continue

            # Back link: [← 返回接口一览](#接口一览)
            if stripped.startswith('[←') or stripped == '':
                i += 1
                continue

            # API title: ## Title
            if stripped.startswith('## '):
                # Save previous API
                _finalize_api(current_api_data, data)
                current_api_data = {
                    'notes': [],
                    'pf': [],
                    'pi': [],
                }
                current_api_data['title'] = stripped[3:].strip()
                tips_list = []
                in_tips = False
                table_rows = []
                table_ctx = None
                table_past_sep = False
                subsection = None
                in_callback = False
                i += 1
                continue

            # Type: **类型:** Type
            if stripped.startswith('**类型:**'):
                typ = stripped.split('**类型:**', 1)[1].strip()
                # Normalize: Async -> async, Sync -> sync, Trigger -> trigger
                current_api_data['t'] = typ.lower()
                i += 1
                continue

            # Tips header
            if stripped == '**Tips:**':
                in_tips = True
                tips_list = []
                i += 1
                continue

            # Tips items
            if in_tips and stripped.startswith('- '):
                tips_list.append(stripped[2:].strip())
                i += 1
                continue
            elif in_tips and not stripped.startswith('- '):
                # End of tips
                current_api_data['notes'] = tips_list
                in_tips = False
                # Don't advance i, reprocess this line

            # Subsection headings
            if stripped.startswith('#### '):
                # Save any pending table
                _commit_table(table_rows, table_ctx, current_api_data)

                heading = stripped[5:].strip()
                table_rows = []
                table_ctx = None
                table_past_sep = False

                if heading == '调用参数说明':
                    subsection = 'req_params'
                    table_ctx = 'pf'
                    in_callback = False
                elif heading == 'Params内参数':
                    subsection = 'inner_params'
                    table_ctx = 'cbi' if in_callback else 'pi'
                elif heading == '调用参数示例':
                    subsection = 'req_example'
                elif heading == '回调参数说明':
                    subsection = 'cb_params'
                    table_ctx = 'cf'
                    in_callback = True
                elif heading == '回调参数示例':
                    subsection = 'cb_example'
                elif heading == '功能演示':
                    subsection = 'demo'
                else:
                    subsection = heading
                i += 1
                continue

            # Table rows
            if stripped.startswith('|') and table_ctx:
                if stripped.startswith('| :') or '---' in stripped:
                    # Separator row
                    table_past_sep = True
                    i += 1
                    continue
                if table_past_sep:
                    cells = _parse_table_row(stripped)
                    table_rows.append(cells)
                # else: header row, skip
                i += 1
                continue
            elif stripped.startswith('|') and not table_ctx:
                # Stray table, skip
                i += 1
                continue

            # End of table (blank line or next section)
            if stripped == '' and table_rows:
                # Check if next line starts a subsection
                pass  # Will be committed at next #### or end

            # Bilibili badge: [![B站视频](...)](url)
            bvid_match = re.search(r'bilibili\.com/video/(BV\w+)', stripped)
            if bvid_match:
                current_api_data['bvid'] = bvid_match.group(1)

            i += 1
            continue

        i += 1

    # Finalize last API
    _commit_table(table_rows, table_ctx, current_api_data)
    _finalize_api(current_api_data, data)

    # Build api_order from groups
    for g in data['groups']:
        for api_name in g['apis']:
            data['api_order'].append(api_name)

    # Match API data by order
    ordered_names = data['api_order']
    ordered_data = data['_api_data_list']

    for idx, name in enumerate(ordered_names):
        if idx < len(ordered_data):
            data['apis'][name] = ordered_data[idx]

    # Clean up temporary key
    del data['_api_data_list']

    return data


def _parse_table_row(line):
    """Parse a markdown table row into a list of cell contents."""
    # Remove leading/trailing pipes and split
    row = line.strip().strip('|')
    cells = [c.strip() for c in row.split('|')]
    return cells


def _convert_inline_code(text):
    """Convert markdown backtick `code` to HTML <code> tags."""
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', text)


def _extract_link_text(cell):
    """Extract text from a markdown link like [text](url). Returns text or original."""
    match = re.match(r'\[([^\]]+)\]\([^)]+\)', cell)
    if match:
        return match.group(1)
    return cell


def _commit_table(table_rows, table_ctx, api_data):
    """Save accumulated table rows to the appropriate field."""
    if not table_rows or not table_ctx or not api_data:
        return
    if table_ctx == 'pf':
        # Convert to 3-field format for pf: [name, type, desc]
        formatted = []
        for row in table_rows:
            if len(row) >= 4:
                formatted.append([row[0], row[1], _convert_inline_code(row[3])])
            elif len(row) >= 3:
                formatted.append([row[0], row[1], _convert_inline_code(row[2])])
        api_data['pf'] = formatted
    elif table_ctx == 'pi':
        api_data['pi'] = [[r[0], r[1], r[2], _convert_inline_code(r[3])] for r in table_rows if len(r) >= 4]
    elif table_ctx == 'cf':
        # Custom callback fields (different from default)
        formatted = []
        for row in table_rows:
            if len(row) >= 4:
                formatted.append([row[0], row[1], _convert_inline_code(row[3])])
            elif len(row) >= 3:
                formatted.append([row[0], row[1], _convert_inline_code(row[2])])
        api_data['cf'] = formatted
    elif table_ctx == 'cbi':
        api_data['cbi'] = [[r[0], r[1], r[2], _convert_inline_code(r[3])] for r in table_rows if len(r) >= 4]


def _finalize_api(api_data, data):
    """Finalize current API data after parsing and append to data list."""
    if not api_data or 'title' not in api_data:
        return
    # Remove empty fields
    for key in ['pf', 'pi', 'cf', 'cbi']:
        if key in api_data and not api_data[key]:
            del api_data[key]
    if 'notes' in api_data and not api_data['notes']:
        del api_data['notes']
    # Omit cf if it matches the default
    if api_data.get('cf') == DEFAULT_CF:
        del api_data['cf']
    # Trigger type has no request
    if api_data.get('t') == 'trigger':
        api_data['noReq'] = True
    data['_api_data_list'].append(api_data)


# ── HTML Generator ─────────────────────────────────────────────────────

def _escape_js_string(s):
    """Escape a string for safe embedding in JavaScript single/double quotes."""
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    return s


def _format_js_array(arr, indent=0):
    """Format a Python list as a JavaScript array string."""
    prefix = ' ' * indent

    def fmt_val(v):
        if isinstance(v, bool):
            return 'true' if v else 'false'
        elif isinstance(v, int) or isinstance(v, float):
            return str(v)
        elif v is None:
            return 'null'
        else:
            return "'" + _escape_js_string(str(v)) + "'"

    if not arr:
        return '[]'

    # If it's an array of arrays (like pf, pi), format each row on its own line
    if arr and isinstance(arr[0], list):
        lines = []
        for row in arr:
            cells = ', '.join(fmt_val(c) for c in row)
            lines.append(f'{prefix}  [{cells}]')
        return '[\n' + ',\n'.join(lines) + '\n' + prefix + ']'
    else:
        cells = ', '.join(fmt_val(c) for c in arr)
        return '[' + cells + ']'


def generate_html(data, output_path):
    """Generate the HTML file from parsed data."""

    # Build GRP JavaScript
    grp_entries = []
    for idx, g in enumerate(data['groups']):
        color = GROUP_COLORS[idx % len(GROUP_COLORS)]
        # Generate a simple id from group label (use index for reliability)
        gid = f"g{idx}"
        apis = '[' + ', '.join(f'"{a}"' for a in g['apis']) + ']'
        grp_entries.append(
            f'  {{ id:"{gid}", label:"{g["label"]}", dot:"{color}",\n'
            f'    apis:{apis} }}'
        )

    grp_js = 'const GRP = [\n' + ',\n'.join(grp_entries) + '\n];'

    # Build API JavaScript
    api_entries = []
    for name in data['api_order']:
        if name not in data['apis']:
            continue
        d = data['apis'][name]

        fields = []
        if 't' in d:
            fields.append(f't:"{d["t"]}"')
        if 'title' in d:
            fields.append(f'title:"{_escape_js_string(d["title"])}"')

        # Notes
        if 'notes' in d and d['notes']:
            notes_js = '[' + ', '.join(f'"{_escape_js_string(n)}"' for n in d['notes']) + ']'
            fields.append(f'notes:{notes_js}')

        # pf, pi, cf, cbi
        for key in ['pf', 'pi', 'cf', 'cbi']:
            if key in d and d[key]:
                fields.append(f'{key}:{_format_js_array(d[key])}')

        # noReq for trigger type
        if d.get('noReq'):
            fields.append('noReq:true')

        # req
        if 'req' in d:
            fields.append(f"req:'{_escape_js_string(d['req'])}'")

        # cb
        if 'cb' in d:
            fields.append(f"cb:'{_escape_js_string(d['cb'])}'")

        # bvid
        if 'bvid' in d:
            fields.append(f'bvid:"{d["bvid"]}"')

        body = ',\n    '.join(fields)
        api_entries.append(f'  "{name}": {{\n    {body}\n  }}')

    api_js = 'const API = {\n' + ',\n'.join(api_entries) + '\n};'

    html = _build_html(data['title'], data['description'], grp_js, api_js)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def _build_html(title, description, grp_js, api_js):
    """Build the complete HTML document with the given data."""
    desc = _escape_js_string(description)
    # Escape for HTML attribute context
    title_html = title.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    desc_html = description.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_html} - UCFPlugin</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/style.css">
<link rel="icon" type="image/svg+xml" href="../../res/favicon.svg">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
<style>
/* ── API Doc Layout ── */
.api-layout{{display:flex;max-width:var(--max-w);margin:0 auto;padding:0 24px 60px;gap:28px;position:relative}}
.api-sidebar{{
  width:max-content;min-width:220px;flex-shrink:0;
  position:sticky;top:calc(var(--nav-h) + 24px);align-self:flex-start;
  display:flex;flex-direction:column;
  max-height:calc(100vh - var(--nav-h) - 48px);
  border-radius:var(--radius-md);
  background:var(--bg-card);border:1px solid var(--border-glass);
  backdrop-filter:blur(12px);
}}
.api-sidebar-search{{
  padding:10px 12px;flex-shrink:0;position:relative;
}}
.api-sidebar-search input{{
  width:100%;padding:7px 10px 7px 30px;
  background:var(--bg-glass);border:1px solid var(--border-glass);
  border-radius:var(--radius-sm);color:var(--text-main);
  font-size:14px;font-family:'Exo 2',sans-serif;
  outline:none;transition:border-color .2s,box-shadow .2s;
}}
.api-sidebar-search input:focus{{border-color:rgba(74,222,128,0.3);box-shadow:0 0 0 3px var(--green-glow)}}
.api-sidebar-search input::placeholder{{color:var(--text-dim)}}
.api-sidebar-search .s-icon{{position:absolute;left:22px;top:50%;transform:translateY(-50%);color:var(--text-dim);pointer-events:none}}
.api-sidebar-nav{{
  overflow-y:auto;flex:1;padding:6px 0 12px;
  scrollbar-gutter:stable;
}}
.api-sidebar-nav::-webkit-scrollbar{{width:3px}}
.api-sidebar-nav::-webkit-scrollbar-track{{background:transparent}}
.api-sidebar-nav::-webkit-scrollbar-thumb{{
  background:rgba(255,255,255,0.15);
  border-radius:3px;
}}
.api-sidebar-nav::-webkit-scrollbar-thumb:hover{{
  background:rgba(255,255,255,0.25);
}}
.snav-group{{
  padding:14px 16px 4px 18px;
  font-size:12px;font-weight:700;text-transform:uppercase;
  letter-spacing:.08em;color:var(--text-main);
  display:flex;align-items:center;gap:8px;
}}
.snav-group::before{{
  content:'';width:6px;height:6px;border-radius:50%;
  background:var(--green);flex-shrink:0;
}}
.snav-item{{
  display:flex;align-items:center;gap:6px;
  padding:7px 12px 7px 18px;margin:1px 6px;border-radius:5px;
  font-size:14px;font-weight:500;color:var(--text-muted);
  cursor:pointer;transition:all .15s;text-decoration:none;position:relative;
}}
.snav-item:hover{{color:var(--text-main);background:var(--green-glow)}}
.snav-item.active{{color:var(--green);background:var(--green-glow)}}
.snav-item.active::before{{
  content:'';position:absolute;left:-6px;top:50%;transform:translateY(-50%);
  width:3px;height:55%;border-radius:0 2px 2px 0;background:var(--green);
}}
.snav-item .sname{{white-space:nowrap}}
.api-content{{flex:1;min-width:0;min-height:calc(100vh - var(--nav-h) - 120px)}}
.api-content > * + *{{margin-top:32px}}
.ep-card{{
  background:var(--bg-card);border:1px solid var(--border-glass);
  border-radius:var(--radius-md);margin-bottom:8px;overflow:hidden;
  transition:border-color .2s,box-shadow .2s;
}}
.ep-card.open{{
  border-color:rgba(74,222,128,0.2);
  box-shadow:0 0 0 1px var(--green-glow),0 8px 32px rgba(0,0,0,0.25);
}}
.ep-header{{
  display:flex;align-items:center;gap:10px;
  padding:10px 16px;cursor:pointer;user-select:none;transition:background .15s;
}}
.ep-header:hover{{background:var(--bg-glass)}}
.ep-card.open .ep-header{{background:rgba(74,222,128,0.08);border-bottom:1px solid rgba(74,222,128,0.1)}}
.ep-name{{
  font-size:14px;font-weight:500;
  color:var(--text-main);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:flex;align-items:center;gap:6px;
}}
.ep-type{{
  font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;
  letter-spacing:.05em;text-transform:uppercase;flex-shrink:0;
}}
.ep-type.sync{{background:var(--green-glow);color:var(--green)}}
.ep-type.trigger{{background:rgba(251,191,36,0.15);color:#fbbf24}}
.ep-type.async{{background:rgba(96,165,250,0.15);color:#60a5fa}}
.ep-arrow{{color:var(--text-dim);flex-shrink:0;transition:transform .3s}}
.ep-card.open .ep-arrow{{transform:rotate(180deg)}}
.ep-body{{display:none}}
.ep-card.open .ep-body{{display:block}}
.ep-inner{{padding:0 20px 20px}}
.ep-inner > * + *{{margin-top:20px}}
.callout{{
  border-radius:var(--radius-sm);padding:12px 16px;
  display:flex;gap:10px;font-size:14px;line-height:1.7;
}}
.callout svg{{flex-shrink:0;margin-top:2px}}
.callout.warn{{background:rgba(251,191,36,0.06);border:1px solid rgba(251,191,36,0.15)}}
.callout.warn svg{{color:#fbbf24}}
.callout.warn .c-title{{color:#fbbf24;font-weight:600;margin-bottom:3px;font-size:12px;text-transform:uppercase;letter-spacing:.05em}}
.callout.info{{background:var(--indigo-glow);border:1px solid rgba(99,102,241,0.15)}}
.callout.info svg{{color:var(--indigo)}}
.callout.tips{{display:block;padding:0;margin-top:16px}}
.callout.tips .c-title{{color:var(--indigo);font-size:12px;font-weight:700;letter-spacing:.04em;margin-bottom:6px}}
.callout.tips ul{{list-style:none;margin:0;padding:0}}
.callout.tips ul li{{color:var(--text-main);font-size:13px;padding:2px 0 2px 12px;position:relative}}
.callout.tips ul li::before{{content:'';position:absolute;left:0;top:11px;width:4px;height:4px;border-radius:50%;background:var(--text-dim)}}
.callout.info .c-title{{color:var(--indigo);font-weight:600;margin-bottom:3px;font-size:12px;text-transform:uppercase;letter-spacing:.05em}}
.callout ul{{list-style:none}}
.callout ul li{{position:relative;padding-left:14px;color:var(--text-muted)}}
.callout ul li::before{{content:'';position:absolute;left:0;top:7px;width:4px;height:4px;border-radius:50%;background:var(--text-dim)}}
.ep-section{{
  display:flex;align-items:center;gap:12px;
  margin:24px 0 14px;font-size:12px;font-weight:700;
  text-transform:uppercase;letter-spacing:.1em;color:var(--green);
}}
.ep-section::before,.ep-section::after{{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(74,222,128,0.25));
}}
.ep-section::after{{background:linear-gradient(90deg,rgba(74,222,128,0.25),transparent)}}
.ep-section:first-child{{margin-top:0}}
.ep-subsection{{
  font-size:13px;font-weight:600;color:var(--text-main);
  display:flex;align-items:center;gap:8px;
  padding:6px 0 4px;margin-top:2px;
}}
.ep-subsection + .p-wrap{{margin-top:8px}}
.ep-subsection::before{{
  content:'';width:3px;height:14px;border-radius:2px;
  background:var(--green);flex-shrink:0;
}}
.p-wrap{{overflow-x:auto;border:1px solid var(--border-glass);border-radius:var(--radius-sm)}}
.p-table{{width:100%;border-collapse:collapse;font-size:14px;min-width:540px;table-layout:fixed}}
.p-table th:nth-child(1),.p-table td:nth-child(1){{width:25%}}
.p-table th:nth-child(2),.p-table td:nth-child(2){{width:12.5%}}
.p-table th:nth-child(3),.p-table td:nth-child(3){{width:12.5%}}
.p-table th:nth-child(4),.p-table td:nth-child(4){{width:50%}}
.p-table th{{
  text-align:left;padding:10px 14px;
  font-weight:600;color:var(--text-dim);
  font-size:11px;text-transform:uppercase;letter-spacing:.06em;
  background:var(--bg-glass);border-bottom:1px solid var(--border-glass);
}}
.p-table td{{padding:9px 14px;border-bottom:1px solid var(--border-glass);color:var(--text-muted);vertical-align:top}}
.p-table tr:last-child td{{border-bottom:none}}
.p-table .pn{{font-family:'Exo 2',monospace;font-size:13px;color:var(--text-main);white-space:nowrap}}
.p-table .pn .nested{{color:var(--text-dim)}}
.p-table .pt{{font-size:13px;color:var(--text-muted);white-space:nowrap}}
.p-table .pr{{font-size:12px;white-space:nowrap}}
.p-table .pr{{color:var(--text-main);font-weight:600}}
.p-table .pr.n{{color:var(--text-dim);font-weight:400}}
.p-table .pd{{font-size:14px;color:var(--text-muted);line-height:1.6}}
.p-table .pd code{{font-family:'Exo 2',monospace;font-size:12px;color:var(--green);padding:0 3px;border-radius:3px}}
.cb{{border:1px solid var(--border-glass);border-radius:var(--radius-sm);overflow:hidden;transition:border-color .2s}}
.cb-h{{
  display:flex;align-items:center;justify-content:flex-end;
  padding:5px 12px;background:rgba(0,0,0,0.2);
  border-bottom:1px solid var(--border-glass);
  font-size:10px;color:var(--text-dim);
}}
.cb-h .cpy{{
  display:flex;align-items:center;gap:4px;
  background:none;border:none;color:var(--text-dim);
  cursor:pointer;font-size:12px;font-family:'Exo 2',sans-serif;
  padding:3px 8px;border-radius:4px;transition:all .15s;
}}
.cb-h .cpy:hover{{background:var(--bg-glass);color:var(--text-muted)}}
.cb-h .cpy.done{{color:var(--green)}}
.cb pre{{margin:0;padding:16px;background:rgba(0,0,0,0.3);overflow-x:auto;font-size:14px;line-height:1.8}}
.cb pre code{{font-family:'Exo 2',monospace;background:none!important;padding:0!important}}
.hljs{{background:transparent!important;color:#e2e8f0!important}}
.hljs-keyword,.hljs-selector-tag,.hljs-type{{color:#a78bfa!important}}
.hljs-string,.hljs-attr{{color:#6ee7b7!important}}
.hljs-number,.hljs-literal{{color:#67e8f9!important}}
.hljs-comment,.hljs-quote{{color:#64748b!important}}
.hljs-built_in,.hljs-title{{color:#818cf8!important}}
.hljs-property{{color:#7dd3fc!important}}
.hljs-attribute{{color:#fcd34d!important}}
.hljs-punctuation{{color:#94a3b8!important}}
.api-note{{font-size:14px;color:var(--text-dim);line-height:1.7}}
.api-demo{{
  margin-top:20px;border:1px solid var(--border-glass);border-radius:var(--radius-sm);overflow:hidden;
}}
.api-demo-h{{
  display:flex;align-items:center;gap:6px;
  padding:8px 14px;background:var(--bg-glass);border-bottom:1px solid var(--border-glass);
  font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--green);
}}
.api-demo-h svg{{color:var(--green)}}
.api-demo-bilibili{{
  position:relative;width:100%;padding-bottom:49.72%;background:#0a0a0f;
}}
.api-demo-bilibili iframe{{
  position:absolute;top:0;left:0;width:100%;height:100%;border:0;
}}
@media(max-width:1024px){{
  .api-layout{{flex-direction:column;padding:0 16px 60px}}
  .api-sidebar{{width:100%;position:relative;top:auto;height:auto;max-height:none;border-radius:var(--radius-md);margin-bottom:0}}
  .api-sidebar-nav{{max-height:260px}}
}}
@media(max-width:600px){{
  .ep-header{{padding:8px 12px}}
  .ep-inner{{padding:0 12px 12px}}
  .ep-name{{font-size:13px}}
  .p-wrap{{overflow-x:auto}}
  .p-table{{min-width:480px}}
  .api-layout{{padding:0 12px 60px}}
}}
@media(prefers-reduced-motion:reduce){{
  *,*::before,*::after{{animation-duration:0.01ms!important;transition-duration:0.01ms!important}}
  html{{scroll-behavior:auto}}
}}
</style>
</head>
<body>

<div id="navbar-container"></div>

<div class="page-loaded">

<div class="page-header" style="padding:120px 24px 30px;text-align:center">
  <div class="page-header-bg">
    <div class="gradient g-left"></div>
    <div class="gradient g-right"></div>
  </div>
  <div class="header-grid"></div>
  <h1 style="font-size:34px;font-weight:700;margin-bottom:20px;letter-spacing:-0.02em">{title_html}</h1>
  <p style="font-size:16px;color:var(--text-muted);max-width:560px;margin:0 auto 40px;line-height:1.6">{desc_html}</p>
</div>

<div class="api-layout">

<aside class="api-sidebar" id="apiSidebar">
  <div class="api-sidebar-search">
    <svg class="s-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="text" id="search" placeholder="搜索接口..." oninput="doFilter(this.value)">
  </div>
  <nav class="api-sidebar-nav" id="snav"></nav>
</aside>

<main class="api-content">
<div id="groupsContainer"></div>
</main>

</div>

<footer class="footer">
  <p>&copy; <span id="year"></span> UCFPlugin. All rights reserved. 数字孪生 · UnrealEngine 插件</p>
</footer>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/json.min.js"></script>
<script src="../../js/common.js"></script>
<script>
// ===================== DATA =====================
{grp_js}

{api_js}

// ===================== RENDER =====================
const ICON_DEMO = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>';

function renderAll() {{
  let sn = "";
  GRP.forEach(g => {{
    sn += `<div class="snav-group">${{g.label}}</div>`;
    g.apis.forEach(n => {{
      sn += `<a class="snav-item" data-href="#${{n}}" onclick="return navClick('${{n}}')"><span class="sname">${{n}}</span></a>`;
    }});
  }});
  document.getElementById("snav").innerHTML = sn;

  let html = "";
  GRP.forEach(g => {{
    g.apis.forEach(n => {{ html += epCard(n, API[n]); }});
  }});
  document.getElementById("groupsContainer").innerHTML = html;
  document.querySelectorAll('pre code').forEach(b => hljs.highlightElement(b));
}}

function epCard(name, d) {{
  let h = `<div class="ep-card" data-api="${{name}}" id="${{name}}">`;
  const typeBadge = {{sync:'<span class="ep-type sync">Sync</span>',async:'<span class="ep-type async">Async</span>',trigger:'<span class="ep-type trigger">Trigger</span>'}}[d.t] || '';
  h += `<div class="ep-header" onclick="toggleEP(this)"><span class="ep-name">${{typeBadge}}${{d.title}}</span><svg class="ep-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></div>`;
  h += `<div class="ep-body"><div class="ep-inner">`;

  if (d.notes) {{
    h += `<div class="callout tips"><div><div class="c-title">Tips</div><ul>${{d.notes.map(n=>`<li>${{n}}</li>`).join("")}}</ul></div></div>`;
  }}
  if (d.scenario) {{
    h += `<div class="callout info"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg><div><div class="c-title">使用场景</div><ul>${{d.scenario.map(s=>`<li>${{s}}</li>`).join("")}}</ul></div></div>`;
  }}
  if (!d.noReq && d.pf) {{
    h += `<div class="ep-section">调用参数说明</div>`;
    if (d.pf.length) {{
      h += `<div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th style="width:56px">必填</th><th>说明</th></tr></thead><tbody>`;
      d.pf.forEach(p => h += `<tr><td class="pn">${{p[0]}}</td><td class="pt">${{p[1]}}</td><td class="pr">必填</td><td class="pd">${{p[2]}}</td></tr>`);
      h += `</tbody></table></div>`;
    }}
    if (d.pi && d.pi.length) {{
      h += `<div class="ep-subsection">Params内参数</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th style="width:56px">必填</th><th>说明</th></tr></thead><tbody>`;
      d.pi.forEach(p => h += `<tr><td class="pn">${{p[0]}}</td><td class="pt">${{p[1]}}</td><td class="pr ${{p[2]==="必填"?'y':'n'}}">${{p[2]}}</td><td class="pd">${{p[3]}}</td></tr>`);
      h += `</tbody></table></div>`;
    }}
    if (d.kpi) {{
      h += `<div class="ep-subsection">Keyframes数组元素</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th style="width:50px">必填</th><th>说明</th></tr></thead><tbody>`;
      d.kpi.forEach(p => h += `<tr><td class="pn">${{p[0]}}</td><td class="pt">${{p[1]}}</td><td class="pr ${{p[2]==="必填"?'y':'n'}}">${{p[2]}}</td><td class="pd">${{p[3]}}</td></tr>`);
      h += `</tbody></table></div>`;
    }}
  }}
  if (d.re) {{
    d.re.forEach(ex => {{ h += `<div class="ep-section">${{ex.lb}}</div>` + codeBlock(ex.cd); }});
  }} else if (!d.noReq && d.req) {{
    h += `<div class="ep-section">调用参数示例</div>` + codeBlock(d.req);
    if (d.reqNote) h += `<div class="api-note">${{d.reqNote}}</div>`;
  }}
  h += `<div class="ep-section">回调参数说明</div>`;
  const cbf = d.cf || [["ExecutionID","String","执行ID"],["Interface","String","接口名称"],["Status","Boolean","操作是否成功"],["DebugInfo","String","调试信息"],["Params","Object","参数对象"]];
  h += `<div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th style="width:56px">必填</th><th>说明</th></tr></thead><tbody>`;
  cbf.forEach(p => h += `<tr><td class="pn">${{p[0]}}</td><td class="pt">${{p[1]}}</td><td class="pr">-</td><td class="pd">${{p[2]}}</td></tr>`);
  h += `</tbody></table></div>`;
  if (d.cbi) {{
    h += `<div class="ep-subsection">Params内参数</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th style="width:56px">必填</th><th>说明</th></tr></thead><tbody>`;
    d.cbi.forEach(p => h += `<tr><td class="pn">${{p[0]}}</td><td class="pt">${{p[1]}}</td><td class="pr ${{p[2]==="必填"?'y':'n'}}">${{p[2]}}</td><td class="pd">${{p[3]}}</td></tr>`);
    h += `</tbody></table></div>`;
  }}
  if (d.ce) {{
    d.ce.forEach(ex => {{ h += `<div class="ep-section">${{ex.lb}}</div>` + codeBlock(ex.cd); }});
  }} else if (d.cb) {{
    h += `<div class="ep-section">回调参数示例</div>` + codeBlock(d.cb);
  }}
  if (d.bvid) {{
    h += `<div class="api-demo"><div class="api-demo-h">${{ICON_DEMO}} 功能演示</div><div class="api-demo-bilibili"><iframe src="https://player.bilibili.com/player.html?bvid=${{d.bvid}}&page=1&high_quality=1&autoplay=0" allowfullscreen></iframe></div></div>`;
  }}
  h += `</div></div></div>`;
  return h;
}}

function codeBlock(code) {{
  let fmt = code;
  try {{ fmt = JSON.stringify(JSON.parse(code), null, 4); }} catch(e) {{}}
  const esc = fmt.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  return `<div class="cb"><div class="cb-h"><button class="cpy" onclick="cpy(this)" data-cd="${{encodeURIComponent(code)}}"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> 复制</button></div><pre><code class="language-json">${{esc}}</code></pre></div>`;
}}

function toggleEP(h) {{
  const card = h.closest('.ep-card');
  card.classList.toggle('open');
  syncNav(card.dataset.api);
}}

function navClick(name) {{
  const card = document.getElementById(name);
  if (card) {{
    card.classList.add('open');
    const navH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-h'));
    const st = navH + 24;
    const ct = card.getBoundingClientRect().top;
    const root = document.documentElement;
    root.style.scrollBehavior = 'auto';
    window.scrollTo(window.scrollX, window.scrollY + ct - st);
    root.style.scrollBehavior = '';
  }}
  syncNav(name);
  return false;
}}

function syncNav(name) {{
  document.querySelectorAll('.snav-item').forEach(n => {{ n.classList.toggle('active', n.getAttribute('data-href') === '#' + name); }});
  const target = document.querySelector(`.snav-item[data-href="#${{name}}"]`);
  if (target) {{
    const navContainer = document.getElementById('snav');
    const targetRect = target.getBoundingClientRect();
    const containerRect = navContainer.getBoundingClientRect();
    if (targetRect.top < containerRect.top || targetRect.bottom > containerRect.bottom) {{
      navContainer.scrollTo({{ top: target.offsetTop - containerRect.height / 3, behavior: 'smooth' }});
    }}
  }}
}}

function cpy(btn) {{
  const code = decodeURIComponent(btn.dataset.cd);
  navigator.clipboard.writeText(code).then(() => {{
    btn.classList.add('done');
    btn.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg> 已复制';
    setTimeout(() => {{ btn.classList.remove('done'); btn.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> 复制'; }}, 2000);
  }});
}}

function doFilter(q) {{
  const s = q.toLowerCase().trim();
  document.querySelectorAll('.ep-card').forEach(c => {{
    c.style.display = (!s || c.dataset.api.toLowerCase().includes(s) || c.textContent.toLowerCase().includes(s)) ? '' : 'none';
  }});
  document.querySelectorAll('.snav-item').forEach(n => {{
    n.style.display = (!s || n.textContent.toLowerCase().includes(s)) ? '' : 'none';
  }});
}}

renderAll();
</script>
</body>
</html>'''


# ── Main ───────────────────────────────────────────────────────────────

def main():
    md_default, html_default = get_default_paths()

    if len(sys.argv) < 2:
        if md_default:
            md_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), md_default))
            html_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), html_default)) if html_default else md_dir
            if not os.path.isdir(md_dir):
                print(f"Error: MD_PATH directory not found: {md_dir}")
                sys.exit(1)
            inputs = glob_mod.glob(os.path.join(md_dir, '*.md'))
            if not inputs:
                print(f"Error: No .md files found in: {md_dir}")
                sys.exit(1)
        else:
            print("Usage: python md2html.py <input.md> [output.html]")
            print("       python md2html.py *.md  (batch convert)")
            print("       Or configure MD_PATH (folder containing .md files) and HTML_PATH (output folder) in .env file, then run without arguments.")
            sys.exit(1)
    else:
        # Expand glob patterns
        inputs = []
        for arg in sys.argv[1:]:
            expanded = glob_mod.glob(arg)
            if expanded:
                inputs.extend(expanded)
            else:
                inputs.append(arg)
        html_dir = None

    for input_path in inputs:
        if not input_path.endswith('.md'):
            print(f"  Skipping non-markdown file: {input_path}")
            continue
        if not os.path.isfile(input_path):
            print(f"  File not found: {input_path}")
            continue

        # Determine output path
        if html_dir:
            base = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(html_dir, base + '.html')
        else:
            base = os.path.splitext(input_path)[0]
            output_path = base + '.html'

        print(f"Converting: {input_path} -> {output_path}")
        try:
            data = parse_md(input_path)
            generate_html(data, output_path)
            print(f"  OK: {output_path}")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    main()
