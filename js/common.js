(function(){
'use strict';

const path = window.location.pathname;
const isApipages = path.includes('/apipages/');
const isPages = !isApipages && path.includes('/pages/');
const prefix = isApipages ? '../../' : isPages ? '../' : '';

const pageName = (function(){
  const f = path.substring(path.lastIndexOf('/') + 1);
  if (!f || f === 'index.html') return '';
  return f.replace('.html','');
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
    </ul>
    <button class="mobile-toggle" id="mobileToggle" aria-label="切换菜单" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
  </div>
</nav>`;

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

// ── Footer year ──
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ── Navbar scroll effect (IO-based, no scroll listener) ──
(function(){
  const nav = document.getElementById('navbar');
  if (!nav || !('IntersectionObserver' in window)) return;
  const sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:32px;left:0;width:1px;height:1px;pointer-events:none;';
  document.body.appendChild(sentinel);
  new IntersectionObserver(function(entries){
    nav.classList.toggle('scrolled', !entries[0].isIntersecting);
  }, { rootMargin: '0px 0px 0px 0px', threshold: 0 }).observe(sentinel);
})();

// ── Pause hero/page-header gradient animations when offscreen ──
(function(){
  if (!('IntersectionObserver' in window)) return;
  const targets = document.querySelectorAll('.hero, .page-header');
  if (!targets.length) return;
  const io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      entry.target.classList.toggle('paused-bg', !entry.isIntersecting);
    });
  }, { threshold: 0 });
  targets.forEach(function(el){ io.observe(el); });
})();

})();