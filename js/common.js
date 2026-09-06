(function(){
'use strict';

const path = window.location.pathname;
const isApipages = path.includes('/apipages/');
const isPages = !isApipages && path.includes('/pages/');
const prefix = isApipages ? '../../' : isPages ? '../' : '';

const pageName = (function(){
  let f = path.substring(path.lastIndexOf('/') + 1);
  if (!f || f === 'index.html') return '';
  f = f.replace('.html','');
  try { f = decodeURIComponent(f); } catch (e) {}
  return f;
})();

// ── Navbar ──
document.getElementById('navbar-container').innerHTML =
`<nav class="navbar" id="navbar" role="navigation" aria-label="主导航">
  <div class="nav-inner">
    <a class="logo" data-href="${prefix}index.html">
      <span class="logo-icon">
        <svg width="40" height="40" viewBox="0 0 1024 1024" aria-hidden="true">
          <path d="M474.282667 96.213333a123.477333 123.477333 0 0 0-116.181334 123.221334l-0.042666 22.826666H243.797333A104.832 104.832 0 0 0 139.093333 347.477333l-0.213333 138.922667a32 32 0 0 0 32 32.042667h54.698667c36.821333 0 66.730667 29.909333 66.730666 66.730666 0 36.821333-29.909333 66.773333-66.730666 66.773334H170.837333a32 32 0 0 0-32 31.957333l-0.170666 138.965333a105.130667 105.130667 0 0 0 105.130666 105.173334h138.965334a32 32 0 0 0 32-32v-54.869334a66.816 66.816 0 0 1 133.504 0V896c0 17.664 14.336 32 32 32h138.965333l6.912-0.213333a105.130667 105.130667 0 0 0 98.218667-104.96v-114.261334h22.869333a123.477333 123.477333 0 0 0 123.434667-123.434666l-0.213334-7.253334a123.477333 123.477333 0 0 0-123.221333-116.181333h-22.869333V347.434667l-0.213334-6.912a105.130667 105.130667 0 0 0-104.917333-98.218667l-114.304-0.042667v-22.826666a123.477333 123.477333 0 0 0-123.392-123.434667z" fill="none" stroke="#4ade80" stroke-width="50" stroke-linejoin="round"/>
          <text x="570" y="650" text-anchor="middle" font-size="220" font-weight="800" fill="#4ade80" font-family="Orbitron,'Segoe UI Black','Arial Black',sans-serif">UCF</text>
        </svg>
      </span>
      <span class="logo-text">UCFPlugin</span>
    </a>
    <ul class="nav-links" id="navLinks" role="menubar">
        <li role="none"><a class="nav-item" data-page="配置插件" data-href="${prefix}pages/配置插件.html">配置插件</a></li>
        <li role="none"><a class="nav-item" data-page="接口文档" data-href="${prefix}pages/接口文档.html">接口文档</a></li>
        <li role="none"><a class="nav-item" data-page="智能体" data-href="${prefix}pages/智能体.html">智能体</a></li>
        <li role="none"><a class="nav-item" data-page="技术思考" data-href="${prefix}pages/技术思考.html">技术思考</a></li>
        <li role="none"><a class="nav-item" data-page="授权申请" data-href="${prefix}pages/授权申请.html">授权申请</a></li>
      </ul>
    <button class="mobile-toggle" id="mobileToggle" aria-label="切换菜单" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
  </div>
</nav>`;

// ── Footer ──
const footerEl = document.getElementById('footer-container');
if (footerEl) {
  footerEl.innerHTML =
`<footer class="footer">
    <div class="footer-bottom">
      <div class="footer-left">
        <div class="footer-copyright">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="12" cy="12" r="10"/>
            <path d="M14.5 9a3.5 3.5 0 1 0 0 5.5"/>
          </svg>
          <span><span class="footer-copyright-at">@</span> 2026 UCFPlugin</span>
        </div>
        <div class="footer-contact">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="2" y="4" width="20" height="16" rx="2"/>
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
          </svg>
          <a href="mailto:ucfplugin@163.com">ucfplugin@163.com</a>
        </div>
      </div>
      <div class="footer-visitor">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
          <circle cx="9" cy="7" r="4"/>
          <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
          <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
        </svg>
        <span>访客 <span id="busuanzi_value_site_uv">0</span></span>
      </div>
    </div>
    <div class="footer-note">
      <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <circle cx="12" cy="12" r="10"/>
        <line x1="12" y1="16" x2="12" y2="12"/>
        <line x1="12" y1="8" x2="12.01" y2="8"/>
      </svg>
      <span>UCFPlugin 为个人持续开发，不保证更新频率与稳定性</span>
    </div>
  </footer>`;
}

// ── Active nav ──
if (pageName) {
  document.querySelectorAll('.nav-item[data-page]').forEach(function(el){
    if (el.getAttribute('data-page') === pageName) {
      el.classList.add('active');
      var dd = el.closest('.nav-dropdown');
      if (dd) dd.classList.add('is-active');
    }
  });
}

// ── Mobile menu ──
(function(){
  const toggle = document.getElementById('mobileToggle');
  const navLinks = document.getElementById('navLinks');
  if (toggle && navLinks) {
    toggle.addEventListener('click', function(){
      const open = navLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    navLinks.addEventListener('click', function(e){
      if (window.innerWidth <= 900 && e.target.closest('.nav-item')) {
        navLinks.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
})();

// ── data-href handler ──
document.addEventListener('click', function(e){
  if (e.defaultPrevented) return;
  const a = e.target.closest('a[data-href]');
  if (a) {
    e.preventDefault();
    const h = a.getAttribute('data-href');
    if (h.charAt(0) === '#') {
      const t = document.querySelector(h);
      if (t) t.scrollIntoView({ behavior:'smooth' });
    } else {
      window.location.href = h;
    }
  }
});

// ── Navbar scroll effect (IO-based, no scroll listener) ──
(function(){
  const nav = document.getElementById('navbar');
  if (!nav || !('IntersectionObserver' in window)) return;
  // Sentinel dedup: don't append another one if common.js runs twice on the same page
  let sentinel = document.getElementById('__nav-sentinel');
  if (!sentinel) {
    sentinel = document.createElement('div');
    sentinel.id = '__nav-sentinel';
    sentinel.style.cssText = 'position:absolute;top:32px;left:0;width:1px;height:1px;pointer-events:none;';
    document.body.appendChild(sentinel);
  }
  new IntersectionObserver(function(entries){
    nav.classList.toggle('scrolled', !entries[0].isIntersecting);
  }, { threshold: 0 }).observe(sentinel);
})();

})();