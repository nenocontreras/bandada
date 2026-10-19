"""Exporta las fotos del sitio a AVIF y WebP con su procedencia.

Uso: python -I tools/fotos.py <carpeta con los JPG exportados de Canva>

Cada archivo de salida lleva al lado un .json con el prompt exacto de
generación (o el origen) y la fecha, para que se sepa de dónde sale.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageEnhance

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'img' / 'foto'

COMUN = ('Imagen ilustrativa generada con IA en Canva (generate-image) para Bandada, '
         'octubre de 2026. Muestra personas adultas y no muestra trabajadores, productores '
         'ni clientes reales. Exportada desde Canva y convertida con tools/fotos.py. Prompt: ')

PROMPTS = {
    'hero-cuadrilla': (
        'Documentary photograph, wide cinematic landscape. A harvest crew of six adult seasonal farm '
        'workers walking together along a dirt path between long rows of lemon trees in Tucumán, '
        'northern Argentina, at golden hour. Low warm sun behind them, long shadows, dust in the light, '
        'mountains (Sierras del Aconquija) softly hazy in the distance. Workers wear practical work '
        'clothes, wide-brim hats and caps, some carry empty harvest bags over the shoulder; seen from '
        'behind and three-quarter view, faces not prominent. Natural, dignified, candid, shot on 35mm, '
        'shallow depth of field, rich but natural color with warm orange highlights and deep blue '
        'shadows. Large calm sky area in the upper third. No text, no logos, no children.'),
    'trabajadora': (
        'Documentary portrait photograph. An adult seasonal farm worker, a woman around 35, standing in '
        'a blueberry field in northern Argentina at early morning, holding a small harvest tray, looking '
        'calmly toward the horizon, soft side light, mist over the rows behind her. Practical work '
        'clothes, cap, light jacket. Natural, dignified, candid, 50mm lens, shallow depth of field, '
        'natural color with warm highlights and cool blue shadows. Empty soft background on the upper '
        'part. No text, no logos, no children.'),
    'productor': (
        'Documentary photograph. An adult farm producer, a man around 50, standing at the edge of an '
        'olive grove in Catamarca, Argentina, in the morning, reviewing a harvest plan on a tablet, '
        'talking with a crew leader wearing a work vest; in the soft-focus background a harvest crew is '
        'getting ready next to the trees. Arid mountains in the distance, clear sky. Natural, '
        'professional, candid, 50mm lens, shallow depth of field, natural color with warm sunlight and '
        'deep blue shadows. No readable screen content, no text, no logos, no children.'),
    'aerea-maiz': (
        'Aerial drone photograph looking straight down at the Argentine countryside in the Pampa near '
        'Pergamino at late afternoon: long parallel rows of tall corn fields, a dirt road crossing '
        'diagonally, a small group of adult workers walking along the edge of the field casting long '
        'shadows. Graphic geometric composition, warm golden light, rich greens and ochres, subtle blue '
        'shadows. Realistic, high detail. No text, no logos.'),
    'alojamiento': (
        'Documentary photograph. Clean, simple worker accommodation room in a rural farm in northern '
        'Argentina: four single beds with folded blankets, lockers, a window with morning light, a table '
        'with a water jug; an adult inspector in a work vest checking a list on a clipboard in the '
        'doorway, seen from behind. Calm, orderly, natural light, realistic, 35mm, natural color with '
        'warm light and blue shadows. No text, no logos, no children.'),
}

# nombre: (archivo de origen, recorte relativo (x0, y0, x1, y1) o None, anchos)
PIEZAS = {
    'hero-cuadrilla': ('hero-cuadrilla.jpg', None, [1680, 1200, 800]),
    'hero-cuadrilla-m': ('hero-cuadrilla.jpg', (0.29, 0.0, 0.71, 1.0), [708, 480]),
    'trabajadora': ('trabajadora.jpg', None, [1136, 720]),
    'productor': ('productor.jpg', None, [1136, 720]),
    'aerea-maiz': ('aerea-maiz.jpg', None, [1680, 1000]),
    'alojamiento': ('alojamiento.jpg', None, [1200, 720]),
    'limonar': ('limon.jpg', None, [1600, 960]),
}

# piezas sin prompt conservado: se declara el origen
ORIGENES = {
    'limonar': ('ORIGEN (no es un prompt de generación; el prompt original de Canva no se conserva): '
                'foto de la cosecha de limón en Tucumán generada con IA en Canva para Bandada el '
                '16/10/2026, con personas adultas; imagen ilustrativa que no muestra trabajadores '
                'reales. Exportada desde Canva y convertida con tools/fotos.py.'),
}


def main(origen: Path) -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    ahora = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    for nombre, (archivo, recorte, anchos) in PIEZAS.items():
        im = Image.open(origen / archivo).convert('RGB')
        if recorte:
            w, h = im.size
            im = im.crop((round(recorte[0] * w), round(recorte[1] * h), round(recorte[2] * w), round(recorte[3] * h)))
        # gradación común muy leve: un poco más de contraste y algo menos de saturación
        im = ImageEnhance.Contrast(im).enhance(1.04)
        im = ImageEnhance.Color(im).enhance(0.94)
        base = nombre.removesuffix('-m')
        for ancho in anchos:
            alto = round(im.height * ancho / im.width)
            r = im.resize((ancho, alto), Image.LANCZOS) if ancho != im.width else im
            for ext, opts in (('avif', {'quality': 58}), ('webp', {'quality': 80, 'method': 6})):
                destino = SALIDA / f'{nombre}-{ancho}.{ext}'
                r.save(destino, **opts)
                texto = ORIGENES.get(base) or (COMUN + PROMPTS[base] + (' Recorte vertical para celular.' if recorte else ''))
                procedencia = {'prompt': texto, 'createdAt': ahora}
                destino.with_name(destino.name + '.json').write_text(
                    json.dumps(procedencia, ensure_ascii=False, indent=2), encoding='utf-8')
                print(destino.relative_to(RAIZ), r.size, destino.stat().st_size // 1024, 'KB')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
