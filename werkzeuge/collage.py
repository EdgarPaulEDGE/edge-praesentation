"""Baut assets/collage/collage.jpg: die gewachsene Collage aus der IHK Kneipentalk Keynote als Basis,
neue Fotos werden randlos darübergesetzt.

Aufruf:  python3 werkzeuge/collage.py
Neues Foto ergänzen: Datei nach werkzeuge/collage/neu/ legen und unten eine Zeile in NEU eintragen.
Koordinaten sind Anteile der Collage (0 bis 1): links, oben, rechts, unten. Fokus = welcher Höhenanteil des Fotos im Bild bleibt.
Tipp: Ankerbilder (Günther Mitte, Urkunde unten links, Handschlag unten rechts) nicht überdecken.
"""
from pathlib import Path
from PIL import Image, ImageOps

HIER = Path(__file__).resolve().parent / "collage"
ZIEL = HIER.parent.parent / "assets/collage/collage.jpg"

NEU = [
    ("18.jpg", .000, .000, .180, .212, .40),   # EDGE über Lübeck
    ("17.jpg", .810, .000, 1.00, .185, .45),   # IHK Kneipentalk
    ("15.jpg", .097, .508, .192, .690, .30),   # Forum Ehrenamt am Pult
    ("12.jpg", .598, .490, .800, .680, .45),   # Vortrag vor vollem Saal
    ("21.jpg", .000, .550, .097, .690, .55),   # Lübeck.Lokal auf dem Dach
    ("19.jpg", .200, .888, .340, 1.00, .60),   # Team vor dem Rathaus
]

basis = Image.open(HIER / "basis.png").convert("RGB"); W, H = basis.size
for datei, x0, y0, x1, y1, fokus in NEU:
    kasten = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    foto = ImageOps.fit(Image.open(HIER / "neu" / datei).convert("RGB"), (kasten[2] - kasten[0], kasten[3] - kasten[1]), Image.LANCZOS, centering=(.5, fokus))
    basis.paste(foto, kasten[:2])
ImageOps.fit(basis, (2560, 1440), Image.LANCZOS).save(ZIEL, quality=86, optimize=True)
print("gebaut:", ZIEL)
