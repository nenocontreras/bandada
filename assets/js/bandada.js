/* Bandada · comportamiento compartido
   Desplazamiento suave (Lenis), cabecera, menú, apariciones, titulares por líneas y contadores.
   Todo el contenido es visible sin JavaScript; el movimiento se apaga con prefers-reduced-motion. */
(function () {
  'use strict';
  var doc = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var motion = !reduce.matches && !!window.gsap;
  var gsap = window.gsap;
  var lenis = null;

  if (window.gsap && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
  if (window.gsap && window.SplitText) gsap.registerPlugin(SplitText);
  if (!motion) doc.classList.remove('js-motion');

  /* ---------- desplazamiento suave ---------- */
  if (motion && window.Lenis && window.ScrollTrigger) {
    lenis = new Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  function altoCabecera() {
    var cab = document.querySelector('[data-cab]');
    return cab ? cab.offsetHeight : 0;
  }

  function irA(destino, enfocar, inmediato) {
    var y = destino.getBoundingClientRect().top + window.scrollY - altoCabecera() + 1;
    // Lenis mide el alto de la página con demora: si las secciones fijadas lo acaban de cambiar, recorta el destino
    if (lenis) lenis.resize();
    if (lenis) lenis.scrollTo(y, inmediato ? { immediate: true, force: true } : { duration: 1.2 });
    else window.scrollTo({ top: y, behavior: motion && !inmediato ? 'smooth' : 'auto' });
    if (enfocar) {
      if (!destino.hasAttribute('tabindex')) destino.setAttribute('tabindex', '-1');
      destino.focus({ preventScroll: true });
    }
  }

  // enlaces a anclas de la misma página
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="#"]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash || url.hash === '#') return;
    var destino = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    if (!destino || a.hasAttribute('data-ir')) return;
    e.preventDefault();
    cerrarMenu(false);
    history.pushState(null, '', url.hash);
    irA(destino, a.classList.contains('saltar'));
  });

  /* ---------- cabecera ---------- */
  var cab = document.querySelector('[data-cab]');
  var ultimoY = window.scrollY;
  function actualizarCabecera() {
    if (!cab) return;
    var y = window.scrollY;
    cab.classList.toggle('cab--fija', y > 24);
    var bajando = y > ultimoY + 4;
    var subiendo = y < ultimoY - 4;
    if (bajando && y > window.innerHeight * 0.6 && !menuAbierto) cab.classList.add('cab--oculta');
    else if (subiendo || y < 80) cab.classList.remove('cab--oculta');
    ultimoY = y;
  }
  if (lenis) lenis.on('scroll', actualizarCabecera);
  else window.addEventListener('scroll', actualizarCabecera, { passive: true });
  actualizarCabecera();
  if (cab) cab.addEventListener('focusin', function () { cab.classList.remove('cab--oculta'); });

  /* ---------- menú ---------- */
  var menu = document.querySelector('[data-menu]');
  var abrir = document.querySelector('[data-menu-abrir]');
  var menuAbierto = false;
  var enfoquePrevio = null;

  function enfocables() {
    return Array.prototype.filter.call(menu.querySelectorAll('a[href], button:not([disabled])'), function (el) {
      return el.offsetParent !== null;
    });
  }
  function abrirMenu() {
    if (!menu) return;
    enfoquePrevio = document.activeElement;
    menuAbierto = true;
    menu.classList.add('abierto');
    abrir.setAttribute('aria-expanded', 'true');
    if (lenis) lenis.stop();
    doc.style.overflow = 'hidden';
    window.setTimeout(function () { var b = menu.querySelector('.menu-cerrar'); if (b) b.focus(); }, 60);
  }
  function cerrarMenu(devolverFoco) {
    if (!menu || !menuAbierto) return;
    menuAbierto = false;
    menu.classList.remove('abierto');
    abrir.setAttribute('aria-expanded', 'false');
    if (lenis) lenis.start();
    doc.style.overflow = '';
    if (devolverFoco !== false && enfoquePrevio) enfoquePrevio.focus();
  }
  if (menu && abrir) {
    abrir.addEventListener('click', abrirMenu);
    menu.addEventListener('click', function (e) {
      if (e.target.closest('[data-menu-cerrar]')) cerrarMenu();
      else if (e.target.closest('a')) cerrarMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (!menuAbierto) return;
      if (e.key === 'Escape') { e.preventDefault(); cerrarMenu(); return; }
      if (e.key !== 'Tab') return;
      var els = enfocables();
      if (!els.length) return;
      var primero = els[0], ultimo = els[els.length - 1];
      if (e.shiftKey && document.activeElement === primero) { e.preventDefault(); ultimo.focus(); }
      else if (!e.shiftKey && document.activeElement === ultimo) { e.preventDefault(); primero.focus(); }
    });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', function (m) { if (m.matches) cerrarMenu(false); });
  }

  /* ---------- números ---------- */
  var formato = new Intl.NumberFormat('es-AR');

  if (!motion || !window.ScrollTrigger) {
    window.Bandada = { lenis: null, motion: false, irA: irA, formato: formato, listo: function (fn) { fn(); } };
    return;
  }

  /* ---------- apariciones ---------- */
  ScrollTrigger.batch('[data-reveal]', {
    start: 'top 88%',
    once: true,
    onEnter: function (els) {
      gsap.to(els, { opacity: 1, y: 0, duration: 1, ease: 'expo.out', stagger: 0.09, overwrite: true });
    }
  });

  /* ---------- titulares por líneas ---------- */
  function partirTitulares() {
    if (!window.SplitText) return;
    document.querySelectorAll('[data-split]').forEach(function (el) {
      SplitText.create(el, {
        type: 'lines',
        mask: 'lines',
        linesClass: 'split-linea',
        autoSplit: true,
        onSplit: function (self) {
          return gsap.from(self.lines, {
            yPercent: 110,
            duration: 1.1,
            ease: 'expo.out',
            stagger: 0.08,
            scrollTrigger: { trigger: el, start: 'top 88%', once: true }
          });
        }
      });
    });
  }

  /* ---------- contadores ---------- */
  function contadores() {
    document.querySelectorAll('[data-cuenta]').forEach(function (el) {
      var fin = parseFloat(el.getAttribute('data-cuenta'));
      var obj = { v: 0 };
      el.textContent = formato.format(0);
      gsap.to(obj, {
        v: fin,
        duration: fin > 1000 ? 2.2 : 1.6,
        ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 90%', once: true },
        onUpdate: function () { el.textContent = formato.format(Math.round(obj.v)); }
      });
    });
  }

  /* ---------- fotos: paralaje y recorte ---------- */
  function fotos() {
    document.querySelectorAll('[data-parallax]').forEach(function (fig) {
      var img = fig.querySelector('img');
      if (!img) return;
      gsap.fromTo(img, { yPercent: -7, scale: 1.16 }, {
        yPercent: 7, scale: 1.16, ease: 'none',
        scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: true }
      });
    });
    document.querySelectorAll('[data-clip]').forEach(function (fig) {
      var img = fig.querySelector('img');
      var tl = gsap.timeline({ scrollTrigger: { trigger: fig, start: 'top 85%', once: true } });
      tl.fromTo(fig, { clipPath: 'inset(14% 10% 14% 10% round 16px)' }, { clipPath: 'inset(0% 0% 0% 0% round 16px)', duration: 1.4, ease: 'expo.out' });
      if (img) tl.fromTo(img, { scale: 1.25 }, { scale: 1, duration: 1.6, ease: 'expo.out' }, 0);
    });
  }

  function iniciar() {
    partirTitulares();
    contadores();
    fotos();
    ScrollTrigger.refresh();
  }

  // espera las tipografías (o 1,2 s como máximo) para medir líneas con la letra final
  var esperaLetras = new Promise(function (ok) {
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(ok);
    else ok();
    window.setTimeout(ok, 1200);
  });
  function listo(fn) { esperaLetras.then(fn); }

  window.Bandada = { lenis: lenis, motion: true, irA: irA, formato: formato, listo: listo };
  listo(iniciar);
})();
