# Bandada

**Que tu temporada no se termine.**

Web de la propuesta de startup del equipo para el Mundial de Estudiantes de Administración 2026 (CLAM, Mendoza).

Bandada propone un circuito anual de cosechas que conecta cuadrillas de trabajadores rurales temporarios con productores: traslado coordinado, alojamiento verificado y registro laboral, tramo a tramo. Es un proyecto en validación; la web distingue lo que existe hoy, el piloto propuesto, la propuesta en validación y los objetivos futuros.

- Página: https://bandada.world/ (también https://nenocontreras.github.io/bandada/)
- Página del equipo: https://bandada.world/equipo/ (cada integrante toca su nombre y ve su próxima tarea, la cuenta regresiva y los links al Drive).
  Link directo por persona: `.../equipo/?p=nombre` (por ejemplo `?p=yas`). Para actualizar nombres, líderes o tareas se edita solo `equipo/datos.js`; las 49 tareas son las mismas del Tablero de tareas del Drive.

## Estructura

- `index.html`: la home "Un año conectado" (HTML, CSS y JS sin dependencias ni CDN). Tiene ocho partes: portada con el año entero, problema y oportunidad, circuito anual interactivo con mapa SVG en línea, entrada para productores (asistente de tres pasos con estimación orientativa), entrada para trabajadores (mensaje armado para Instagram), un tramo por dentro, estado del piloto, preguntas y cierre.
- `fuentes/index.html`: fuentes de cada dato, metodología de la estimación, procedencia de imágenes, declaración de uso de IA y lo que está pendiente de validar.
- `img/`: fotos en AVIF y WebP en varios tamaños, más `og.jpg` para redes. Cada archivo lleva su origen embebido en los metadatos.
- `fonts/`: Bricolage Grotesque, Atkinson Hyperlegible Next e IBM Plex Mono en woff2, alojadas en el propio sitio (licencia SIL Open Font).
- `equipo/`, `CNAME`, `robots.txt`: sin cambios. El sitio sigue con `noindex`.

Los controles interactivos (cabecera, pestañas, asistente, opciones, campos, chips, calendario, contador, caja de copia y preguntas) se portaron de Lucian UX/UI Prompt, con licencia MIT (c) 2026 Seokwoooo. Cada uno conserva su comentario de licencia en `index.html`.

## Canal de contacto

Por ahora el único canal es Instagram. En el script de `index.html`, `B.IG` apunta al chat de @bandada.world. La página no envía datos a ningún servidor: productores y trabajadores arman un mensaje, lo copian y lo mandan ellos mismos. No hay botón de WhatsApp ni formulario de preinscripción hasta que exista un número verificado y un formulario real.

## Procedencia de imágenes y datos

- Fotografías: ilustrativas, generadas con IA en Canva y después recortadas, compuestas y con una gradación común. Solo muestran personas adultas. No muestran trabajadores, productores ni clientes reales de Bandada, y la web las marca como tales.
- Ilustraciones de los pasos, gráfico de unidades, pasaporte y rueda del año: SVG dibujados para este sitio.
- Mapa: Natural Earth (dominio público), proyectado y simplificado para la web.
- Cifras: cada dato lleva su fuente al pie y el detalle en `fuentes/`. Lo que todavía no está confirmado figura en `fuentes/#pendiente`.

Documento de trabajo elaborado con apoyo de IA (Claude, Anthropic) para investigación, diseño y código; el equipo valida los supuestos y toma las decisiones.

## Estado anterior

La versión anterior de la home ("hoja de ruta de temporada") está en el commit `049a6e0`. Se puede ver con `git show 049a6e0:index.html` y las imágenes viejas se recuperan desde ese mismo commit.
