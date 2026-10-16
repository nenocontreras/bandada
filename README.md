# Bandada

**Que tu temporada no se termine.**

Web de la propuesta de startup del equipo para el Mundial de Estudiantes de Administración 2026 (CLAM, Mendoza).

Bandada propone un circuito anual de cosechas que conecta cuadrillas de trabajadores rurales temporarios con productores: traslado coordinado, alojamiento verificado y registro laboral, tramo a tramo. Es un proyecto en validación; la web distingue lo que existe hoy, el piloto propuesto, la propuesta en validación y los objetivos futuros.

- Página: https://bandada.world/ (también https://nenocontreras.github.io/bandada/)
- Página del equipo: https://bandada.world/equipo/ (cada integrante toca su nombre y ve su próxima tarea, la cuenta regresiva y los links al Drive).
  Link directo por persona: `.../equipo/?p=nombre` (por ejemplo `?p=yas`). Para actualizar nombres, líderes o tareas se edita solo `equipo/datos.js`; las 49 tareas son las mismas del Tablero de tareas del Drive.

## Estructura

- `index.html`: la home completa (HTML, CSS y JS sin dependencias ni CDN). Incluye el mapa del circuito como SVG en línea.
- `img/`: fotos en AVIF y WebP en varios tamaños, más `og.jpg` para redes.
- `fonts/`: Bricolage Grotesque, Literata e IBM Plex Mono en woff2, alojadas en el propio sitio (licencia SIL Open Font).
- `equipo/`, `CNAME`, `robots.txt`: sin cambios. El sitio sigue con `noindex`.

## Canales de contacto

Al final de `index.html` está el bloque `CONTACT`:

```js
var CONTACT = { instagram: "bandada.world", whatsapp: "", preinscripcion: "" };
```

Cuando exista el número de WhatsApp (formato internacional sin `+`) o el link del formulario de preinscripción, se completa ahí y los botones aparecen solos. La página no envía datos a ningún servidor: la solicitud de cuadrilla arma un resumen para copiar y mandar por mensaje.

## Procedencia de imágenes y datos

- Fotografías: ilustrativas, generadas con IA en Canva. No muestran trabajadores, productores ni clientes reales de Bandada, y la web las marca como tales.
- Mapa: Natural Earth (dominio público), proyectado y simplificado para la web.
- Cifras: cada dato lleva su fuente en la sección "Fuentes de cada dato". Lo que todavía no tiene fuente figura como DATO A VALIDAR.

Documento de trabajo elaborado con apoyo de IA (Claude, Anthropic) para investigación, diseño y código; el equipo valida los supuestos y toma las decisiones.
