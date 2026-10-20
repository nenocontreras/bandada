"""Genera las páginas públicas de bandada.world.

Uso: python -I tools/sitio.py

Escribe index.html, trabajadores/, empresas/, blog/, nosotros/ y fuentes/.
La cabecera, el menú y el pie son los mismos en todas las páginas.
/equipo/ e /ig/ no se tocan.
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PARTES = Path(__file__).resolve().parent / 'partes'
IG_PERFIL = 'https://www.instagram.com/bandada.world/'
EXT = ' target="_blank" rel="noopener"'


# ---------------------------------------------------------------- utilidades
def ico(p, nombre, clase='ico'):
    return f'<svg class="{clase}" aria-hidden="true" focusable="false"><use href="{p}img/iconos.svg#i-{nombre}"/></svg>'


def flecha(p):
    return ico(p, 'arrow-right', 'ico ico-flecha')


def foto(p, nombre, anchos, alt, sizes, ancho_real, alto_real, clase='', carga='lazy', extra=''):
    av = ', '.join(f'{p}img/foto/{nombre}-{a}.avif {a}w' for a in anchos)
    wb = ', '.join(f'{p}img/foto/{nombre}-{a}.webp {a}w' for a in anchos)
    prioridad = ' fetchpriority="high"' if carga == 'eager' else ''
    return (f'<figure class="foto {clase}"{extra}><picture>'
            f'<source type="image/avif" srcset="{av}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{wb}" sizes="{sizes}">'
            f'<img src="{p}img/foto/{nombre}-{anchos[0]}.webp" alt="{alt}" width="{ancho_real}" height="{alto_real}" loading="{carga}" decoding="async"{prioridad}>'
            f'</picture><span class="ia">Imagen ilustrativa · IA</span></figure>')


def tramo_foto(p, nombre, alt):
    return (f'<figure class="foto tramo-foto"><picture>'
            f'<source type="image/avif" srcset="{p}img/tramo-{nombre}-720.avif 720w, {p}img/tramo-{nombre}-1200.avif 1200w" sizes="(max-width: 900px) 92vw, 30vw">'
            f'<source type="image/webp" srcset="{p}img/tramo-{nombre}-720.webp 720w, {p}img/tramo-{nombre}-1200.webp 1200w" sizes="(max-width: 900px) 92vw, 30vw">'
            f'<img src="{p}img/tramo-{nombre}-720.webp" alt="{alt}" width="1200" height="800" loading="lazy" decoding="async">'
            f'</picture><span class="ia">Imagen ilustrativa · IA</span></figure>')


def logo(p):
    inicio = p or './'
    return (f'<a class="logo" href="{inicio}" aria-label="Bandada, inicio">'
            f'<svg class="ave" aria-hidden="true" focusable="false"><use href="{p}img/marca/marca.svg#ave"/></svg>'
            f'<svg class="palabra" aria-hidden="true" focusable="false"><use href="{p}img/marca/marca.svg#palabra"/></svg>'
            f'</a>')


NAV = [('Servicios', '#servicios'), ('Cómo funciona', '#como'), ('Rutas', '#rutas'), ('Blog', 'blog/'), ('Nosotros', 'nosotros/')]


def nav_href(p, href, inicio):
    if href.startswith('#'):
        return href if inicio else f'{p or "./"}{href}'
    return f'{p}{href}'


def actual_attr(cond):
    return ' aria-current="page"' if cond else ''


def cabecera(p, actual='', sobre=False, inicio=False):
    links = ''.join(f'<a href="{nav_href(p, h, inicio)}"{actual_attr(actual == t)}>{t}</a>' for t, h in NAV)
    clase = 'cab cab--sobre' if sobre else 'cab'
    return f'''<header class="{clase}" data-cab>
  <div class="cab-in ancho">
    {logo(p)}
    <nav class="cab-nav" aria-label="Principal">{links}</nav>
    <div class="cab-acc">
      <a class="btn btn--contorno btn--chico" href="{p}trabajadores/"{actual_attr(actual == 'Trabajadores')}>{ico(p, 'user-circle')}Trabajadores</a>
      <a class="btn btn--chico" href="{p}empresas/"{actual_attr(actual == 'Empresas')}>{ico(p, 'buildings')}Empresas</a>
    </div>
    <button class="cab-menu" type="button" aria-expanded="false" aria-controls="menu" data-menu-abrir>{ico(p, 'list')}<span>Menú</span></button>
  </div>
</header>'''


def menu(p, inicio=False):
    links = ''.join(f'<li><a href="{nav_href(p, h, inicio)}">{t}</a></li>' for t, h in NAV)
    return f'''<div class="menu" id="menu" data-menu>
  <div class="menu-velo" data-menu-cerrar></div>
  <div class="menu-panel" role="dialog" aria-modal="true" aria-label="Menú">
    <div class="menu-top">
      {logo(p)}
      <button class="menu-cerrar" type="button" data-menu-cerrar>{ico(p, 'x')}<span>Cerrar</span></button>
    </div>
    <div class="menu-acc">
      <a href="{p}trabajadores/"><strong>Trabajadores</strong><span>Tu próximo paso empieza acá</span>{ico(p, 'arrow-right')}</a>
      <a class="empresa" href="{p}empresas/"><strong>Empresas</strong><span>Planificá tu próxima cosecha</span>{ico(p, 'arrow-right')}</a>
    </div>
    <ul class="menu-links">{links}<li><a href="{p}fuentes/">Fuentes</a></li></ul>
    <p class="menu-red">{ico(p, 'instagram-logo')}<a href="{IG_PERFIL}"{EXT}>@bandada.world</a></p>
  </div>
</div>'''


def pie(p):
    i = p or './'
    return f'''<footer class="pie oscuro">
  <div class="ancho">
    <div class="pie-top">
      <div class="pie-marca">
        <img class="pie-logo" src="{p}img/marca/bandada-logo-claro.svg" alt="Bandada. Que la temporada no se termine" width="708" height="440" loading="lazy">
      </div>
      <div class="pie-cols">
        <div><h2>Servicio</h2><ul>
          <li><a href="{i}#servicios">Servicios</a></li>
          <li><a href="{i}#como">Cómo funciona</a></li>
          <li><a href="{i}#rutas">Rutas</a></li>
        </ul></div>
        <div><h2>Accesos</h2><ul>
          <li><a href="{p}trabajadores/">Trabajadores</a></li>
          <li><a href="{p}empresas/">Empresas</a></li>
        </ul></div>
        <div><h2>Bandada</h2><ul>
          <li><a href="{p}nosotros/">Nosotros</a></li>
          <li><a href="{p}blog/">Blog</a></li>
          <li><a href="{p}fuentes/">Fuentes y metodología</a></li>
        </ul></div>
        <div><h2>Contacto</h2><ul>
          <li><a class="pie-ig" href="{IG_PERFIL}"{EXT}>{ico(p, 'instagram-logo')}@bandada.world</a></li>
        </ul></div>
      </div>
    </div>
    <div class="pie-bajo">
      <p>Bandada está preparando su primer circuito. Las cifras del plan son hipótesis en validación y las fotos son imágenes ilustrativas generadas con IA. <a href="{p}fuentes/">Fuentes y metodología</a>.</p>
      <p>© 2026 Bandada</p>
    </div>
  </div>
</footer>'''


# marca la página como "con JS" y "con movimiento"; si bandada.js no llega a cargar en 4 s, devuelve todo a visible
HEAD_JS = ("<script>(function(d){d.classList.add('js');if(!matchMedia('(prefers-reduced-motion: reduce)').matches)"
           "{d.classList.add('js-motion');setTimeout(function(){if(!window.Bandada)d.classList.remove('js-motion')},4000)}})"
           "(document.documentElement);</script>")


def documento(p, titulo, descripcion, cuerpo, css=(), js=(), sobre=False, actual='', inicio=False, preload='', ruta=''):
    hojas = ''.join(f'\n<link rel="stylesheet" href="{p}assets/css/{c}.css">' for c in ('bandada', *css))
    scripts = ''.join(f'\n<script src="{p}assets/js/vendor/{v}.min.js" defer></script>' for v in ('gsap', 'ScrollTrigger', 'SplitText', 'lenis'))
    scripts += ''.join(f'\n<script src="{p}assets/js/{s}.js" defer></script>' for s in ('bandada', *js))
    return f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<meta name="theme-color" content="#12263D">
<link rel="canonical" href="https://bandada.world/{ruta}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="Bandada">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="https://bandada.world/{ruta}">
<meta property="og:image" content="https://bandada.world/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}img/marca/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{p}fonts/outfit.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}fonts/atkinson-hyperlegible-next.woff2" as="font" type="font/woff2" crossorigin>{preload}{hojas}
{HEAD_JS}{scripts}
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
{cabecera(p, actual, sobre, inicio)}
{menu(p, inicio)}
{cuerpo}
{pie(p)}
</body>
</html>
'''


def escribir(ruta, html):
    destino = RAIZ / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding='utf-8', newline='\n')
    print(ruta, len(html) // 1024, 'KB')


# ---------------------------------------------------------------- mapa
P = {'sde': (278.3, 210.4), 'tuc': (250.9, 178.3), 'per': (383.7, 415.2), 'cat': (234.9, 233.6)}


def curva(a, b, k):
    (ax, ay), (cx, cy) = P[a], P[b]
    mx, my, dx, dy = (ax + cx) / 2, (ay + cy) / 2, cx - ax, cy - ay
    return f'M{ax} {ay} Q{mx - dy * k:.1f} {my + dx * k:.1f} {cx} {cy}'


# la ruta: sale de Santiago del Estero, aceituna en Catamarca, limón y arándano en Tucumán,
# despanojado en Pergamino y vuelta a Catamarca en febrero
LEGS = [curva('sde', 'cat', 0.3), curva('cat', 'tuc', -0.35), curva('tuc', 'per', -0.16), curva('per', 'cat', -0.14)]


def mapa(p):
    base = (PARTES / 'mapa.svg').read_text(encoding='utf-8').split('\n', 1)[1]  # sin el comentario de origen
    casa = curva('tuc', 'sde', 0.5) + ' ' + curva('sde', 'tuc', 0.5)
    puntos = [
        ('sde', 'Santiago del Estero', 'Origen de las cuadrillas', 11, 4, 'start'),
        ('cat', 'Catamarca', 'Aceituna', -12, 10, 'end'),
        ('tuc', 'Tucumán', 'Limón y arándano', -12, -8, 'end'),
        ('per', 'Pergamino', 'Despanojado', -12, -9, 'end'),
    ]
    pts = ''
    for k, nombre, sub, dx, dy, ancla in puntos:
        x, y = P[k]
        pts += (f'<g class="pt pt-{k}" data-pt="{k}"><circle class="pt-anillo" cx="{x}" cy="{y}" r="7"/><circle class="pt-centro" cx="{x}" cy="{y}" r="3.2"/>'
                f'<text x="{x + dx}" y="{y + dy}" text-anchor="{ancla}"><tspan class="pt-n">{nombre}</tspan>'
                f'<tspan class="pt-s" x="{x + dx}" dy="10">{sub}</tspan></text></g>')
    sx, sy = P['sde']
    d = ' '.join(LEGS)
    return f'''<svg class="mapa" viewBox="172 128 270 312" role="img" aria-labelledby="mapa-t" data-mapa data-legs="{'|'.join(LEGS)}">
        <title id="mapa-t">Mapa de la Ruta Norte: sale de Santiago del Estero, pasa por Catamarca y Tucumán, sigue a Pergamino y en febrero vuelve a Catamarca.</title>
        {base}
        <path class="ruta-casa" d="{casa}"/>
        <path class="ruta-fondo" d="{d}"/>
        <path class="ruta" d="{d}" data-ruta/>
        {pts}
        <g class="ave-ruta" data-ave transform="translate({sx} {sy})"><svg x="-15" y="-10" width="30" height="19" overflow="visible"><use href="{p}img/marca/marca.svg#ave"/></svg></g>
      </svg>'''


# ---------------------------------------------------------------- contenido compartido
TRAMOS = [
    {'id': 'aceituna', 'meses': 'Feb a Abr', 'm': (0, 2), 'cultivo': 'Aceituna de mesa', 'lugar': 'Catamarca',
     'texto': 'La cosecha va de fines de enero hasta abril. Es la puerta de entrada al circuito.',
     'fuente': 'Catamarca Actual', 'alt': 'Cosecha de aceituna con mallas en Catamarca'},
    {'id': 'limon', 'meses': 'May a Jul', 'm': (3, 5), 'cultivo': 'Limón', 'lugar': 'Tucumán',
     'texto': 'Primero, una pausa en casa en mayo. La cosecha de limón emplea unas 40.000 personas.',
     'fuente': 'CEIL-CONICET (2024)', 'alt': 'Cosecha de limón en Tucumán'},
    {'id': 'arandano', 'meses': 'Ago a Oct', 'm': (6, 8), 'cultivo': 'Arándano', 'lugar': 'Tucumán',
     'texto': 'Pico de cosecha en septiembre y octubre, con 30 a 40 personas por hectárea. Al terminar, otra pausa en casa.',
     'fuente': 'IBO (2026)', 'alt': 'Manos cosechando arándanos'},
    {'id': 'despanojado', 'meses': 'Nov a Ene', 'm': (9, 11), 'cultivo': 'Despanojado de maíz', 'lugar': 'Pergamino, Buenos Aires',
     'texto': 'Unos 12.100 santiagueños viajaban cada campaña al despanojado del noreste bonaerense. En febrero, el circuito vuelve a empezar.',
     'fuente': 'Trabajo y Sociedad (2014)', 'alt': 'Despanojado de maíz en la pampa'},
]
MESES = ['Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic', 'Ene']

POSTS = [
    {'slug': 'circuito-de-cosechas', 'tag': 'Guía', 'titulo': 'Qué es un circuito de cosechas y cómo funciona la Ruta Norte',
     'bajada': 'Cuatro cosechas encadenadas en un año, con traslado coordinado y dos pausas en casa. Así está pensado el primer circuito de Bandada.',
     'img': ('limonar', [960, 1600], 1600, 900, 'Una cuadrilla trabaja en un limonar de Tucumán.'), 'min': 5},
    {'slug': 'alojamiento-inspeccionado', 'tag': 'Servicio', 'titulo': 'El alojamiento en la cosecha: quién lo da y qué revisa Bandada',
     'bajada': 'El productor aloja a la cuadrilla y Bandada inspecciona y aprueba el lugar antes de que llegue. Qué proponemos mirar en cada visita.',
     'img': ('alojamiento', [720, 1200], 1200, 800, 'Un inspector revisa una habitación de alojamiento rural.'), 'min': 4},
    {'slug': 'trazabilidad-social-2027', 'tag': 'Mercado', 'titulo': 'Trazabilidad social: qué cambia para la exportación desde 2027',
     'bajada': 'El 14/12/2027 empieza a regir el reglamento europeo contra el trabajo forzoso. Qué significa para quien exporta fruta y dónde encaja Cosecha Trazable.',
     'img': ('productor', [720, 1136], 1136, 1408, 'Un productor y un capataz revisan un plan de cosecha en un olivar.'), 'min': 4},
    {'slug': 'registrar-interes', 'tag': 'Trabajadores', 'titulo': 'Cómo registrar tu interés en Bandada, paso a paso',
     'bajada': 'Qué datos te pedimos, qué no te vamos a pedir en este paso y qué pasa después de que nos escribís.',
     'img': ('trabajadora', [720, 1136], 1136, 1408, 'Una trabajadora en un campo de arándanos al amanecer.'), 'min': 3},
]
FECHA_POSTS = '19 de octubre de 2026'


def tarjeta_post(p, post, clase='post-card', sizes='(max-width: 700px) 86vw, 420px', nivel='h3'):
    n, anchos, w, h, alt = post['img']
    return f'''<article class="{clase}">
  <a class="post-link" href="{p}blog/{post['slug']}/">
    {foto(p, n, anchos, alt, sizes, w, h, 'post-foto')}
    <div class="post-txt">
      <p class="post-meta"><span class="tag">{post['tag']}</span><span>{post['min']} min de lectura</span></p>
      <{nivel} class="post-t">{post['titulo']}</{nivel}>
      <p class="post-b">{post['bajada']}</p>
    </div>
  </a>
</article>'''


# ---------------------------------------------------------------- home
def home():
    p = ''
    meses = ''.join(f'<li data-mes="{i}">{m}</li>' for i, m in enumerate(MESES))
    tramos = ''
    for i, t in enumerate(TRAMOS):
        tramos += f'''
          <li class="tramo" data-tramo="{i}" data-meses="{t['m'][0]},{t['m'][1]}">
            {tramo_foto(p, t['id'], t['alt'])}
            <div class="tramo-txt">
              <p class="tramo-meses">{t['meses']}<span>Tramo {i + 1} de 4</span></p>
              <h3 class="t-h3">{t['cultivo']}</h3>
              <p class="tramo-lugar">{ico(p, 'map-trifold')}{t['lugar']}</p>
              <p class="tramo-texto">{t['texto']}</p>
              <p class="t-fuente">Fuente: {t['fuente']}</p>
            </div>
          </li>'''
    etapas = [
        ('clipboard-text', 'Pedido', 'La empresa nos cuenta su cosecha: cultivo, finca, fechas y cuántas personas necesita.'),
        ('users-three', 'Asignación', 'Armamos la cuadrilla con personas registradas en Bandada y un Jefe de Bandada a cargo.'),
        ('bus', 'Traslado y alojamiento', 'Micro desde el lugar de origen. El productor aloja y Bandada inspecciona el lugar antes de que llegue la cuadrilla.'),
        ('list-checks', 'Check-in y cosecha', 'Llegada registrada y acompañamiento durante el tramo. Si la cosecha se cae, buscamos reubicar a la cuadrilla con un objetivo de 72 horas.'),
        ('seal-check', 'Cierre del tramo', 'Cada tramo completado queda en el Pasaporte Bandada de cada persona y la empresa recibe el cierre del tramo.'),
    ]
    etapas_html = ''.join(
        f'<li class="etapa"><div class="etapa-cab"><span class="etapa-n">0{i + 1}</span>{ico(p, ic, "ico etapa-ico")}</div>'
        f'<h3 class="t-h3">{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(etapas))
    servicios = [
        ('users-three', 'Cuadrillas por temporada', 'Cuadrillas de 15 personas con un Jefe de Bandada que coordina en la finca.', '', 'tramo-limon-720'),
        ('bus', 'Traslado coordinado', 'Micro desde el lugar de origen hasta la finca y entre cosechas, con horarios acordados con la empresa.', '', 'tramo-despanojado-720'),
        ('house-line', 'Alojamiento inspeccionado', 'El productor aloja; Bandada inspecciona y aprueba el alojamiento antes de cada tramo.', '', 'foto/alojamiento-720'),
        ('path', 'Reubicación si la cosecha se cae', 'Buscamos otra finca del circuito para la cuadrilla, con un objetivo de 72 horas.', '', 'tramo-aceituna-720'),
        ('identification-card', 'Pasaporte Bandada', 'El historial de tramos completados de cada persona, que la acompaña de una cosecha a la otra.', '', 'foto/trabajadora-720'),
        ('seal-check', 'Cosecha Trazable', 'Registro por lote de quién cosechó, cuándo y con qué cuadrilla, pensado para auditorías sociales y compradores que lo piden.', 'En validación', 'foto/productor-720'),
    ]
    serv_html = ''
    for i, (ic, t, d, est, img) in enumerate(servicios):
        estado = f'<span class="estado estado--estudio">{est}</span>' if est else ''
        serv_html += (f'<li class="serv" data-serv-img="{p}img/{img}.webp"><span class="serv-n">0{i + 1}</span>{ico(p, ic, "ico serv-ico")}'
                      f'<h3 class="serv-t">{t}</h3><p class="serv-d">{d}</p><div class="serv-est">{estado}</div></li>')
    posts = ''.join(f'<li>{tarjeta_post(p, post)}</li>' for post in POSTS)
    norte = ''.join(f'<li><span class="t-meta">{t["meses"]}</span><strong>{t["cultivo"]}</strong><span>{t["lugar"]}</span></li>' for t in TRAMOS)
    sur = ''.join(f'<li><span class="t-meta">{m}</span><strong>{c}</strong><span>{l}</span></li>' for m, c, l in [
        ('Ene a Mar', 'Pera y manzana', 'Alto Valle'), ('Abr a Jun', 'Aceituna y nuez', 'Cuyo'),
        ('Jul a Sep', 'Poda', 'Cuyo'), ('Oct a Dic', 'Ajo y cereza', 'Mendoza')])

    cuerpo = f'''<main id="contenido">
  <section class="hero oscuro" aria-labelledby="hero-t">
    <div class="hero-media" data-hero-media>
      <picture>
        <source media="(max-width: 640px)" type="image/avif" srcset="img/foto/hero-cuadrilla-m-480.avif 480w, img/foto/hero-cuadrilla-m-708.avif 708w" sizes="100vw">
        <source media="(max-width: 640px)" type="image/webp" srcset="img/foto/hero-cuadrilla-m-480.webp 480w, img/foto/hero-cuadrilla-m-708.webp 708w" sizes="100vw">
        <source type="image/avif" srcset="img/foto/hero-cuadrilla-800.avif 800w, img/foto/hero-cuadrilla-1200.avif 1200w, img/foto/hero-cuadrilla-1680.avif 1680w" sizes="100vw">
        <source type="image/webp" srcset="img/foto/hero-cuadrilla-800.webp 800w, img/foto/hero-cuadrilla-1200.webp 1200w, img/foto/hero-cuadrilla-1680.webp 1680w" sizes="100vw">
        <img src="img/foto/hero-cuadrilla-1200.webp" alt="Una cuadrilla camina entre limoneros al atardecer, con los cerros de fondo." width="1680" height="944" fetchpriority="high" decoding="async">
      </picture>
    </div>
    <div class="hero-velo" aria-hidden="true"></div>
    <div class="bandada" aria-hidden="true" data-bandada></div>
    <div class="hero-in ancho">
      <h1 id="hero-t" class="t-display hero-t" data-hero-titulo>Que la temporada no se termine.</h1>
      <div class="hero-lado" data-hero-lado>
        <p class="hero-bajada">Bandada encadena cosechas de distintas regiones en un circuito anual: cuadrillas organizadas para las empresas productoras y una temporada que sigue para quienes cosechan.</p>
        <div class="hero-cta">
          <a class="btn" href="empresas/">Soy empresa {flecha(p)}</a>
          <a class="btn btn--claro" href="trabajadores/">Soy trabajador</a>
        </div>
      </div>
    </div>
    <div class="hero-pie ancho" data-hero-lado>
      <p>Ruta Norte <span aria-hidden="true">·</span> Catamarca <span aria-hidden="true">·</span> Tucumán <span aria-hidden="true">·</span> Pergamino</p>
      <a class="hero-bajar" href="#problema">Recorré el circuito {ico(p, 'caret-down')}</a>
    </div>
    <span class="ia">Imagen ilustrativa · IA</span>
  </section>

  <section class="seccion problema" id="problema" aria-labelledby="prob-t">
    <div class="ancho">
      <h2 id="prob-t" class="problema-frase" data-scrub-texto>En la cosecha no falta gente ni falta trabajo: están desencontrados. Cada campaña dura dos o tres meses y después hay que volver a empezar.</h2>
      <ul class="datos">
        <li data-reveal><p class="dato-n"><span data-cuenta="150000">150.000</span></p><p>personas siguen las cosechas cada año en la Argentina.</p><p class="t-fuente">Infobae, 27/09/2026</p></li>
        <li data-reveal><p class="dato-n"><span data-cuenta="67">67</span>%</p><p>de los asalariados agrícolas no está registrado.</p><p class="t-fuente">INDEC 2024, citado por Infobae</p></li>
        <li data-reveal><p class="dato-n">2 a 3</p><p>meses dura cada campaña. Después, la cuadrilla vuelve a casa a esperar la próxima.</p><p class="t-fuente">Infobae, 27/09/2026</p></li>
      </ul>
      <a class="enlace-flecha" href="fuentes/"><span>Ver todas las fuentes</span>{flecha(p)}</a>
    </div>
  </section>

  <section class="circuito oscuro" id="circuito" aria-labelledby="circ-t" data-circuito>
    <div class="circ-pin">
      <div class="circ-in ancho">
        <div class="circ-texto">
          <h2 id="circ-t" class="t-h2">Un año de trabajo, cuatro cosechas.</h2>
          <p class="circ-bajada">La Ruta Norte es el primer circuito. Sale de Santiago del Estero y encadena aceituna, limón, arándano y despanojado, con dos pausas en casa.</p>
          <ol class="circ-meses" aria-label="Meses del circuito, de febrero a enero">{meses}</ol>
          <ol class="tramos">{tramos}
          </ol>
        </div>
        <div class="circ-mapa">
      {mapa(p)}
          <p class="mapa-ley"><span class="ley-ruta"></span>Ruta del circuito <span class="ley-casa"></span>Pausa en casa</p>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion caminos" id="caminos" aria-labelledby="cam-t">
    <div class="ancho">
      <div class="sec-cabeza">
        <h2 id="cam-t" class="t-h2" data-split>Dos caminos, un mismo circuito.</h2>
        <p class="t-lead">Las empresas planifican su cosecha con una cuadrilla organizada. Quienes cosechan encadenan una temporada con la siguiente.</p>
      </div>
      <div class="caminos-grid">
        <article class="camino">
          {foto(p, 'productor', [720, 1136], 'Un productor y un capataz revisan el plan de cosecha en un olivar.', '(max-width: 800px) 92vw, 46vw', 1136, 1408, 'camino-foto', extra=' data-clip')}
          <div class="camino-txt">
            <h3 class="t-h3">Para empresas productoras</h3>
            <p>Pedí una cuadrilla para tu temporada. Nos ocupamos de armarla, trasladarla y acompañarla durante todo el tramo.</p>
            <ul class="lista-check">
              <li>{ico(p, 'check')}Cuadrillas de 15 personas con un Jefe de Bandada</li>
              <li>{ico(p, 'check')}Traslado coordinado desde el lugar de origen</li>
              <li>{ico(p, 'check')}Alojamiento del productor, inspeccionado y aprobado por Bandada</li>
            </ul>
            <div class="camino-cta"><a class="btn" href="empresas/">Soy empresa {flecha(p)}</a><a class="enlace-flecha" href="#servicios"><span>Ver servicios</span>{flecha(p)}</a></div>
          </div>
        </article>
        <article class="camino">
          {foto(p, 'trabajadora', [720, 1136], 'Una trabajadora mira el horizonte en un campo de arándanos al amanecer.', '(max-width: 800px) 92vw, 46vw', 1136, 1408, 'camino-foto', extra=' data-clip')}
          <div class="camino-txt">
            <h3 class="t-h3">Para quienes cosechan</h3>
            <p>Registrá tu interés: estamos armando el primer circuito. No es una oferta de trabajo, es el primer paso para sumarte.</p>
            <ul class="lista-check">
              <li>{ico(p, 'check')}Una temporada que sigue en la próxima cosecha</li>
              <li>{ico(p, 'check')}El servicio lo paga el productor: no pagás por acceder</li>
              <li>{ico(p, 'check')}Tu Pasaporte Bandada con los tramos que completaste</li>
            </ul>
            <div class="camino-cta"><a class="btn btn--azul" href="trabajadores/">Soy trabajador {flecha(p)}</a><a class="enlace-flecha" href="blog/registrar-interes/"><span>Cómo registrarte</span>{flecha(p)}</a></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="como" id="como" aria-labelledby="como-t" data-como>
    <div class="como-pin">
      <div class="ancho como-cabeza">
        <h2 id="como-t" class="t-h2" data-split>Cómo funciona.</h2>
        <p class="t-lead">Del pedido de la empresa al cierre del tramo, en cinco etapas.</p>
      </div>
      <div class="como-pista" data-como-pista>
        <ol class="como-lista ancho">{etapas_html}</ol>
      </div>
      <div class="ancho como-avance" aria-hidden="true"><span data-como-barra></span></div>
    </div>
  </section>

  <section class="seccion params oscuro" id="servicio" aria-labelledby="param-t">
    <div class="ancho params-grid">
      {foto(p, 'limonar', [960, 1600], 'Una cuadrilla trabaja en un limonar de Tucumán.', '(max-width: 900px) 92vw, 50vw', 1600, 900, 'params-foto', extra=' data-parallax')}
      <div class="params-txt">
        <h2 id="param-t" class="t-h2" data-split>Cómo está pensado el servicio.</h2>
        <p class="params-bajada">Son los parámetros del plan operativo del primer circuito: el diseño del servicio, no resultados.</p>
        <ul class="params-lista">
          <li data-reveal><strong><span data-cuenta="15">15</span></strong><span>personas por cuadrilla, con un Jefe de Bandada</span></li>
          <li data-reveal><strong><span data-cuenta="45">45</span></strong><span>asientos por micro: tres cuadrillas viajan juntas</span></li>
          <li data-reveal><strong><span data-cuenta="72">72</span> h</strong><span>de objetivo para reubicar a una cuadrilla si la cosecha se cae</span></li>
          <li data-reveal><strong><span data-cuenta="2">2</span></strong><span>pausas en casa durante el año</span></li>
        </ul>
        <p class="t-fuente">Fuente: Bandada, Logística y Operaciones y Finanzas: Rutas Norte y Sur (octubre de 2026).</p>
      </div>
    </div>
  </section>

  <section class="seccion servicios" id="servicios" aria-labelledby="serv-t" data-serv>
    <div class="ancho">
      <div class="sec-cabeza sec-cabeza--fila">
        <h2 id="serv-t" class="t-h2" data-split>Servicios para tu temporada.</h2>
        <p>Lo que incluye el servicio del primer circuito, hoy en preparación.</p>
      </div>
      <ul class="serv-lista">{serv_html}</ul>
      <div class="serv-cta"><a class="btn" href="empresas/#registro">Contanos tu cosecha {flecha(p)}</a></div>
    </div>
    <div class="serv-flotante" aria-hidden="true" data-serv-flotante><img alt="" src="img/foto/alojamiento-720.webp" width="720" height="480" loading="lazy" decoding="async"></div>
  </section>

  <section class="seccion rutas oscuro" id="rutas" aria-labelledby="rutas-t">
    <div class="ancho">
      <div class="sec-cabeza">
        <h2 id="rutas-t" class="t-h2" data-split>Empezamos por el norte.</h2>
        <p class="t-lead">Cada ruta encadena cosechas de una región para cubrir el año. La Ruta Norte es la primera; la Ruta Sur está en estudio.</p>
      </div>
      <div class="rutas-grid">
        <article class="ruta-card" data-reveal>
          <div class="ruta-cab"><h3 class="t-h3">Ruta Norte</h3><span class="estado">Primer circuito · en preparación</span></div>
          <p class="ruta-origen">Sale de Santiago del Estero. De febrero a enero.</p>
          <ol class="ruta-tramos">{norte}</ol>
        </article>
        <article class="ruta-card ruta-card--estudio" data-reveal>
          <div class="ruta-cab"><h3 class="t-h3">Ruta Sur</h3><span class="estado estado--estudio">En estudio · desde el año 2</span></div>
          <p class="ruta-origen">Entrada por Mendoza. Meses y lugares a confirmar.</p>
          <ol class="ruta-tramos">{sur}</ol>
        </article>
      </div>
    </div>
  </section>

  <section class="seccion blog-home" id="blog" aria-labelledby="blog-t">
    <div class="ancho blog-cab">
      <h2 id="blog-t" class="t-h2" data-split>Del blog.</h2>
      <div class="blog-acciones">
        <a class="enlace-flecha" href="blog/"><span>Ver todo el blog</span>{flecha(p)}</a>
        <div class="slider-ctrl">
          <button type="button" class="slider-btn" data-slider-prev aria-label="Notas anteriores">{ico(p, 'arrow-left')}</button>
          <button type="button" class="slider-btn" data-slider-next aria-label="Notas siguientes">{ico(p, 'arrow-right')}</button>
        </div>
      </div>
    </div>
    <div class="slider" data-slider><ul class="slider-pista">{posts}</ul></div>
  </section>

  <section class="cierre oscuro" aria-labelledby="cierre-t" data-cierre>
    <div class="cierre-media" data-cierre-media>
      <picture>
        <source type="image/avif" srcset="img/foto/aerea-maiz-1000.avif 1000w, img/foto/aerea-maiz-1680.avif 1680w" sizes="100vw">
        <source type="image/webp" srcset="img/foto/aerea-maiz-1000.webp 1000w, img/foto/aerea-maiz-1680.webp 1680w" sizes="100vw">
        <img src="img/foto/aerea-maiz-1000.webp" alt="" width="1680" height="944" loading="lazy" decoding="async">
      </picture>
      <span class="ia">Imagen ilustrativa · IA</span>
    </div>
    <div class="ancho cierre-in">
      <h2 id="cierre-t" class="t-display" data-split>Planifiquemos la próxima temporada.</h2>
      <p class="t-lead">Elegí tu camino. Mientras habilitamos las cuentas, te respondemos por Instagram.</p>
      <div class="hero-cta">
        <a class="btn" href="empresas/">Soy empresa {flecha(p)}</a>
        <a class="btn btn--claro" href="trabajadores/">Soy trabajador</a>
      </div>
    </div>
  </section>
</main>'''
    pre = ('\n<link rel="preload" as="image" type="image/avif" imagesrcset="img/foto/hero-cuadrilla-800.avif 800w, img/foto/hero-cuadrilla-1200.avif 1200w, img/foto/hero-cuadrilla-1680.avif 1680w" imagesizes="100vw" media="(min-width: 641px)" fetchpriority="high">'
           '\n<link rel="preload" as="image" type="image/avif" imagesrcset="img/foto/hero-cuadrilla-m-480.avif 480w, img/foto/hero-cuadrilla-m-708.avif 708w" imagesizes="100vw" media="(max-width: 640px)" fetchpriority="high">')
    escribir('index.html', documento(
        p, 'Bandada · Que la temporada no se termine',
        'Bandada encadena cosechas en un circuito anual: cuadrillas organizadas para empresas productoras y una temporada que sigue para quienes cosechan. Primer circuito: Ruta Norte.',
        cuerpo, css=('home',), js=('home',), sobre=True, inicio=True, preload=pre))


# ---------------------------------------------------------------- accesos
ACCESOS = {
    'trabajadores': {
        'titulo': 'Tu próximo paso empieza acá',
        'doc': 'Bandada · Acceso para trabajadores',
        'desc': 'Ingresá a tu espacio Bandada o registrá tu interés para sumarte al primer circuito. El servicio lo paga el productor: el trabajador no paga por acceder.',
        'foto': ('trabajadora', [720, 1136], 1136, 1408, 'Una trabajadora en un campo de arándanos al amanecer.'),
        'espacio': 'Tu espacio Bandada',
        'items': [('identification-card', 'Tu perfil y tu Pasaporte', 'Tus datos, las cosechas que conocés y los tramos que completaste.'),
                  ('map-trifold', 'Oportunidades', 'Los próximos tramos del circuito, con fechas, lugar y cultivo.'),
                  ('list-checks', 'Seguimiento de postulaciones', 'En qué estado está cada tramo al que te sumaste.')],
        'usuario': ('Celular o correo', 'text', 'El que vas a usar cuando habilitemos las cuentas.'),
        'registrar': 'Registrarme como trabajador',
        'otro': ('¿Sos empresa?', 'empresas/', 'Ingresá por acá'),
        'faq': [('¿Tengo que pagar algo?', 'No. El servicio lo paga el productor: el trabajador no paga por acceder.'),
                ('¿Registrarme me asegura un puesto?', 'No. Estamos armando el primer circuito y registrar tu interés no es una oferta de trabajo. Te avisamos cuando haya tramos abiertos.'),
                ('¿Qué datos me piden?', 'Tu nombre, de dónde salís y, si querés, qué cosechas conocés. En este paso no pedimos documentos ni datos de salud.'),
                ('¿Cuándo empieza el circuito?', 'Las fechas del primer circuito todavía no están confirmadas. Las vamos a anunciar por Instagram.')],
    },
    'empresas': {
        'titulo': 'Planificá tu próxima cosecha con Bandada',
        'doc': 'Bandada · Acceso para empresas',
        'desc': 'Ingresá al espacio de tu empresa o registrala para pedir cuadrillas organizadas para tu temporada.',
        'foto': ('productor', [720, 1136], 1136, 1408, 'Un productor y un capataz revisan el plan de cosecha en un olivar.'),
        'espacio': 'El espacio de tu empresa',
        'items': [('buildings', 'Perfil de la empresa', 'Fincas, cultivos, temporadas y personas de contacto.'),
                  ('users-three', 'Solicitud de cuadrillas', 'Cultivo, finca, fechas y cantidad de personas para cada tramo.'),
                  ('list-checks', 'Estado de las solicitudes', 'Del pedido a la asignación, el traslado y el cierre del tramo.')],
        'usuario': ('Correo de la empresa', 'email', ''),
        'registrar': 'Registrar mi empresa',
        'otro': ('¿Sos trabajador?', 'trabajadores/', 'Ingresá por acá'),
        'faq': [('¿Cuánto cuesta el servicio?', 'Depende del cultivo, las fechas y el tamaño de la cuadrilla. Los valores están en revisión: contanos tu cosecha y te respondemos.'),
                ('¿Quién da el alojamiento?', 'El productor aloja a la cuadrilla y Bandada inspecciona y aprueba el alojamiento antes de cada tramo.'),
                ('¿Qué pasa si la cosecha se cae?', 'Buscamos reubicar a la cuadrilla en otra finca del circuito, con un objetivo de 72 horas.'),
                ('¿Qué es Cosecha Trazable?', 'Un registro por lote de quién cosechó, cuándo y con qué cuadrilla, pensado para auditorías sociales. Está en validación.')],
    },
}


def campo(id_, etiqueta, tipo='text', auto='off', ayuda='', extra='', requerido=True):
    req = ' required' if requerido else ''
    ayuda_html = f'<p class="campo-ayuda" id="{id_}-ayuda">{ayuda}</p>' if ayuda else ''
    desc = f'{id_}-error' + (f' {id_}-ayuda' if ayuda else '')
    opc = '' if requerido else ' <span>(opcional)</span>'
    return (f'<div class="campo"><label for="{id_}">{etiqueta}{opc}</label>'
            f'<input id="{id_}" name="{id_}" type="{tipo}" autocomplete="{auto}"{req} aria-describedby="{desc}"{extra}>'
            f'{ayuda_html}<p class="campo-error" id="{id_}-error" hidden></p></div>')


def acceso(clave):
    p = '../'
    a = ACCESOS[clave]
    n, anchos, w, h, alt = a['foto']
    items = ''.join(f'<li>{ico(p, ic)}<div><strong>{t}</strong><span>{d}</span></div></li>' for ic, t, d in a['items'])
    faq = ''.join(f'<details><summary>{q}{ico(p, "caret-down")}</summary><p>{r}</p></details>' for q, r in a['faq'])
    u_et, u_tipo, u_ayuda = a['usuario']
    pre = clave[0]
    if clave == 'trabajadores':
        cosechas = ''.join(f'<label><input type="checkbox" name="cosechas" value="{v}"><span>{v.capitalize()}</span></label>'
                           for v in ('aceituna', 'limón', 'arándano', 'despanojado', 'otra'))
        registro = f'''
          <p class="panel-intro">Completá tus datos y armamos un mensaje para que lo mandes por Instagram, que es el canal que hoy tenemos abierto. Registrar tu interés no es una oferta de trabajo.</p>
          <form class="form" data-armar="trabajador" novalidate>
            {campo(pre + '-nombre', 'Tu nombre', auto='given-name')}
            {campo(pre + '-lugar', 'Desde dónde salís', auto='address-level2', ayuda='Localidad y provincia.')}
            <fieldset class="chips"><legend>Cosechas que conocés <span>(opcional)</span></legend>{cosechas}</fieldset>
            <div class="campo"><label for="{pre}-cuadrilla">¿Viajás con tu cuadrilla? <span>(opcional)</span></label>
              <select id="{pre}-cuadrilla" name="cuadrilla"><option value="">Elegí una opción</option><option>Sí, con mi cuadrilla</option><option>No, me sumo por mi cuenta</option><option>Todavía no sé</option></select></div>
            <p class="nota">{ico(p, 'info')}No pedimos documentos ni datos de salud en este paso.</p>
            <button class="btn btn--ancho" type="submit">{ico(p, 'copy')}Copiar mensaje y abrir Instagram</button>
            <div class="mensaje-armado" data-mensaje hidden><p class="mensaje-t">Tu mensaje</p><pre data-mensaje-texto></pre></div>
            <p class="form-estado" role="status" aria-live="polite" data-estado></p>
          </form>'''
    else:
        meses = ''.join(f'<option>{m}</option>' for m in ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
        registro = f'''
          <p class="panel-intro">Contanos tu cosecha y armamos un mensaje para que lo mandes por Instagram, que es el canal que hoy tenemos abierto. Te respondemos por ahí.</p>
          <form class="form" data-armar="empresa" novalidate>
            {campo(pre + '-empresa', 'Empresa o finca', auto='organization')}
            {campo(pre + '-lugar', 'Localidad y provincia de la finca', auto='off')}
            <div class="campo"><label for="{pre}-cultivo">Cultivo</label>
              <select id="{pre}-cultivo" name="cultivo" required aria-describedby="{pre}-cultivo-error"><option value="">Elegí un cultivo</option><option>Aceituna</option><option>Limón</option><option>Arándano</option><option>Despanojado de maíz</option><option>Otro</option></select>
              <p class="campo-error" id="{pre}-cultivo-error" hidden></p></div>
            <div data-si-otro="{pre}-cultivo" hidden>{campo(pre + '-cultivo-otro', '¿Qué cultivo?')}</div>
            <div class="campo-fila">
              <div class="campo"><label for="{pre}-mes">Mes de inicio <span>(opcional)</span></label>
                <select id="{pre}-mes" name="mes"><option value="">A definir</option>{meses}</select></div>
              {campo(pre + '-personas', 'Personas', tipo='number', extra=' min="1" max="2000" inputmode="numeric"', requerido=False)}
            </div>
            <button class="btn btn--ancho" type="submit">{ico(p, 'copy')}Copiar mensaje y abrir Instagram</button>
            <div class="mensaje-armado" data-mensaje hidden><p class="mensaje-t">Tu mensaje</p><pre data-mensaje-texto></pre></div>
            <p class="form-estado" role="status" aria-live="polite" data-estado></p>
          </form>'''
    otro_t, otro_h, otro_l = a['otro']
    cuerpo = f'''<main id="contenido" class="acceso acceso--{clave}">
  <aside class="acceso-lado oscuro" aria-labelledby="espacio-t">
    {foto(p, n, anchos, alt, '(max-width: 960px) 100vw, 44vw', w, h, 'acceso-foto', carga='eager')}
    <div class="acceso-lado-in">
      <span class="estado">Próximamente</span>
      <h2 id="espacio-t" class="t-h3">{a['espacio']}</h2>
      <p>Cuando habilitemos las cuentas, desde acá vas a tener:</p>
      <ul class="espacio-lista">{items}</ul>
    </div>
  </aside>
  <div class="acceso-main">
    <div class="acceso-in">
      <p class="acceso-otro">{otro_t} <a href="{p}{otro_h}">{otro_l}</a></p>
      <h1 class="t-h2 acceso-t">{a['titulo']}</h1>
      <div class="aviso" role="note">{ico(p, 'info')}<p><strong>Vista previa.</strong> Las cuentas todavía no están habilitadas. Esta pantalla muestra cómo va a funcionar el acceso y no guarda lo que escribas. Para sumarte hoy, usá «{a['registrar']}».</p></div>
      <div class="pestanas" role="tablist" aria-label="Opciones de acceso" data-pestanas hidden>
        <button type="button" role="tab" id="tab-ingresar" aria-controls="ingresar" aria-selected="true" data-tab="ingresar">Ingresar</button>
        <button type="button" role="tab" id="tab-registro" aria-controls="registro" aria-selected="false" tabindex="-1" data-tab="registro">{a['registrar']}</button>
      </div>

      <section class="panel" id="ingresar" aria-labelledby="ingresar-t" data-panel>
        <h2 class="t-h4 panel-t" id="ingresar-t">Ingresar</h2>
        <form class="form" data-login novalidate autocomplete="off">
          {campo(pre + '-usuario', u_et, tipo=u_tipo, ayuda=u_ayuda)}
          <div class="campo campo--clave"><label for="{pre}-clave">Contraseña</label>
            <div class="clave-caja"><input id="{pre}-clave" name="clave" type="password" autocomplete="off" required aria-describedby="{pre}-clave-error">
              <button type="button" class="clave-ver" data-ver-clave aria-pressed="false" aria-label="Mostrar contraseña">{ico(p, 'eye')}{ico(p, 'eye-slash', 'ico ico-oculta')}</button></div>
            <p class="campo-error" id="{pre}-clave-error" hidden></p></div>
          <p class="form-link"><a href="#recuperar" data-ir="recuperar">¿Olvidaste tu contraseña?</a></p>
          <button class="btn btn--ancho" type="submit">Ingresar {flecha(p)}</button>
          <p class="form-estado" role="status" aria-live="polite" data-estado></p>
        </form>
        <p class="panel-alt">¿Primera vez? <a href="#registro" data-ir="registro">{a['registrar']}</a></p>
      </section>

      <section class="panel" id="registro" aria-labelledby="registro-t" data-panel>
        <h2 class="t-h4 panel-t" id="registro-t">{a['registrar']}</h2>{registro}
        <p class="panel-alt">¿Ya tenés cuenta? <a href="#ingresar" data-ir="ingresar">Ingresar</a></p>
      </section>

      <section class="panel" id="recuperar" aria-labelledby="rec-t" data-panel>
        <h2 class="t-h4 panel-t" id="rec-t">Recuperar tu contraseña</h2>
        <p class="panel-intro">Escribí el dato con el que te registraste y te vamos a mandar los pasos para crear una contraseña nueva.</p>
        <form class="form" data-recuperar novalidate autocomplete="off">
          {campo(pre + '-rec', u_et, tipo=u_tipo)}
          <button class="btn btn--ancho" type="submit">Enviar instrucciones</button>
          <p class="form-estado" role="status" aria-live="polite" data-estado></p>
        </form>
        <p class="panel-alt"><a href="#ingresar" data-ir="ingresar">{ico(p, 'arrow-left')}Volver a ingresar</a></p>
      </section>

      <section class="acceso-faq" aria-labelledby="faq-t">
        <h2 id="faq-t" class="t-h4">Preguntas frecuentes</h2>
        <div class="faq">{faq}</div>
      </section>
    </div>
  </div>
</main>'''
    escribir(f'{clave}/index.html', documento(p, a['doc'], a['desc'], cuerpo, css=('accesos',), js=('accesos',),
                                               actual=clave.capitalize(), ruta=f'{clave}/'))


# ---------------------------------------------------------------- blog
def blog_indice():
    p = '../'
    principal, *resto = POSTS
    otras = ''.join(tarjeta_post(p, post, 'post-card post-card--fila', '(max-width: 900px) 40vw, 220px') for post in resto)
    cuerpo = f'''<main id="contenido" class="blog">
  <section class="seccion blog-top">
    <div class="ancho">
      <div class="sec-cabeza sec-cabeza--fila">
        <h1 class="t-display" data-split>Blog</h1>
        <p class="t-lead">Guías y novedades sobre cosechas, trabajo registrado y logística rural, con la fuente de cada dato.</p>
      </div>
      <div class="blog-grid">
        {tarjeta_post(p, principal, 'post-card post-card--grande', '(max-width: 900px) 92vw, 58vw', 'h2')}
        <div class="blog-lista">{otras}</div>
      </div>
    </div>
  </section>
</main>'''
    escribir('blog/index.html', documento(p, 'Bandada · Blog', 'Guías y novedades sobre cosechas, trabajo registrado y logística rural.', cuerpo,
                                          css=('blog',), actual='Blog', ruta='blog/'))


ARTICULOS = {
    'circuito-de-cosechas': '''
<p>Cada año, unas 150.000 personas siguen las cosechas en la Argentina. Cada campaña dura dos o tres meses. Cuando termina, la cuadrilla vuelve a casa y hay que volver a buscar la próxima. En la cosecha no falta gente ni falta trabajo: están desencontrados.</p>
<h2>La idea: encadenar cosechas</h2>
<p>Las cosechas de distintas regiones no ocurren al mismo tiempo. Si se ordenan en el calendario, una puede empezar cuando termina la otra. Un circuito de cosechas es eso: una secuencia de tramos que cubre el año, con el traslado entre fincas organizado de antemano.</p>
<h2>La Ruta Norte, mes a mes</h2>
<p>Es el primer circuito que estamos preparando. Sale de Santiago del Estero y tiene cuatro tramos:</p>
<ul>
<li><strong>Febrero a abril:</strong> aceituna de mesa en Catamarca.</li>
<li><strong>Mayo a julio:</strong> limón en Tucumán, después de una pausa en casa en mayo.</li>
<li><strong>Agosto a octubre:</strong> arándano en Tucumán. Al terminar, otra pausa en casa.</li>
<li><strong>Noviembre a enero:</strong> despanojado de maíz en Pergamino, Buenos Aires.</li>
</ul>
<p>En febrero el circuito vuelve a empezar. Los meses salen de fuentes públicas sobre cada cosecha y se van a ajustar con los productores de cada zona.</p>
<h2>Qué cambia para cada parte</h2>
<p>Para la empresa productora, la cuadrilla llega organizada: 15 personas con un Jefe de Bandada, traslado coordinado y un alojamiento que el productor ofrece y Bandada inspecciona antes de que llegue la cuadrilla. Para quien cosecha, la temporada sigue en la próxima cosecha en lugar de cortarse a los tres meses.</p>
<p>Según una estimación del equipo, una campaña suelta de limón suma unas 95 jornadas en el año. Con los cuatro tramos encadenados, el potencial de largo plazo ronda las 220 jornadas. Es una meta del plan, no una promesa.</p>
<h2>Qué falta confirmar</h2>
<p>Las fechas del piloto, los valores del servicio y el detalle de cada tramo se definen con las entrevistas a productores. Lo vamos a contar en este blog y en Instagram.</p>''',
    'alojamiento-inspeccionado': '''
<p>Cuando una cuadrilla viaja a cosechar, el lugar donde duerme y come es tan importante como el trabajo. En el modelo de Bandada el reparto es claro: <strong>el productor aloja a la cuadrilla; Bandada inspecciona y aprueba el alojamiento</strong> antes de que llegue.</p>
<h2>Por qué una inspección previa</h2>
<p>La cuadrilla llega lejos de su casa y por varias semanas. Revisar el lugar antes de cada tramo permite resolver problemas cuando todavía hay tiempo, y no con la gente ya instalada.</p>
<h2>Qué proponemos mirar</h2>
<p>Estos son los puntos con los que pensamos empezar. La lista final se define con el piloto y con los productores:</p>
<ul>
<li>Una cama para cada persona de la cuadrilla.</li>
<li>Agua potable, baños y duchas para todo el grupo.</li>
<li>Un lugar para cocinar o comer, y para guardar la comida.</li>
<li>Ventilación, luz y un lugar para guardar las cosas de cada persona.</li>
<li>Distancia y forma de llegar a la finca.</li>
</ul>
<h2>Qué pasa si algo no está bien</h2>
<p>Si la inspección encuentra algo para corregir, se acuerda con el productor antes de confirmar el tramo. El objetivo es que la cuadrilla no llegue a un lugar que nadie revisó.</p>
<p>La inspección forma parte del servicio que estamos preparando para el primer circuito, con inspectores en Catamarca, Tucumán y Buenos Aires.</p>''',
    'trazabilidad-social-2027': '''
<p>Los compradores de fruta piden cada vez más información sobre cómo se cosecha: quién trabajó, en qué condiciones y si el trabajo estaba registrado. Dos fechas hacen que el tema sea urgente para quienes exportan.</p>
<h2>El reglamento europeo contra el trabajo forzoso</h2>
<p>El 14/12/2027 empieza a regir el Reglamento (UE) 2024/3015 contra el trabajo forzoso. Para exportar a la Unión Europea va a hacer falta poder mostrar cómo se organizó el trabajo en la cadena, empezando por quién cosechó.</p>
<h2>El acuerdo UE-Mercosur</h2>
<p>El acuerdo comercial interino entre la Unión Europea y el Mercosur se aplica en forma provisoria desde el 01/05/2026. Más comercio con Europa también significa más auditorías y más preguntas sobre el origen de cada lote.</p>
<h2>Dónde encaja Cosecha Trazable</h2>
<p>Cosecha Trazable es un servicio que estamos validando: un registro por lote de quién cosechó, cuándo y con qué cuadrilla, pensado para auditorías sociales y para los compradores que lo piden. Todavía está en validación y no reemplaza ninguna certificación ni asesoramiento legal.</p>
<p>Si exportás y te interesa probarlo, contanos tu caso.</p>''',
    'registrar-interes': '''
<p>Estamos armando el primer circuito de Bandada, la Ruta Norte. Si querés sumarte, el primer paso es registrar tu interés. Te contamos cómo funciona.</p>
<h2>Paso 1: entrá a Trabajadores</h2>
<p>Arriba a la derecha de la página está el botón <strong>Trabajadores</strong>. En el celular, está dentro del menú. Ahí elegí <strong>Registrarme como trabajador</strong>.</p>
<h2>Paso 2: completá tus datos</h2>
<p>Te pedimos tu nombre, desde dónde salís y, si querés, qué cosechas conocés y si viajás con tu cuadrilla. <strong>No pedimos documentos ni datos de salud</strong> en este paso.</p>
<h2>Paso 3: mandanos el mensaje por Instagram</h2>
<p>La página arma un mensaje con tus datos y lo copia. Después se abre el chat de Instagram de Bandada: pegá el mensaje y envialo desde ahí. Hoy Instagram es el único canal que tenemos abierto.</p>
<h2>Lo que tenés que saber</h2>
<ul>
<li>El servicio lo paga el productor: el trabajador no paga por acceder.</li>
<li>Registrar tu interés no es una oferta de trabajo. Te avisamos cuando haya tramos abiertos.</li>
<li>Las fechas del primer circuito todavía no están confirmadas.</li>
</ul>''',
}
URL = {
    'infobae': 'https://www.infobae.com/sociedad/2026/09/27/aves-de-paso-la-larga-travesia-de-los-150-mil-trabajadores-golondrina-que-recorren-el-pais-detras-de-cada-cosecha/',
    'oit': 'https://www.ilo.org/sites/default/files/2026-04/Oportunidades%20y%20desafios%20para%20mejorar%20vida%20laboral%20migrantes.pdf',
    'huella': 'https://huelladelsur.ar/2026/09/03/el-gobierno-dejo-vencer-el-decreto-que-compatibiliza-trabajo-rural-y-planes-sociales-y-quedaron-120-000-puestos-de-trabajo-sin-certezas/',
    'fieldfisher': 'https://www.fieldfisher.com/en/locations/germany/insights/eu-forced-labour-regulation',
    'mercosur': 'https://trade.ec.europa.eu/access-to-markets/es/news/aplicacion-del-acuerdo-comercial-interino-ue-mercosur-el-1-de-mayo-de-2026',
    'ley26727': 'https://www.argentina.gob.ar/normativa/nacional/norma-192152/actualizacion',
    'ibo': 'https://www.internationalblueberry.org/2026/06/08/argentina-proyecta-una-cosecha-de-15-millones-de-kilos-de-arandanos-para-la-temporada-2026/',
    'scielo': 'https://www.scielo.org.ar/scielo.php?script=sci_arttext&amp;pid=S1514-68712014000100003',
    'ceil': 'https://www.ceil-conicet.gov.ar/wp-content/uploads/2024/11/mi18-EPT-limon.pdf',
}


def a_ext(clave, texto):
    return f'<a href="{URL[clave]}"{EXT}>{texto}</a>'


FUENTES_POST = {
    'circuito-de-cosechas': [f'Infobae (27/09/2026). {a_ext("infobae", "Aves de paso: la larga travesía de los 150 mil trabajadores golondrina")}.',
                             'Calendario de cada cosecha: ver Fuentes y metodología.',
                             'Bandada (2026). Finanzas: Rutas Norte y Sur v2.1, y Logística y Operaciones.'],
    'alojamiento-inspeccionado': ['Bandada (2026). Logística y Operaciones: cadena de abastecimiento y diseño organizacional.'],
    'trazabilidad-social-2027': [f'Fieldfisher. {a_ext("fieldfisher", "EU Forced Labour Regulation")} (en inglés).',
                                 f'Comisión Europea (2026). {a_ext("mercosur", "Aplicación del acuerdo comercial interino UE-Mercosur el 1 de mayo de 2026")}.'],
    'registrar-interes': ['Bandada (2026). Marketing: sitio web y plan de lanzamiento.'],
}


def articulo(post):
    p = '../../'
    n, anchos, w, h, alt = post['img']
    otras = [x for x in POSTS if x['slug'] != post['slug']][:2]
    fuentes_html = ''.join(f'<li>{f}</li>' for f in FUENTES_POST[post['slug']])
    sigue = ''.join(tarjeta_post(p, x, 'post-card post-card--fila', '(max-width: 900px) 40vw, 220px') for x in otras)
    if post['tag'] == 'Trabajadores':
        cta = f'<a class="btn btn--ancho" href="{p}trabajadores/#registro">Registrarme {flecha(p)}</a>'
    else:
        cta = f'<a class="btn btn--ancho" href="{p}empresas/#registro">Contanos tu cosecha {flecha(p)}</a>'
    cuerpo = f'''<main id="contenido" class="nota">
  <article>
    <header class="nota-cab ancho">
      <a class="enlace-flecha enlace-flecha--atras" href="../">{ico(p, 'arrow-left')}<span>Blog</span></a>
      <p class="post-meta"><span class="tag">{post['tag']}</span><span>{FECHA_POSTS}</span><span>{post['min']} min de lectura</span></p>
      <h1 class="t-h2 nota-t" data-split>{post['titulo']}</h1>
      <p class="t-lead">{post['bajada']}</p>
    </header>
    <div class="ancho">{foto(p, n, anchos, alt, '(max-width: 1320px) 92vw, 1320px', w, h, 'nota-foto', carga='eager')}</div>
    <div class="nota-cuerpo ancho">
      <div class="prosa">{ARTICULOS[post['slug']]}
        <div class="nota-fuentes"><h2>Fuentes</h2><ul>{fuentes_html}</ul><p><a href="{p}fuentes/">Ver fuentes y metodología</a></p></div>
      </div>
      <aside class="nota-aside"><p class="nota-aside-t">Equipo Bandada</p><p>Las cifras del plan son hipótesis en validación.</p>{cta}</aside>
    </div>
  </article>
  <section class="seccion nota-sigue" aria-labelledby="sigue-t">
    <div class="ancho"><h2 id="sigue-t" class="t-h3">Seguí leyendo</h2><div class="sigue-grid">{sigue}</div></div>
  </section>
</main>'''
    escribir(f'blog/{post["slug"]}/index.html', documento(p, f'{post["titulo"]} · Bandada', post['bajada'], cuerpo, css=('blog',),
                                                       actual='Blog', ruta=f'blog/{post["slug"]}/'))


# ---------------------------------------------------------------- nosotros
def nosotros():
    p = '../'
    valores = [('Continuidad', 'Que el trabajo siga de una cosecha a la otra.'),
               ('Encuentro', 'Juntar a quien necesita una cuadrilla con quien quiere trabajar.'),
               ('Formalidad', 'Trabajo registrado y reglas claras para todas las partes.'),
               ('Cumplimiento', 'Hacer lo que acordamos, en tiempo y forma.'),
               ('Transparencia', 'Decir qué sabemos, qué estamos probando y de dónde sale cada dato.')]
    val = ''.join(f'<li data-reveal><span class="valor-n">0{i + 1}</span><h3 class="t-h3">{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(valores))
    areas = [('Gerencia general', 'Define el rumbo y coordina las áreas.'),
             ('Administración y finanzas', 'Costos, cobros y el modelo de cada ruta.'),
             ('Marketing', 'La relación con productores y trabajadores, y este sitio.'),
             ('Innovación y tecnología', 'El Pasaporte Bandada, los pedidos y Cosecha Trazable.'),
             ('Recursos humanos', 'Registro, formación y acompañamiento de las cuadrillas.'),
             ('Administración de trabajadores rurales y logística', 'Traslados, alojamiento e inspecciones, con inspectores en Catamarca, Tucumán y Buenos Aires.'),
             ('Jefes de Bandada', 'El capataz de cada cuadrilla, a cargo en la finca.')]
    ar = ''.join(f'<li data-reveal><strong>{t}</strong><span>{d}</span></li>' for t, d in areas)
    cuerpo = f'''<main id="contenido" class="nos">
  <section class="seccion nos-top">
    <div class="ancho nos-top-grid">
      <h1 class="t-display" data-split>Encadenamos cosechas para que la temporada no se termine.</h1>
      <p class="t-lead">Bandada es una empresa de servicios para el trabajo rural de temporada. Conecta a las empresas productoras con cuadrillas organizadas y a quienes cosechan con una temporada que sigue en la próxima cosecha.</p>
    </div>
  </section>
  <div class="ancho">{foto(p, 'hero-cuadrilla', [1200, 1680], 'Una cuadrilla camina entre limoneros al atardecer.', '(max-width: 1320px) 92vw, 1320px', 1680, 944, 'nos-foto', extra=' data-parallax')}</div>
  <section class="seccion nos-mv" aria-label="Misión y visión">
    <div class="ancho nos-mv-grid">
      <div data-reveal><h2 class="nos-mv-t">Misión</h2><p class="nos-frase">Encadenar cosechas de distintas regiones en un circuito anual.</p></div>
      <div data-reveal><h2 class="nos-mv-t">Visión</h2><p class="nos-frase">Ser la red de referencia del trabajo rural de temporada en el Mercosur.</p></div>
    </div>
  </section>
  <section class="seccion oscuro nos-valores" aria-labelledby="val-t">
    <div class="ancho">
      <div class="sec-cabeza"><h2 id="val-t" class="t-h2" data-split>Lo que nos guía.</h2></div>
      <ul class="valores">{val}</ul>
    </div>
  </section>
  <section class="seccion nos-org" aria-labelledby="org-t">
    <div class="ancho nos-org-grid">
      <div class="sec-cabeza"><h2 id="org-t" class="t-h2" data-split>Cómo nos organizamos.</h2><p>La estructura prevista para el primer año de operación.</p></div>
      <ul class="org-lista">{ar}</ul>
    </div>
  </section>
  <section class="seccion nos-cta">
    <div class="ancho nos-cta-in">
      <h2 class="t-h2" data-split>¿Hablamos de tu próxima temporada?</h2>
      <div class="hero-cta"><a class="btn" href="../empresas/">Soy empresa {flecha(p)}</a><a class="btn btn--contorno" href="../trabajadores/">Soy trabajador</a></div>
    </div>
  </section>
</main>'''
    escribir('nosotros/index.html', documento(p, 'Bandada · Nosotros', 'Misión, visión, valores y organización de Bandada, el circuito anual de cosechas.', cuerpo,
                                              css=('paginas',), actual='Nosotros', ruta='nosotros/'))


# ---------------------------------------------------------------- fuentes
def fuentes():
    p = '../'
    cuerpo = f'''<main id="contenido" class="fuentes">
  <section class="seccion">
    <div class="ancho fuentes-grid">
      <div class="fuentes-cab">
        <h1 class="t-h2" data-split>Fuentes y metodología.</h1>
        <p class="t-lead">De dónde sale cada dato del sitio, qué es una meta del plan y qué falta confirmar.</p>
        <nav class="fuentes-indice" aria-label="En esta página"><ul>
          <li><a href="#problema">Datos del problema</a></li><li><a href="#calendario">Calendario de la Ruta Norte</a></li>
          <li><a href="#servicio">Parámetros y metas del plan</a></li><li><a href="#recursos">Imágenes y recursos</a></li>
          <li><a href="#ia">Uso de IA</a></li><li><a href="#falta">Qué falta confirmar</a></li></ul></nav>
      </div>
      <div class="prosa">
        <h2 id="problema">Datos del problema</h2>
        <ul class="refs">
          <li><p>Unas 150.000 personas siguen las cosechas cada año; 35.000 salen de Santiago del Estero en cuadrillas de 13 a 17. Las campañas duran dos o tres meses. El 67% de los asalariados agrícolas no está registrado (INDEC 2024, citado por la nota).</p><p class="ref">Infobae (27/09/2026). {a_ext('infobae', 'Aves de paso: la larga travesía de los 150 mil trabajadores golondrina')}.</p></li>
          <li><p>El 6% de los migrantes rurales accedió a la prestación por desempleo.</p><p class="ref">OIT (2026). {a_ext('oit', 'Informe sobre trabajadores migrantes rurales en Argentina')} (PDF).</p></li>
          <li><p>El 01/09/2026 venció el decreto 514/2021, que permitía cobrar un plan social y trabajar registrado en la cosecha.</p><p class="ref">Huella del Sur (03/09/2026). {a_ext('huella', 'El Gobierno dejó vencer el decreto que compatibiliza trabajo rural y planes sociales')}.</p></li>
          <li><p>El Reglamento UE 2024/3015 contra el trabajo forzoso rige desde el 14/12/2027.</p><p class="ref">Fieldfisher. {a_ext('fieldfisher', 'EU Forced Labour Regulation')} (en inglés).</p></li>
          <li><p>El acuerdo comercial UE-Mercosur se aplica en forma provisoria desde el 01/05/2026.</p><p class="ref">Comisión Europea (2026). {a_ext('mercosur', 'Aplicación del acuerdo comercial interino UE-Mercosur el 1 de mayo de 2026')}.</p></li>
          <li><p>El traslado y el alojamiento quedan a cargo del empleador.</p><p class="ref">{a_ext('ley26727', 'Ley 26.727 de Trabajo Agrario, texto actualizado')}.</p></li>
        </ul>
        <h2 id="calendario">Calendario de la Ruta Norte</h2>
        <p>La Ruta Norte es la propuesta para el año 1, de febrero a enero, según el documento interno Finanzas: Rutas Norte y Sur v2.1 (octubre de 2026). Los meses de cada cosecha salen de estas fuentes públicas:</p>
        <ul class="refs">
          <li><p><strong>Aceituna de mesa, Catamarca, feb a abr.</strong> La cosecha va de fines de enero hasta abril.</p><p class="ref">Catamarca Actual, nota sobre el calendario de la aceituna de mesa. <span class="sin">Falta recuperar el enlace.</span></p></li>
          <li><p><strong>Limón, Tucumán, may a jul.</strong> La cosecha emplea unas 40.000 personas y tiene su pico en julio y agosto.</p><p class="ref">CEIL-CONICET (2024). {a_ext('ceil', 'Informe sobre la cosecha de limón en Tucumán')} (PDF).</p></li>
          <li><p><strong>Arándano, Tucumán, ago a oct.</strong> Pico de cosecha en septiembre y octubre, con 30 a 40 personas por hectárea en plena temporada.</p><p class="ref">IBO (08/06/2026). {a_ext('ibo', 'Argentina proyecta una cosecha de 15 millones de kilos de arándanos para la temporada 2026')}.</p></li>
          <li><p><strong>Despanojado de maíz, Pergamino, nov a ene.</strong> Unos 12.100 santiagueños viajaban cada campaña al despanojado del noreste bonaerense, según un estudio de 2014.</p><p class="ref">Trabajo y Sociedad (2014). {a_ext('scielo', 'Artículo sobre el despanojado')}, en SciELO Argentina.</p></li>
          <li><p><strong>Ruta Sur, en estudio desde el año 2.</strong> Entrada por Mendoza: pera y manzana en el Alto Valle, aceituna y nuez en Cuyo, poda, y ajo y cereza en Mendoza. Es un objetivo del plan: meses, lugares y fuentes de cada tramo a confirmar.</p><p class="ref">Bandada (2026). Finanzas: Rutas Norte y Sur v2.1.</p></li>
        </ul>
        <h2 id="servicio">Parámetros y metas del plan</h2>
        <p>Cuadrillas de 15 personas con un Jefe de Bandada, micros de 45 asientos para tres cuadrillas, un objetivo de reubicación de 72 horas si una cosecha se cae y dos pausas en casa por año. Salen de los documentos internos Logística y Operaciones y Finanzas: Rutas Norte y Sur v2.1 (octubre de 2026). Son el diseño del servicio, no resultados.</p>
        <dl class="calc">
          <div><dt>Hoy, unas 95 jornadas</dt><dd>Una campaña suelta de limón, de 2 a 3 meses, de lunes a sábado. Estimación del equipo con datos de Infobae (2026).</dd></div>
          <div><dt>Circuito completo, unas 220</dt><dd>Los cuatro tramos encadenados con dos pausas en casa. Es el potencial de largo plazo, no una promesa.</dd></div>
          <div><dt>Metas del plan</dt><dd>90 jornadas por persona en el año 1, 130 en el año 2 y 160 en el año 3.</dd></div>
        </dl>
        <p>Los valores del servicio no se publican hasta completar la revisión legal del modelo.</p>
        <h2 id="recursos">Imágenes y recursos</h2>
        <ul class="refs">
          <li><p><strong>Fotografías.</strong> Ilustrativas, generadas con IA en Canva y convertidas para el sitio. Muestran personas adultas y no muestran trabajadores, productores ni clientes reales de Bandada. La web las marca como «Imagen ilustrativa · IA» y cada archivo lleva al lado su prompt de generación.</p></li>
          <li><p><strong>Logo.</strong> Diseñado por el área Identidad de Bandada. Para la web se pasó a vector manteniendo el ave, la palabra y el lema originales.</p></li>
          <li><p><strong>Mapa.</strong> Natural Earth, dominio público, proyectado y simplificado para la web.</p></li>
          <li><p><strong>Tipografías.</strong> Outfit y Atkinson Hyperlegible Next, con licencia SIL Open Font, alojadas en el propio sitio.</p></li>
          <li><p><strong>Íconos.</strong> Phosphor Icons, licencia MIT.</p></li>
          <li><p><strong>Animación.</strong> GSAP (licencia estándar de GreenSock) y Lenis (licencia MIT), alojadas en el propio sitio.</p></li>
        </ul>
        <h2 id="ia">Declaración de uso de IA</h2>
        <p>Según los artículos 25 a 28 del reglamento del Mundial de Estudiantes de Administración 2026.</p>
        <div class="apa">
          <p>Anthropic. (2026). <i>Claude</i> (Opus 5.5) [Modelo de lenguaje de gran escala]. https://claude.ai</p>
          <p>Canva. (2026). <i>Canva</i> [Plataforma de diseño con generación de imágenes por IA]. https://www.canva.com</p>
        </div>
        <p>Claude se usó para investigar, redactar borradores, diseñar y programar este sitio. Canva se usó para generar las fotografías ilustrativas. El equipo revisó el contenido, toma las decisiones y responde por cada dato.</p>
        <h2 id="falta">Qué falta confirmar</h2>
        <ul>
          <li>Fechas del piloto de la Ruta Norte.</li>
          <li>Valores del servicio, jornal y movilidad, que se ajustan con las entrevistas a productores y la revisión legal.</li>
          <li>Costos de alojamiento en cada tramo.</li>
          <li>Meses y fuentes de cada tramo de la Ruta Sur.</li>
          <li>Enlace a la nota de Catamarca Actual sobre la aceituna de mesa.</li>
          <li>Alcance legal de la intermediación en el agro tras la Ley 27.742, con asesoramiento legal.</li>
          <li>Cuentas de usuario para trabajadores y empresas: hoy las pantallas de acceso son una vista previa.</li>
          <li>Otros canales de contacto: por ahora el único es Instagram, <a href="{IG_PERFIL}"{EXT}>@bandada.world</a>.</li>
        </ul>
        <p class="t-fuente">Propuesta de startup para el Mundial de Estudiantes de Administración 2026 (CLAM, Mendoza). Las cifras del plan son hipótesis en validación.</p>
      </div>
    </div>
  </section>
</main>'''
    escribir('fuentes/index.html', documento(p, 'Bandada · Fuentes y metodología', 'De dónde sale cada dato del sitio de Bandada, qué es una meta del plan y qué falta confirmar.',
                                             cuerpo, css=('paginas',), ruta='fuentes/'))


if __name__ == '__main__':
    home()
    acceso('trabajadores')
    acceso('empresas')
    blog_indice()
    for post in POSTS:
        articulo(post)
    nosotros()
    fuentes()
