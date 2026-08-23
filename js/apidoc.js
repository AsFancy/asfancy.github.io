// ── Shared renderer for API doc pages (apipages/*.html) ──
// Each apipage must set window.GRP (group list) and window.API (ep map) before this script's
// DOMContentLoaded handler fires. The inline <script> in each page runs synchronously before
// DOMContentLoaded, so the order is: apidoc.js (sync) -> data inline script (sync) -> DOMContentLoaded
// -> renderAll().

(function(){
'use strict';

const ICON_DEMO = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>';
const SCROLL_OFFSET = 88; // --nav-h (64) + 24

function renderAll() {
  const GRP = window.GRP;
  const API = window.API;
  if (!GRP || !API) return;

  let sn = '';
  GRP.forEach(function(g){
    if (g.label) sn += '<div class="snav-group">' + g.label + '</div>';
    g.apis.forEach(function(n){
      sn += '<a class="snav-item" data-href="#' + n + '" onclick="return navClick(\'' + n + '\')"><span class="sname">' + n + '</span></a>';
    });
  });
  document.getElementById('snav').innerHTML = sn;

  let html = '';
  GRP.forEach(function(g){
    g.apis.forEach(function(n){ html += epCard(n, API[n]); });
  });
  document.getElementById('groupsContainer').innerHTML = html;

  const hlBlocks = document.querySelectorAll('pre code');
  const hlRun = function(){ hlBlocks.forEach(function(b){ hljs.highlightElement(b); }); };
  if ('requestIdleCallback' in window) requestIdleCallback(hlRun, {timeout: 500});
  else setTimeout(hlRun, 0);
}

function epCard(name, d) {
  let h = '<div class="ep-card" data-api="' + name + '" id="' + name + '">';
  const typeBadge = {sync:'<span class="ep-type sync">Sync</span>',async:'<span class="ep-type async">Async</span>',trigger:'<span class="ep-type trigger">Trigger</span>'}[d.t] || '';
  h += '<div class="ep-header" onclick="toggleEP(this)"><span class="ep-name">' + typeBadge + d.title + '</span><svg class="ep-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></div>';
  h += '<div class="ep-body"><div class="ep-inner">';

  // Empty braces/arrays gain a single space so they read as wrapping content.
  const fmtPn = function(s){ return s.split('{}').join('{ }').split('[]').join('[ ]'); };

  if (d.notes) {
    h += '<div class="callout tips"><div><div class="c-title">Tips</div><ul>' + d.notes.map(function(n){ return '<li>' + n + '</li>'; }).join('') + '</ul></div></div>';
  }
  if (d.scenario) {
    h += '<div class="callout info"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg><div><div class="c-title">使用场景</div><ul>' + d.scenario.map(function(s){ return '<li>' + s + '</li>'; }).join('') + '</ul></div></div>';
  }
  if (!d.noReq && d.pf) {
    h += '<div class="ep-section">调用参数说明</div>';
    if (d.pf.length) {
      h += '<div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>说明</th></tr></thead><tbody>';
      d.pf.forEach(function(p){ h += '<tr><td class="pn">' + fmtPn(p[0]) + '</td><td class="pt">' + p[1] + '</td><td class="pr">必填</td><td class="pd">' + p[2] + '</td></tr>'; });
      h += '</tbody></table></div>';
    }
    if (d.pi && d.pi.length) {
      h += '<div class="ep-subsection">Params内参数</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>说明</th></tr></thead><tbody>';
      d.pi.forEach(function(p){ h += '<tr><td class="pn">' + fmtPn(p[0]) + '</td><td class="pt">' + p[1] + '</td><td class="pr ' + (p[2]==='必填'?'y':'n') + '">' + p[2] + '</td><td class="pd">' + p[3] + '</td></tr>'; });
      h += '</tbody></table></div>';
    }
    if (d.kpi) {
      h += '<div class="ep-subsection">Keyframes数组元素</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>说明</th></tr></thead><tbody>';
      d.kpi.forEach(function(p){ h += '<tr><td class="pn">' + fmtPn(p[0]) + '</td><td class="pt">' + p[1] + '</td><td class="pr ' + (p[2]==='必填'?'y':'n') + '">' + p[2] + '</td><td class="pd">' + p[3] + '</td></tr>'; });
      h += '</tbody></table></div>';
    }
  }
  if (d.re) {
    d.re.forEach(function(ex){ h += '<div class="ep-section">' + ex.lb + '</div>' + codeBlock(ex.cd); });
  } else if (!d.noReq && d.req) {
    h += '<div class="ep-section">调用参数示例</div>' + codeBlock(d.req);
    if (d.reqNote) h += '<div class="api-note">' + d.reqNote + '</div>';
  }
  h += '<div class="ep-section">回调参数说明</div>';
  const cbf = d.cf || [['ExecutionID','String','执行ID'],['Interface','String','接口名称'],['Status','Boolean','操作是否成功'],['DebugInfo','String','调试信息'],['Params','Object','参数对象']];
  h += '<div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>说明</th></tr></thead><tbody>';
  cbf.forEach(function(p){ h += '<tr><td class="pn">' + fmtPn(p[0]) + '</td><td class="pt">' + p[1] + '</td><td class="pr">-</td><td class="pd">' + p[2] + '</td></tr>'; });
  h += '</tbody></table></div>';
  if (d.cbi) {
    h += '<div class="ep-subsection">Params内参数</div><div class="p-wrap"><table class="p-table"><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>说明</th></tr></thead><tbody>';
    d.cbi.forEach(function(p){ h += '<tr><td class="pn">' + fmtPn(p[0]) + '</td><td class="pt">' + p[1] + '</td><td class="pr ' + (p[2]==='必填'?'y':'n') + '">' + p[2] + '</td><td class="pd">' + p[3] + '</td></tr>'; });
    h += '</tbody></table></div>';
  }
  if (d.ce) {
    d.ce.forEach(function(ex){ h += '<div class="ep-section">' + ex.lb + '</div>' + codeBlock(ex.cd); });
  } else if (d.cb) {
    h += '<div class="ep-section">回调参数示例</div>' + codeBlock(d.cb);
  }
  if (d.bvid) {
    h += '<div class="api-demo"><div class="api-demo-h">' + ICON_DEMO + ' 功能演示</div><div class="api-demo-bilibili"><iframe loading="lazy" src="https://player.bilibili.com/player.html?bvid=' + d.bvid + '&page=1&high_quality=1&autoplay=0" allowfullscreen></iframe></div></div>';
  }
  h += '</div></div></div>';
  return h;
}

function codeBlock(code) {
  let fmt = code;
  try { fmt = JSON.stringify(JSON.parse(code), null, 4); } catch(e) {}
  const esc = fmt.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  return '<div class="cb"><div class="cb-h"><button class="cpy" onclick="cpy(this)" data-cd="' + encodeURIComponent(code) + '"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg><span class="cpy-text">复制</span></button></div><pre><code class="language-json">' + esc + '</code></pre></div>';
}

function toggleEP(h) {
  const card = h.closest('.ep-card');
  card.classList.toggle('open');
  syncNav(card.dataset.api);
}

function navClick(name) {
  const card = document.getElementById(name);
  if (card) {
    card.classList.add('open');
    window.scrollTo(window.scrollX, window.scrollY + card.getBoundingClientRect().top - SCROLL_OFFSET);
  }
  syncNav(name);
  return false;
}

function syncNav(name) {
  const target = document.querySelector('.snav-item[data-href="#' + name + '"]');
  if (!target) return;
  document.querySelectorAll('.snav-item.active').forEach(function(n){ n.classList.remove('active'); });
  target.classList.add('active');
  const navContainer = document.getElementById('snav');
  const tRect = target.getBoundingClientRect();
  const cRect = navContainer.getBoundingClientRect();
  if (tRect.top < cRect.top || tRect.bottom > cRect.bottom) {
    navContainer.scrollTop = target.offsetTop - cRect.height / 3;
  }
}

let _copyResetTimer = null;
function cpy(btn) {
  const code = decodeURIComponent(btn.dataset.cd);
  const textEl = btn.querySelector('.cpy-text');
  if (!textEl) return;
  navigator.clipboard.writeText(code).then(function(){
    btn.classList.add('done');
    textEl.textContent = '已复制';
    if (_copyResetTimer) clearTimeout(_copyResetTimer);
    _copyResetTimer = setTimeout(function(){
      btn.classList.remove('done');
      textEl.textContent = '复制';
    }, 2000);
  });
}

let _filterTimer = null;
function doFilter(q) {
  if (_filterTimer) clearTimeout(_filterTimer);
  _filterTimer = setTimeout(function(){ _doFilter(q); }, 80);
}

function _doFilter(q) {
  const s = q.toLowerCase().trim();
  document.querySelectorAll('.ep-card').forEach(function(c){
    c.style.display = (!s || c.dataset.api.toLowerCase().includes(s) || c.textContent.toLowerCase().includes(s)) ? '' : 'none';
  });
  document.querySelectorAll('.snav-item').forEach(function(n){
    n.style.display = (!s || n.textContent.toLowerCase().includes(s)) ? '' : 'none';
  });
}

// Expose for inline event handlers (onclick="toggleEP(this)" etc.)
window.toggleEP = toggleEP;
window.navClick = navClick;
window.cpy = cpy;
window.doFilter = doFilter;

document.addEventListener('DOMContentLoaded', function(){
  if (typeof window.GRP !== 'undefined' && typeof window.API !== 'undefined') {
    renderAll();
  }
});

})();