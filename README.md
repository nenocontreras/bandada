# Bandada

**Que la temporada no se termine.**

Web de la propuesta de startup del equipo para el Mundial de Estudiantes de Administración 2026 (CLAM, Mendoza).

Bandada propone un circuito anual de cosechas que conecta cuadrillas de trabajadores rurales temporarios con empresas productoras: traslado coordinado, alojamiento inspeccionado y registro laboral, tramo a tramo. Es un proyecto en validación; la web distingue lo que existe hoy, el plan del primer circuito y lo que está en estudio.

- Página: https://bandada.world/ (también https://nenocontreras.github.io/bandada/)
- Página del equipo: https://bandada.world/equipo/ (cada integrante toca su nombre y ve su próxima tarea, la cuenta regresiva y los links al Drive).
  Link directo por persona: `.../equipo/?p=nombre` (por ejemplo `?p=yas`). Para actualizar nombres, líderes o tareas se edita solo `equipo/datos.js`; las 49 tareas son las mismas del Tablero de tareas del Drive.

## Estructura

Las páginas se generan con `python -I tools/sitio.py` desde la raíz del repo. Para cambiar un texto se edita `tools/sitio.py` y se vuelve a generar; los HTML no se editan a mano.

- `index.html`: portada de empresa de servicios. Portada con la bandada en vuelo, el problema con datos y fuente, el circuito anual con mapa y recorrido animado, los dos caminos (empresas y trabajadores), cómo funciona, los parámetros del plan, servicios, rutas, notas del blog y cierre.
- `trabajadores/` y `empresas/`: accesos separados con ingreso, registro y recuperación de contraseña. Son una **vista previa**: no hay cuentas todavía, no se guarda nada en el navegador y no se envía nada a ningún servidor. El registro arma un mensaje que la persona copia y manda por Instagram.
- `blog/`: índice y cuatro notas.
- `nosotros/`: misión, visión, valores y estructura prevista.
- `fuentes/`: fuentes de cada dato, calendario, parámetros y metas del plan, procedencia de imágenes, uso de IA y lo que falta confirmar.
- `assets/css/` y `assets/js/`: estilos y comportamiento. El movimiento usa GSAP 3.13 (ScrollTrigger, SplitText) y Lenis 1.1.13, alojados en `assets/js/vendor/` sin CDN. Con «reducir movimiento» activado todo se ve sin animaciones.
- `img/foto/`: fotos en AVIF y WebP en varios tamaños (`tools/fotos.py` las prepara). `img/marca/`: logo y favicon de Identidad. `img/iconos.svg`: íconos Phosphor (MIT).
- `fonts/`: Outfit y Atkinson Hyperlegible Next en woff2, alojadas en el propio sitio (licencia SIL Open Font). Bricolage Grotesque e IBM Plex Mono quedan porque las usa `equipo/`.
- `equipo/`, `ig/`, `CNAME`, `robots.txt`: sin cambios. El sitio sigue con `noindex`.

## Canal de contacto

Por ahora el único canal es Instagram (@bandada.world). La dirección está en `assets/js/accesos.js` y en `tools/sitio.py`. La página no envía datos a ningún servidor. No hay botón de WhatsApp hasta que exista un número verificado.

## Qué falta para cuentas reales

Para que el ingreso funcione de verdad hacen falta: un proveedor de autenticación y un backend, una base de datos, roles y permisos separados para trabajadores y empresas, contraseñas guardadas con hash seguro, recuperación por correo o SMS, política de privacidad y revisión legal.

## Procedencia de imágenes y datos

- Fotografías: ilustrativas, generadas con IA y después recortadas y con una gradación común. Solo muestran personas adultas. No muestran trabajadores, productores ni clientes reales de Bandada, y la web las marca como «Imagen ilustrativa · IA».
- Mapa: Natural Earth (dominio público), proyectado y simplificado para la web.
- Cifras: cada dato lleva su fuente y el detalle en `fuentes/`. Lo que todavía no está confirmado figura en `fuentes/`, en «Qué falta confirmar».

Documento de trabajo elaborado con apoyo de IA (Claude, Anthropic) para investigación, diseño y código; el equipo valida los supuestos y toma las decisiones.

## Estado anterior

La versión anterior de la home ("Un año conectado") está en el commit `d812ba8`. Se puede ver con `git show d812ba8:index.html`.
