/* Bandada · movimiento de la portada
   Portada con la bandada de aves, frase del problema, circuito fijado en pantalla con la Ruta Norte,
   cómo funciona en horizontal, imagen flotante de servicios, carrusel del blog y cierre que se expande. */
(function () {
  'use strict';
  var B = window.Bandada || { motion: false, listo: function (fn) { fn(); } };
  var gsap = window.gsap;

  /* ---------- carrusel del blog (también sin movimiento) ---------- */
  var slider = document.querySelector('[data-slider]');
  if (slider) {
    var prev = document.querySelector('[data-slider-prev]');
    var next = document.querySelector('[data-slider-next]');
    var paso = function () {
      var li = slider.querySelector('li');
      return li ? li.getBoundingClientRect().width + 24 : slider.clientWidth * 0.8;
    };
    var estado = function () {
      var max = slider.scrollWidth - slider.clientWidth - 2;
      if (prev) prev.disabled = slider.scrollLeft <= 2;
      if (next) next.disabled = slider.scrollLeft >= max;
    };
    if (prev) prev.addEventListener('click', function () { slider.scrollBy({ left: -paso(), behavior: B.motion ? 'smooth' : 'auto' }); });
    if (next) next.addEventListener('click', function () { slider.scrollBy({ left: paso(), behavior: B.motion ? 'smooth' : 'auto' }); });
    slider.addEventListener('scroll', estado, { passive: true });
    window.addEventListener('resize', estado);
    estado();
  }

  /* ---------- mapa: medidas de la ruta ---------- */
  var circuito = document.querySelector('[data-circuito]');
  var mapa = circuito && circuito.querySelector('[data-mapa]');
  var ruta = mapa && mapa.querySelector('[data-ruta]');
  var ave = mapa && mapa.querySelector('[data-ave]');
  var largos = [0];
  var total = 0;
  if (mapa && ruta) {
    var ns = 'http://www.w3.org/2000/svg';
    mapa.getAttribute('data-legs').split('|').forEach(function (d) {
      var tmp = document.createElementNS(ns, 'path');
      tmp.setAttribute('d', d);
      tmp.setAttribute('fill', 'none');
      mapa.appendChild(tmp);
      total += tmp.getTotalLength();
      largos.push(total);
      mapa.removeChild(tmp);
    });
    total = ruta.getTotalLength();
  }

  function ponerAve(largo) {
    if (!ave || !ruta) return;
    var l = Math.max(0, Math.min(total, largo));
    var p = ruta.getPointAtLength(l);
    var q = ruta.getPointAtLength(Math.min(total, l + 2));
    var dx = q.x - p.x, dy = q.y - p.y;
    var giro = l >= total - 0.5 ? 0 : Math.atan2(dy, Math.abs(dx) || 0.001) * 180 / Math.PI;
    giro = Math.max(-35, Math.min(35, giro));
    var espejo = dx < -0.01 ? -1 : 1;
    ave.setAttribute('transform', 'translate(' + p.x.toFixed(1) + ' ' + p.y.toFixed(1) + ') scale(' + espejo + ' 1) rotate(' + (giro * espejo).toFixed(1) + ')');
  }

  function dibujar(largo) {
    if (!ruta) return;
    ruta.style.strokeDasharray = total + ' ' + total;
    ruta.style.strokeDashoffset = String(total - largo);
    ponerAve(largo);
  }

  if (!B.motion || !gsap || !window.ScrollTrigger) {
    if (ruta) { ruta.style.strokeDasharray = ''; ruta.style.strokeDashoffset = ''; }
    return;
  }

  B.listo(function () {
    var mm = gsap.matchMedia();

    /* ---------- portada ---------- */
    var titulo = document.querySelector('[data-hero-titulo]');
    var lados = document.querySelectorAll('[data-hero-lado]');
    var media = document.querySelector('[data-hero-media]');
    var hero = document.querySelector('.hero');
    if (titulo && window.SplitText) {
      SplitText.create(titulo, {
        type: 'lines, words', mask: 'lines', linesClass: 'split-linea', autoSplit: true,
        onSplit: function (self) {
          gsap.set(titulo, { autoAlpha: 1 });
          return gsap.from(self.words, { yPercent: 115, duration: 1.4, ease: 'expo.out', stagger: 0.06, delay: 0.15 });
        }
      });
    } else if (titulo) {
      gsap.to(titulo, { autoAlpha: 1, duration: 0.6 });
    }
    gsap.fromTo(lados, { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 1.2, ease: 'expo.out', stagger: 0.12, delay: 0.55 });
    if (media) {
      gsap.fromTo(media, { scale: 1.14 }, { scale: 1, duration: 2.6, ease: 'power3.out' });
      gsap.to(media.querySelector('img'), {
        yPercent: 14, ease: 'none',
        scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true }
      });
    }
    if (hero) {
      gsap.to('.hero-in, .hero-pie', {
        y: -70, autoAlpha: 0, ease: 'none',
        scrollTrigger: { trigger: hero, start: '35% top', end: 'bottom top', scrub: true }
      });
    }

    /* ---------- la bandada ---------- */
    var cielo = document.querySelector('[data-bandada]');
    if (cielo) {
      var href = 'img/marca/marca.svg#ave';
      var formacion = document.createElement('div');
      formacion.className = 'formacion';
      // formación en V: la que guía adelante y las demás en dos alas
      var lugares = [[0, 0, 1.0, 1], [-46, 24, .82, 0], [-46, -22, .78, 0], [-92, 46, .7, 0], [-90, -40, .66, 0], [-136, 66, .6, 0], [-134, -58, .56, 0], [-178, 86, .5, 0], [-188, -12, .52, 0]];
      lugares.forEach(function (l) {
        var s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        s.setAttribute('aria-hidden', 'true');
        s.setAttribute('class', 'ave-vuelo' + (l[3] ? ' guia' : ''));
        s.style.left = l[0] + 'px';
        s.style.top = l[1] + 'px';
        s.style.width = (44 * l[2]).toFixed(1) + 'px';
        var u = document.createElementNS('http://www.w3.org/2000/svg', 'use');
        u.setAttribute('href', href);
        s.appendChild(u);
        formacion.appendChild(s);
      });
      cielo.appendChild(formacion);
      var aves = formacion.querySelectorAll('.ave-vuelo');
      var vuelo = gsap.timeline({ repeat: -1, repeatDelay: 3 });
      vuelo.fromTo(formacion, { xPercent: 0, x: -260, y: 40 }, { x: function () { return cielo.clientWidth + 260; }, y: -30, duration: 30, ease: 'none' });
      aves.forEach(function (a, i) {
        gsap.to(a, { y: '+=' + (5 + (i % 3) * 2), duration: 1.6 + (i % 4) * 0.25, yoyo: true, repeat: -1, ease: 'sine.inOut' });
        gsap.to(a, { scaleY: 0.72, duration: 0.34 + (i % 3) * 0.05, yoyo: true, repeat: -1, ease: 'sine.inOut', delay: i * 0.07, transformOrigin: '50% 60%' });
      });
      vuelo.progress(0.18);
      ScrollTrigger.create({
        trigger: hero, start: 'top bottom', end: 'bottom top',
        onToggle: function (self) { self.isActive ? vuelo.play() : vuelo.pause(); }
      });
    }

    /* ---------- frase del problema ---------- */
    var frase = document.querySelector('[data-scrub-texto]');
    if (frase && window.SplitText) {
      SplitText.create(frase, {
        type: 'words', autoSplit: true,
        onSplit: function (self) {
          return gsap.fromTo(self.words, { opacity: 0.16 }, {
            opacity: 1, ease: 'none', stagger: 0.1,
            scrollTrigger: { trigger: frase, start: 'top 80%', end: 'bottom 45%', scrub: true }
          });
        }
      });
    }

    /* ---------- el circuito ---------- */
    if (circuito && ruta) {
      var tramos = circuito.querySelectorAll('.tramo');
      var meses = circuito.querySelectorAll('[data-mes]');
      var puntos = { sde: mapa.querySelector('[data-pt="sde"]'), cat: mapa.querySelector('[data-pt="cat"]'), tuc: mapa.querySelector('[data-pt="tuc"]'), per: mapa.querySelector('[data-pt="per"]') };
      var paradas = ['cat', 'tuc', 'tuc', 'per'];
      var activo = -1;

      var activar = function (i, vuelta) {
        circuito.classList.toggle('es-vuelta', !!vuelta);
        if (i === activo) return;
        activo = i;
        tramos.forEach(function (t, k) {
          t.classList.toggle('activo', k === i);
          t.classList.toggle('pasado', k < i);
          t.setAttribute('aria-hidden', k === i ? 'false' : 'true');
        });
        var rango = tramos[i].getAttribute('data-meses').split(',').map(Number);
        meses.forEach(function (m, k) {
          m.classList.toggle('activo', k >= rango[0] && k <= rango[1]);
          m.classList.toggle('pasado', k < rango[0]);
        });
        Object.keys(puntos).forEach(function (k) { if (puntos[k]) puntos[k].classList.remove('activo'); });
        var pt = puntos[paradas[i]];
        if (pt) pt.classList.add('activo', 'visitado');
        if (puntos.sde) puntos.sde.classList.add('visitado');
      };

      // progreso del scroll -> largo dibujado: tramo 1, tramo 2, pausa en Tucumán, tramo 3, vuelta a Catamarca
      var mapear = function (t) {
        var L = largos;
        if (t < 0.2) return L[1] * (t / 0.2);
        if (t < 0.42) return L[1] + (L[2] - L[1]) * ((t - 0.2) / 0.22);
        if (t < 0.56) return L[2];
        if (t < 0.8) return L[2] + (L[3] - L[2]) * ((t - 0.56) / 0.24);
        return L[3] + (L[4] - L[3]) * ((t - 0.8) / 0.2);
      };
      var indice = function (t) { return t < 0.2 ? 0 : t < 0.43 ? 1 : t < 0.58 ? 2 : 3; };

      mm.add('(min-width: 1024px) and (min-height: 620px)', function () {
        circuito.classList.add('es-pin');
        activo = -1;
        activar(0);
        dibujar(0);
        var st = ScrollTrigger.create({
          trigger: circuito,
          pin: circuito.querySelector('.circ-pin'),
          start: 'top top',
          end: '+=320%',
          scrub: 0.6,
          anticipatePin: 1,
          onUpdate: function (self) {
            var t = self.progress;
            dibujar(mapear(t));
            activar(indice(t), t > 0.86);
          }
        });
        return function () {
          st.kill();
          circuito.classList.remove('es-pin', 'es-vuelta');
          tramos.forEach(function (t) { t.classList.remove('activo', 'pasado'); t.removeAttribute('aria-hidden'); });
          meses.forEach(function (m) { m.classList.remove('activo', 'pasado'); });
          activo = -1;
        };
      });

      mm.add('(max-width: 1023.98px), (max-height: 619.98px)', function () {
        dibujar(0);
        var obj = { l: 0 };
        var tw = gsap.to(obj, {
          l: total, duration: 3.2, ease: 'power1.inOut',
          scrollTrigger: { trigger: mapa, start: 'top 75%', once: true },
          onUpdate: function () { dibujar(obj.l); }
        });
        gsap.utils.toArray(tramos).forEach(function (t) {
          gsap.from(t, { autoAlpha: 0, y: 30, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: t, start: 'top 88%', once: true } });
        });
        return function () { tw.kill(); };
      });
    }

    /* ---------- cómo funciona en horizontal ---------- */
    var como = document.querySelector('[data-como]');
    if (como) {
      mm.add('(min-width: 1024px) and (min-height: 620px)', function () {
        var lista = como.querySelector('.como-lista');
        var barra = como.querySelector('[data-como-barra]');
        como.classList.add('es-pin');
        var dist = function () { return Math.max(0, lista.scrollWidth - lista.clientWidth); };
        var tl = gsap.timeline({
          scrollTrigger: {
            trigger: como, pin: como.querySelector('.como-pin'), start: 'top top',
            end: function () { return '+=' + (dist() + window.innerHeight * 0.35); },
            scrub: 0.6, invalidateOnRefresh: true, anticipatePin: 1
          }
        });
        tl.to(lista, { x: function () { return -dist(); }, ease: 'none' }, 0)
          .fromTo(barra, { scaleX: 0 }, { scaleX: 1, ease: 'none' }, 0);
        return function () { como.classList.remove('es-pin'); };
      });
      mm.add('(max-width: 1023.98px), (max-height: 619.98px)', function () {
        gsap.utils.toArray(como.querySelectorAll('.etapa')).forEach(function (e) {
          gsap.from(e, { autoAlpha: 0, y: 28, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: e, start: 'top 88%', once: true } });
        });
      });
    }

    /* ---------- servicios: imagen que sigue al cursor ---------- */
    var serv = document.querySelector('[data-serv]');
    var flot = document.querySelector('[data-serv-flotante]');
    if (serv && flot) {
      mm.add('(hover: hover) and (pointer: fine) and (min-width: 1081px)', function () {
        var img = flot.querySelector('img');
        var xTo = gsap.quickTo(flot, 'x', { duration: 0.55, ease: 'power3' });
        var yTo = gsap.quickTo(flot, 'y', { duration: 0.55, ease: 'power3' });
        var mover = function (e) {
          var r = serv.getBoundingClientRect();
          xTo(e.clientX - r.left);
          yTo(e.clientY - r.top);
        };
        var entrar = function (e) {
          var li = e.currentTarget;
          var src = li.getAttribute('data-serv-img');
          if (src && img.getAttribute('src') !== src) img.setAttribute('src', src);
          gsap.to(flot, { autoAlpha: 1, scale: 1, duration: 0.45, ease: 'expo.out', overwrite: 'auto' });
        };
        var salir = function () { gsap.to(flot, { autoAlpha: 0, scale: 0.85, duration: 0.35, ease: 'power2.out', overwrite: 'auto' }); };
        var items = serv.querySelectorAll('.serv');
        gsap.set(flot, { autoAlpha: 0, scale: 0.85, xPercent: -50, yPercent: -50 });
        serv.addEventListener('pointermove', mover);
        items.forEach(function (li) { li.addEventListener('pointerenter', entrar); li.addEventListener('pointerleave', salir); });
        return function () {
          serv.removeEventListener('pointermove', mover);
          items.forEach(function (li) { li.removeEventListener('pointerenter', entrar); li.removeEventListener('pointerleave', salir); });
          gsap.set(flot, { autoAlpha: 0 });
        };
      });
      gsap.from(serv.querySelectorAll('.serv'), {
        autoAlpha: 0, y: 26, duration: 0.9, ease: 'expo.out', stagger: 0.07,
        scrollTrigger: { trigger: serv.querySelector('.serv-lista'), start: 'top 85%', once: true }
      });
    }

    /* ---------- cierre que se expande ---------- */
    var cierre = document.querySelector('[data-cierre]');
    if (cierre) {
      var cm = cierre.querySelector('[data-cierre-media]');
      gsap.fromTo(cm, { clipPath: 'inset(12% 7% 12% 7% round 24px)' }, {
        clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'none',
        scrollTrigger: { trigger: cierre, start: 'top bottom', end: 'top 15%', scrub: true }
      });
      gsap.fromTo(cm.querySelector('img'), { scale: 1.2 }, {
        scale: 1, ease: 'none',
        scrollTrigger: { trigger: cierre, start: 'top bottom', end: 'bottom top', scrub: true }
      });
    }

    /* ---------- carrusel: entrada ---------- */
    if (slider) {
      gsap.from(slider.querySelectorAll('li'), {
        autoAlpha: 0, x: 60, duration: 1.1, ease: 'expo.out', stagger: 0.08,
        scrollTrigger: { trigger: slider, start: 'top 85%', once: true }
      });
    }

    ScrollTrigger.refresh();

    // las secciones fijadas alargan la página después de cargar: si se llegó con un ancla, se vuelve a ubicar
    if (location.hash.length > 1 && B.irA) {
      var destino = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      var ubicar = function () { B.irA(destino, false, true); };
      if (destino && document.readyState === 'complete') window.requestAnimationFrame(ubicar);
      else if (destino) {
        window.addEventListener('load', function () {
          window.setTimeout(function () { ScrollTrigger.refresh(); ubicar(); }, 80);
        }, { once: true });
      }
    }
  });
})();
