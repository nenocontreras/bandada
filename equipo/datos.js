// =====================================================================
//  DATOS DE LA PÁGINA DEL EQUIPO · Bandada · Mundial de Estudiantes 2026
//  Es el único archivo que hay que tocar para actualizar la página.
//  Las tareas son las mismas 49 del "Tablero de tareas" del Drive.
//  - Para cambiar un nombre, editá solo el texto de "nombre".
//  - Cuando se elijan los líderes (tarea T1), poné el id de cada uno en LIDERES.
//  - En TAREAS, "@id" es una persona; cualquier otro texto es un grupo o un área.
// =====================================================================
window.BANDADA = {
  PERSONAS: [
    {id: 'nacho', nombre: "Nacho", area: 'fin'},
    {id: 'tadeo', nombre: "Tadeo", area: 'fin'},
    {id: 'carmina', nombre: "Carmina", area: 'fin'},
    {id: 'lujan', nombre: "Luján", area: 'fin'},
    {id: 'martin', nombre: "Martín", area: 'ide'},
    {id: 'luji', nombre: "Luji", area: 'ide'},
    {id: 'karlina', nombre: "Karlina", area: 'ide'},
    {id: 'luisana', nombre: "Luisana", area: 'rrhh'},
    {id: 'gabriela', nombre: "Gabriela", area: 'rrhh'},
    {id: 'sami', nombre: "Sami", area: 'rrhh'},
    {id: 'coordinacion', nombre: "Coordinador/a del Drive", area: 'mkt'},
    {id: 'yas', nombre: "Yas", area: 'mkt'},
    {id: 'sofi', nombre: "Sofi", area: 'pyl'},
    {id: 'dana', nombre: "Dana", area: 'pyl'},
  ],

  // id de quien lidera cada área ('' mientras no esté definido)
  LIDERES: {fin: '', ide: '', rrhh: '', mkt: '', pyl: ''},
  COORDINACION: '',  // id de quien hace la coordinación general

  AREAS: [
    {id: 'fin', nombre: "Finanzas", corto: "Finanzas", color: 'sea', carpeta: 'https://drive.google.com/drive/folders/1EZwIwqmHZw17NA_po73aLrwlmN4RKyOX'},
    {id: 'ide', nombre: "Identidad de la empresa", corto: "Identidad", color: 'berry', carpeta: 'https://drive.google.com/drive/folders/1zWAJ32bd6WtVO7gs7-ZOYWxxgn_LzXvS'},
    {id: 'rrhh', nombre: "Recursos Humanos", corto: "RRHH", color: 'leaf', carpeta: 'https://drive.google.com/drive/folders/1S6bcEjyHC3wyuwVFhtr3gGmFbjptJfDb'},
    {id: 'mkt', nombre: "Marketing", corto: "Marketing", color: 'soil', carpeta: 'https://drive.google.com/drive/folders/107Jbr5XwICsOnSerp5xrn6QR4eCqE28v'},
    {id: 'pyl', nombre: "Procesos y Logística", corto: "Procesos y Logística", color: 'citrus', carpeta: 'https://drive.google.com/drive/folders/1uxLBtq4kH08RrVGxVqkn_sA7Jz5XCe97'},
  ],

  LINKS: {
    carpeta: {titulo: "Carpeta del equipo", url: 'https://drive.google.com/drive/folders/1T7hvv7WYqe4Jxfvy5jScK6d89cAjr8f2'},
    tablero: {titulo: "Tablero de tareas", url: 'https://docs.google.com/spreadsheets/d/1qULSPfEFXhDikNwTnFyWFeCqEq9gm-jFMICqFp6jxfU/edit'},
    ficha: {titulo: "Ficha maestra para tu IA", url: 'https://docs.google.com/document/d/1U5A6d884wE6DCQEh3T1cVItVoTz0LI3h7uX7XPOqONA/edit'},
    instructivo: {titulo: "Instructivo para integrantes", url: 'https://docs.google.com/document/d/1C2jXY5GNkWKhfXzaLyUrn2ZJWwNmYXJjJH6A4sXd40o/edit'},
    supuestos: {titulo: "Supuestos maestros: las cifras", url: 'https://docs.google.com/spreadsheets/d/14-4kqq_2l-62miUsihFEVZf5K9pnHIoxGfjaN905PrU/edit'},
    registros: {titulo: "Registros: decisiones y uso de IA", url: 'https://docs.google.com/spreadsheets/d/1nCVigvUdeyY1rcSIbPAeVVPBrO2PHMIQaKJE_8Xpf1M/edit'},
    entrevistas: {titulo: "Carpeta de entrevistas", url: 'https://drive.google.com/drive/folders/1PI9MmeEg8s8sYOZobFFGdaciZRRR0dph'},
    entrega: {titulo: "Entrega Etapa 2: solo versiones finales", url: 'https://drive.google.com/drive/folders/1pcdYn_tiIxyyzXiTQ-VkgogeUnhPKmXz'},
  },

  HITOS: [
    {fecha: '2026-10-05', titulo: "Kickoff", detalle: "Líderes elegidos, equipo completo con datos, Drive y tablero en uso."},
    {fecha: '2026-10-10', titulo: "Hito 1", detalle: "Cliente validado: canvas v1, identidad (logo y paleta), cuentas creadas y 7 o más entrevistas hechas."},
    {fecha: '2026-10-17', titulo: "Hito 2", detalle: "Diseño v1: finanzas v1, web online, organigrama, plan de RRHH v1, calendario de cosechas y costos, 4 publicaciones."},
    {fecha: '2026-10-24', titulo: "Hito 3", detalle: "Congelamiento: todos los entregables completos, finanzas v2 y resultado del piloto o cartas de intención."},
    {fecha: '2026-10-28', titulo: "Entrega", detalle: "Los 10 entregables subidos antes de las 18:00, con fuentes APA y declaración de IA."},
    {fecha: '2026-11-05', titulo: "Mendoza", detalle: "Defensa final: 15 minutos de exposición y 10 de preguntas."},
  ],
  ENTREGA: '2026-10-28',
  DEFENSA: '2026-11-05',

  // id, área, tarea, responsable, apoyo, revisa, entregable, inicio, vence
  TAREAS: [
    ["T1", "tra", "Elegir líder de cada área y coordinador/a general", "Todas las áreas", "", "Capitán docente", "Organización interna", "2026-10-05", "2026-10-06"],
    ["T2", "tra", "Consulta escrita al CLAM: composición del equipo, roles de los 5 titulares y fecha de entrega (28 o 30/10)", "Coordinación general", "Mesa de líderes", "Capitán docente", "Cumplimiento del reglamento", "2026-10-05", "2026-10-07"],
    ["T3", "tra", "Revisiones de hito con todo el equipo (sáb 10, 17 y 24/10)", "Mesa de líderes", "", "Capitán docente", "Organización interna", "2026-10-10", "2026-10-24"],
    ["T4", "tra", "Control cruzado de cifras entre todos los entregables", "Finanzas", "Mesa de líderes", "Capitán docente", "Todos", "2026-10-26", "2026-10-27"],
    ["T5", "tra", "Fuentes APA y declaración de IA en cada entregable (Arts. 24 y 28)", "Cada área", "Coordinación general", "Mesa de líderes", "Todos", "2026-10-26", "2026-10-27"],
    ["T6", "tra", "Envío de los entregables de la Etapa 2", "Coordinación general", "", "Capitán docente", "Todos", "2026-10-28", "2026-10-28"],
    ["T7", "tra", "Banco de 30 preguntas difíciles con respuestas (cada área aporta 6)", "Coordinación general", "Todas las áreas", "Capitán docente", "Defensa final", "2026-10-22", "2026-10-31"],
    ["T8", "tra", "Ensayos generales con jurado simulado (31/10, 2/11 y 4/11)", "Mesa de líderes", "Todas las áreas", "Capitán docente", "Defensa final", "2026-10-31", "2026-11-04"],
    ["T9", "tra", "Viaje a Mendoza: pasajes, alojamiento y acreditaciones", "Coordinación general", "Procesos y Logística", "Capitán docente", "Defensa final", "2026-10-29", "2026-11-03"],
    ["F1", "fin", "Mantener la planilla Supuestos maestros y validar cada dato con su fuente", "@nacho", "@carmina", "Marketing", "9. Finanzas", "2026-10-05", "2026-10-27"],
    ["F2", "fin", "Inversión inicial detallada", "@tadeo", "", "Procesos y Logística", "9. Finanzas", "2026-10-06", "2026-10-12"],
    ["F3", "fin", "Estructura de costos fijos y variables (incluye costos por tramo de traslado y alojamiento)", "@carmina", "@sofi", "Procesos y Logística", "9. Finanzas", "2026-10-08", "2026-10-15"],
    ["F4", "fin", "Punto de equilibrio", "@lujan", "", "Marketing", "9. Finanzas", "2026-10-12", "2026-10-17"],
    ["F5", "fin", "Flujo de fondos y proyección a 3 años: v1 17/10, v2 24/10", "@nacho", "@tadeo", "Mesa de líderes", "9. Finanzas", "2026-10-10", "2026-10-24"],
    ["F6", "fin", "Unit economics: LTV/CAC del productor y del trabajador", "@lujan", "", "Marketing", "Instructivo · Unit economics", "2026-10-14", "2026-10-20"],
    ["F7", "fin", "TAM, SAM y SOM con fuentes", "@tadeo", "", "Marketing", "Instructivo · TAM/SAM/SOM", "2026-10-12", "2026-10-16"],
    ["F8", "fin", "Análisis de sensibilidad: jornal, fee y retención", "@carmina", "", "Mesa de líderes", "9. Finanzas", "2026-10-19", "2026-10-23"],
    ["F9", "fin", "Impacto económico (parte del entregable 10)", "@lujan", "", "RRHH", "10. Impacto social", "2026-10-19", "2026-10-24"],
    ["F10", "fin", "Plan de crecimiento (junto con Procesos y Logística)", "@tadeo", "@dana", "RRHH", "5. Organización empresarial", "2026-10-19", "2026-10-23"],
    ["I1", "ide", "Logo, slogan y manual básico de marca", "@martin", "@karlina", "Marketing", "2. Identidad empresarial", "2026-10-05", "2026-10-11"],
    ["I2", "ide", "Misión, visión y valores", "@luji", "", "RRHH", "2. Identidad empresarial", "2026-10-06", "2026-10-11"],
    ["I3", "ide", "Plantillas de marca en Canva: documentos, slides y posts", "@karlina", "", "Marketing", "2. Identidad empresarial", "2026-10-08", "2026-10-13"],
    ["I4", "ide", "Web \"Reservá tu cuadrilla\": servicios, contacto, descripción y proceso de compra", "@martin", "@yas", "Procesos y Logística", "4. Comercio electrónico", "2026-10-12", "2026-10-20"],
    ["I5", "ide", "Diseño de las 12 publicaciones y las 4 historias destacadas", "@karlina", "@luji", "Marketing", "3. Marketing digital", "2026-10-12", "2026-10-26"],
    ["I6", "ide", "4 reels, incluido el video narrado en formato 9:16", "@luji", "", "Marketing", "3. Marketing digital", "2026-10-12", "2026-10-26"],
    ["I7", "ide", "Diseño del pitch deck de 10 a 12 slides", "@martin", "@coordinacion", "Mesa de líderes", "Defensa final", "2026-10-21", "2026-10-27"],
    ["H1", "rrhh", "Entrevistas a trabajadores y cabecillas de Santiago del Estero (8 de las 15)", "@gabriela", "@sami", "Marketing", "Instructivo · Customer discovery", "2026-10-05", "2026-10-14"],
    ["H2", "rrhh", "Consulta con abogado laboralista: Leyes 26.727, 27.742, 27.802 y decreto 514", "@luisana", "", "Mesa de líderes", "Riesgo legal", "2026-10-06", "2026-10-16"],
    ["H3", "rrhh", "Organigrama, estructura organizacional y manual de funciones", "@sami", "", "Procesos y Logística", "5. Organización empresarial", "2026-10-08", "2026-10-16"],
    ["H4", "rrhh", "Programa Jefe de Bandada: perfil, selección, incentivo y estrategia de liderazgo", "@gabriela", "", "Finanzas", "6. Recursos humanos", "2026-10-12", "2026-10-18"],
    ["H5", "rrhh", "Plan de RRHH: dotación inicial, plan de contratación, capacitación y evaluación de desempeño", "@luisana", "@sami", "Procesos y Logística", "6. Recursos humanos", "2026-10-12", "2026-10-22"],
    ["H6", "rrhh", "Cultura organizacional y política de contratación equitativa (OIT) con canal de reclamos", "@sami", "", "Identidad", "6. Recursos humanos", "2026-10-15", "2026-10-20"],
    ["H7", "rrhh", "Impacto social y ambiental; consolidar el entregable 10 con Finanzas", "@luisana", "@lujan", "Mesa de líderes", "10. Impacto social", "2026-10-19", "2026-10-25"],
    ["M1", "mkt", "Entrevistas a productores, empacadoras y exportadores (7 de las 15)", "@yas", "@coordinacion", "RRHH", "Instructivo · Customer discovery", "2026-10-05", "2026-10-14"],
    ["M2", "mkt", "Value Proposition Canvas por segmento", "@yas", "", "Finanzas", "Instructivo · VPC", "2026-10-08", "2026-10-11"],
    ["M3", "mkt", "Business Model Canvas y Lean Canvas", "@coordinacion", "", "Finanzas", "1. Modelo de negocios", "2026-10-08", "2026-10-13"],
    ["M4", "mkt", "Estrategia comercial y validación del precio (fee de 6% a 9%)", "@coordinacion", "@yas", "Finanzas", "1. Modelo de negocios", "2026-10-14", "2026-10-20"],
    ["M5", "mkt", "Crear Instagram, LinkedIn y Facebook, y el calendario de contenidos de 4 semanas", "@yas", "@karlina", "Identidad", "3. Marketing digital", "2026-10-08", "2026-10-12"],
    ["M6", "mkt", "Textos de las publicaciones y campaña de preinscripción de trabajadores (meta: 100)", "@yas", "@gabriela", "RRHH", "3. Marketing digital", "2026-10-12", "2026-10-25"],
    ["M7", "mkt", "Cartas de intención de productores (junto con Procesos y Logística)", "@coordinacion", "@sofi", "Mesa de líderes", "Tracción", "2026-10-19", "2026-10-25"],
    ["M8", "mkt", "Guion y contenido del pitch (diseño a cargo de Identidad)", "@coordinacion", "@martin", "Mesa de líderes", "Defensa final", "2026-10-21", "2026-10-27"],
    ["M9", "mkt", "Métricas de redes para mostrar tracción en el pitch", "@yas", "", "Mesa de líderes", "Defensa final", "2026-10-26", "2026-10-27"],
    ["P1", "pyl", "Calendario de cosechas de 12 meses validado con fuentes y 2 productores", "@sofi", "", "Marketing", "8. Logística", "2026-10-05", "2026-10-13"],
    ["P2", "pyl", "Flujograma general y cadena de valor", "@dana", "", "RRHH", "7. Procesos", "2026-10-08", "2026-10-16"],
    ["P3", "pyl", "Cadena de abastecimiento, distribución e inventario de jornadas", "@sofi", "", "Finanzas", "8. Logística", "2026-10-12", "2026-10-20"],
    ["P4", "pyl", "Service Blueprint del viaje de una cuadrilla", "@dana", "", "Identidad", "Instructivo · Service Blueprint", "2026-10-15", "2026-10-21"],
    ["P5", "pyl", "Tablero de 10 KPIs con fórmula y meta", "@dana", "@lujan", "Finanzas", "7. Procesos", "2026-10-16", "2026-10-21"],
    ["P6", "pyl", "Piloto: colocar 1 cuadrilla en el arándano de Tucumán o conseguir 3 cartas de intención", "@sofi", "@coordinacion", "Mesa de líderes", "Tracción", "2026-10-14", "2026-10-25"],
    ["P7", "pyl", "Plan de expansión regional al MERCOSUR con marco CAGE", "@dana", "@tadeo", "Marketing", "8. Logística", "2026-10-19", "2026-10-25"],
  ],
};
