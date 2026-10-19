/* Bandada · pantallas de acceso (vista previa)
   Las cuentas todavía no existen: el ingreso y la recuperación validan los campos y lo dicen con claridad.
   El registro arma un mensaje para mandarlo por Instagram. Nada se guarda ni se envía a un servidor. */
(function () {
  'use strict';
  var IG = 'https://ig.me/m/bandada.world';
  var main = document.querySelector('.acceso');
  if (!main) return;
  var esEmpresa = main.classList.contains('acceso--empresas');
  var B = window.Bandada || {};

  /* ---------- paneles ---------- */
  var tablist = main.querySelector('[data-pestanas]');
  var tabs = Array.prototype.slice.call(main.querySelectorAll('[data-tab]'));
  var paneles = {};
  main.querySelectorAll('[data-panel]').forEach(function (p) { paneles[p.id] = p; });

  if (tablist) {
    tablist.hidden = false;
    main.classList.add('con-paneles');
    ['ingresar', 'registro'].forEach(function (id) {
      var p = paneles[id];
      if (!p) return;
      p.setAttribute('role', 'tabpanel');
      p.setAttribute('aria-labelledby', 'tab-' + id);
    });
  }

  function mostrar(id, enfocar) {
    if (!paneles[id]) id = 'ingresar';
    Object.keys(paneles).forEach(function (k) { paneles[k].hidden = k !== id; });
    var tabActiva = id === 'registro' ? 'registro' : 'ingresar';
    tabs.forEach(function (t) {
      var sel = t.getAttribute('data-tab') === tabActiva;
      t.setAttribute('aria-selected', sel ? 'true' : 'false');
      t.tabIndex = sel ? 0 : -1;
    });
    if (enfocar) {
      var foco = paneles[id].querySelector('h2') || paneles[id];
      foco.setAttribute('tabindex', '-1');
      foco.focus({ preventScroll: true });
    }
    if (window.gsap && B.motion) {
      window.gsap.fromTo(paneles[id], { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: 'expo.out' });
    }
  }

  function irA(id, enfocar) {
    if (history.replaceState) history.replaceState(null, '', '#' + id);
    mostrar(id, enfocar);
  }

  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { irA(t.getAttribute('data-tab'), false); });
    t.addEventListener('keydown', function (e) {
      var j = null;
      if (e.key === 'ArrowRight') j = (i + 1) % tabs.length;
      else if (e.key === 'ArrowLeft') j = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === 'Home') j = 0;
      else if (e.key === 'End') j = tabs.length - 1;
      if (j === null) return;
      e.preventDefault();
      tabs[j].focus();
      irA(tabs[j].getAttribute('data-tab'), false);
    });
  });
  main.addEventListener('click', function (e) {
    var a = e.target.closest('[data-ir]');
    if (!a) return;
    e.preventDefault();
    irA(a.getAttribute('data-ir'), true);
  });
  window.addEventListener('hashchange', function () { mostrar(location.hash.slice(1), true); });
  mostrar(location.hash.slice(1), false);

  /* ---------- mostrar contraseña ---------- */
  main.querySelectorAll('[data-ver-clave]').forEach(function (b) {
    b.addEventListener('click', function () {
      var input = b.parentNode.querySelector('input');
      var ver = input.type === 'password';
      input.type = ver ? 'text' : 'password';
      b.setAttribute('aria-pressed', ver ? 'true' : 'false');
      b.setAttribute('aria-label', ver ? 'Ocultar contraseña' : 'Mostrar contraseña');
    });
  });

  /* ---------- validación ---------- */
  var correo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function mensajeError(input) {
    var v = input.value.trim();
    if (input.required && !v) {
      if (input.tagName === 'SELECT') return 'Elegí una opción.';
      if (input.type === 'password') return 'Escribí tu contraseña.';
      return 'Completá este campo.';
    }
    if (v && input.type === 'email' && !correo.test(v)) return 'Revisá el correo: falta la arroba o el dominio.';
    if (v && input.type === 'number') {
      var n = Number(v);
      if (!Number.isInteger(n) || n < 1) return 'Escribí un número entero, por ejemplo 15.';
      if (n > 2000) return 'Escribí un número menor a 2000.';
    }
    return '';
  }

  function validar(form) {
    var primero = null;
    form.querySelectorAll('input:not([type="checkbox"]), select').forEach(function (input) {
      var err = document.getElementById(input.id + '-error');
      var m = mensajeError(input);
      input.setAttribute('aria-invalid', m ? 'true' : 'false');
      if (err) { err.textContent = m; err.hidden = !m; }
      if (m && !primero) primero = input;
    });
    if (primero) primero.focus();
    return !primero;
  }

  main.querySelectorAll('.form input, .form select').forEach(function (input) {
    input.addEventListener('input', function () {
      if (input.getAttribute('aria-invalid') !== 'true') return;
      var err = document.getElementById(input.id + '-error');
      var m = mensajeError(input);
      input.setAttribute('aria-invalid', m ? 'true' : 'false');
      if (err) { err.textContent = m; err.hidden = !m; }
    });
  });

  function estado(form, html, tipo) {
    var e = form.querySelector('[data-estado]');
    if (!e) return;
    e.className = 'form-estado' + (tipo ? ' form-estado--' + tipo : '');
    e.innerHTML = html;
  }

  var registrar = esEmpresa ? 'Registrar mi empresa' : 'Registrarme como trabajador';

  /* ---------- ingresar: vista previa sin cuentas ---------- */
  var login = main.querySelector('[data-login]');
  if (login) {
    login.addEventListener('submit', function (e) {
      e.preventDefault();
      estado(login, '', '');
      if (!validar(login)) return;
      var clave = login.querySelector('input[type="password"], input[name="clave"]');
      if (clave) { clave.value = ''; clave.type = 'password'; }
      var ver = login.querySelector('[data-ver-clave]');
      if (ver) { ver.setAttribute('aria-pressed', 'false'); ver.setAttribute('aria-label', 'Mostrar contraseña'); }
      estado(login, '<strong>Todavía no podés ingresar.</strong> Las cuentas no están habilitadas y no guardamos lo que escribiste. ' +
        'Para sumarte hoy, usá <a href="#registro" data-ir="registro">' + registrar + '</a>.', 'aviso');
    });
  }

  /* ---------- recuperar: vista previa sin cuentas ---------- */
  var rec = main.querySelector('[data-recuperar]');
  if (rec) {
    rec.addEventListener('submit', function (e) {
      e.preventDefault();
      estado(rec, '', '');
      if (!validar(rec)) return;
      estado(rec, '<strong>No enviamos ningún mensaje.</strong> La recuperación de contraseña se habilita junto con las cuentas. ' +
        'Si necesitás ayuda, escribinos por <a href="' + IG + '" target="_blank" rel="noopener">Instagram</a>.', 'aviso');
    });
  }

  /* ---------- registro: arma el mensaje para Instagram ---------- */
  function valor(form, sel) {
    var el = form.querySelector(sel);
    return el ? el.value.trim() : '';
  }

  function armarTexto(form, tipo) {
    var lineas;
    if (tipo === 'trabajador') {
      var cosechas = Array.prototype.map.call(form.querySelectorAll('input[name="cosechas"]:checked'), function (c) { return c.value; });
      lineas = [
        'Hola, Bandada. Quiero registrar mi interés como trabajador.',
        'Nombre: ' + valor(form, '#t-nombre'),
        'Salgo desde: ' + valor(form, '#t-lugar')
      ];
      if (cosechas.length) lineas.push('Cosechas que conozco: ' + cosechas.join(', '));
      var cuadrilla = valor(form, '#t-cuadrilla');
      if (cuadrilla) lineas.push('Cuadrilla: ' + cuadrilla);
    } else {
      lineas = [
        'Hola, Bandada. Quiero contarles sobre mi cosecha.',
        'Empresa o finca: ' + valor(form, '#e-empresa'),
        'Ubicación de la finca: ' + valor(form, '#e-lugar'),
        'Cultivo: ' + valor(form, '#e-cultivo')
      ];
      var mes = valor(form, '#e-mes');
      var personas = valor(form, '#e-personas');
      if (mes) lineas.push('Mes de inicio: ' + mes);
      if (personas) lineas.push('Personas: ' + personas);
    }
    return lineas.join('\n');
  }

  function copiar(texto) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(texto).then(function () { return true; }, function () { return false; });
    }
    return Promise.resolve(false);
  }

  main.querySelectorAll('[data-armar]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      estado(form, '', '');
      if (!validar(form)) return;
      var texto = armarTexto(form, form.getAttribute('data-armar'));
      var caja = form.querySelector('[data-mensaje]');
      var pre = form.querySelector('[data-mensaje-texto]');
      pre.textContent = texto;
      caja.hidden = false;
      // primero se copia (con la página todavía enfocada) y en el mismo gesto se abre Instagram,
      // para que el navegador no bloquee la pestaña nueva
      var copiado = copiar(texto);
      var ventana = window.open(IG, '_blank');
      if (ventana) ventana.opener = null;
      copiado.then(function (ok) {
        var enlace = '<a href="' + IG + '" target="_blank" rel="noopener">abrí el chat de Bandada</a>';
        if (ok) {
          estado(form, '<strong>Copiamos tu mensaje.</strong> ' + (ventana ? 'Se abrió Instagram en otra pestaña: pegalo en el chat y envialo desde ahí. Si no se abrió, ' + enlace + '.' : 'Ahora ' + enlace + ', pegalo y envialo desde ahí.') +
            ' Todavía no lo recibimos: llega cuando lo envíes.', 'ok');
        } else {
          var rango = document.createRange();
          rango.selectNodeContents(pre);
          var sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(rango);
          estado(form, '<strong>No pudimos copiar el mensaje solos.</strong> Ya está seleccionado: copialo, ' + enlace + ' y pegalo ahí para enviarlo.', 'aviso');
        }
      });
    });
  });
})();
