/* UCFPlugin Shared Utilities */
(function(){
'use strict';

var path = window.location.pathname;
var isApipages = path.indexOf('/apipages/') !== -1;
var isPages = !isApipages && path.indexOf('/pages/') !== -1;
var prefix = isApipages ? '../../' : isPages ? '../' : '';

// Current page name from URL
var pageName = (function(){
  var f = path.substring(path.lastIndexOf('/') + 1);
  if (!f || f === 'index.html') return '';
  return f.replace('.html','');
})();

// ── Navbar ──
document.getElementById('navbar-container').innerHTML =
'<nav class="navbar" id="navbar" role="navigation" aria-label="主导航">'+
'  <div class="nav-inner">'+
'    <a class="logo" data-href="'+prefix+'index.html">'+
'      <span class="logo-icon">'+
'        <svg width="40" height="40" viewBox="0 0 1024 1024" aria-hidden="true">'+
'          <path d="M474.282667 96.213333a123.477333 123.477333 0 0 0-116.181334 123.221334l-0.042666 22.826666H243.797333A104.832 104.832 0 0 0 139.093333 347.477333l-0.213333 138.922667a32 32 0 0 0 32 32.042667h54.698667c36.821333 0 66.730667 29.909333 66.730666 66.730666 0 36.821333-29.909333 66.773333-66.730666 66.773334H170.837333a32 32 0 0 0-32 31.957333l-0.170666 138.965333a105.130667 105.130667 0 0 0 105.130666 105.173334h138.965334a32 32 0 0 0 32-32v-54.869334a66.816 66.816 0 0 1 133.504 0V896c0 17.664 14.336 32 32 32h138.965333l6.912-0.213333a105.130667 105.130667 0 0 0 98.218667-104.96v-114.261334h22.869333a123.477333 123.477333 0 0 0 123.434667-123.434666l-0.213334-7.253334a123.477333 123.477333 0 0 0-123.221333-116.181333h-22.869333V347.434667l-0.213334-6.912a105.130667 105.130667 0 0 0-104.917333-98.218667l-114.304-0.042667v-22.826666a123.477333 123.477333 0 0 0-123.392-123.434667z"'+
'            fill="none" stroke="#4ade80" stroke-width="50" stroke-linejoin="round"/>'+
'          <text x="570" y="650" text-anchor="middle" font-size="220" font-weight="800"'+
'            fill="#4ade80" font-family="Orbitron,\'Segoe UI Black\',\'Arial Black\',sans-serif">UCF</text>'+
'        </svg>'+
'      </span>'+
'      <span class="logo-text">UCFPlugin</span>'+
'    </a>'+
'    <ul class="nav-links" id="navLinks" role="menubar">'+
'      <li role="none"><a class="nav-item" data-page="配置插件" data-href="'+prefix+'pages/配置插件.html">配置插件</a></li>'+
'      <li class="nav-dropdown" role="none">'+
'        <a class="nav-item" data-page="接口文档" data-href="'+prefix+'pages/接口文档.html">接口文档 <span class="dropdown-arrow">▾</span></a>'+
'        <div class="nav-dropdown-menu" role="menu" aria-label="接口文档">'+
'          <a data-href="'+prefix+'pages/apipages/UCFView.html" role="menuitem">'+
'            <span class="menu-label">UCFView</span><span class="menu-desc">视点管理</span>'+
'          </a>'+
'          <a data-href="'+prefix+'pages/接口文档.html#UCFVisibility" role="menuitem">'+
'            <span class="menu-label">UCFVisibility</span><span class="menu-desc">可视性</span>'+
'          </a>'+
'          <a data-href="'+prefix+'pages/接口文档.html#UCFOutlineActor" role="menuitem">'+
'            <span class="menu-label">UCFOutlineActor</span><span class="menu-desc">对象高亮</span>'+
'          </a>'+
'          <a data-href="'+prefix+'pages/接口文档.html#UCFOutlineArea" role="menuitem">'+
'            <span class="menu-label">UCFOutlineArea</span><span class="menu-desc">区域高亮</span>'+
'          </a>'+
'        </div>'+
'      </li>'+
'      <li role="none"><a class="nav-item" data-page="智能体" data-href="'+prefix+'pages/智能体.html">智能体</a></li>'+
'      <li role="none"><a class="nav-item" data-page="插件扩展" data-href="'+prefix+'pages/插件扩展.html">插件扩展</a></li>'+
'      <li role="none"><a class="nav-item" data-page="素材库" data-href="'+prefix+'pages/素材库.html">素材库</a></li>'+
'      <li role="none"><a class="nav-item" data-page="博客分享" data-href="'+prefix+'pages/博客分享.html">博客分享</a></li>'+
'    </ul>'+
'    <button class="mobile-toggle" id="mobileToggle" aria-label="切换菜单" aria-expanded="false">'+
'      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'+
'        <path d="M4 6h16M4 12h16M4 18h16"/>'+
'      </svg>'+
'    </button>'+
'  </div>'+
'</nav>';

// ── Active nav ──
if (pageName) {
  var pageMap = { 'UCFView':'接口文档' };
  var activePage = pageMap[pageName] || pageName;
  document.querySelectorAll('.nav-item[data-page]').forEach(function(el){
    if (el.getAttribute('data-page') === activePage) el.classList.add('active');
  });
}

// ── Mobile menu ──
(function(){
  var toggle = document.getElementById('mobileToggle');
  var navLinks = document.getElementById('navLinks');
  if (toggle && navLinks) {
    toggle.addEventListener('click', function(){
      var open = navLinks.classList.toggle('open');
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
  var a = e.target.closest('a[data-href]');
  if (a) {
    e.preventDefault();
    var h = a.getAttribute('data-href');
    if (h.charAt(0) === '#') {
      var t = document.querySelector(h);
      if (t) t.scrollIntoView({ behavior:'smooth' });
    } else {
      window.location.href = h;
    }
  }
});

// ── Footer year ──
var yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ── Navbar scroll effect ──
document.addEventListener('scroll', function(){
  var nav = document.getElementById('navbar');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 32);
}, { passive: true });

})();
