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

# Zweite Runde: Fotos von LinkedIn (Edgar und Emre). Angaben hier in Pixeln auf einer 1920 x 1080 Folie,
# das ist beim Platzieren anschaulicher. (datei, links, oben, rechts, unten, fokus)
LINKEDIN = [
    ("li-guenther-vfb.jpg",     1383, 392, 1622, 598, .40),   # Günther mit Emre im VfB Stadion, bewusst groß
    ("li-vfb-gruppe.jpg",       1370, 228, 1572, 392, .45),
    ("li-vfb-stadion.jpg",      1540, 598, 1740, 736, .50),
    ("li-vfb-trikot.jpg",        975, 745, 1146, 900, .35),
    ("li-lachclash-gruppe.jpg",  290, 250,  526, 393, .50),
    ("li-lachclash-duo.jpg",     526, 280,  612, 396, .55),
    ("li-moin.jpg",              590, 598,  832, 717, .62),
    ("li-roboter-gruppe.jpg",    632, 742,  892, 861, .42),
    ("li-it4b.jpg",             1045, 520, 1147, 652, .45),
    ("li-emre-redner.jpg",       900, 798,  976, 900, .35),
    ("li-fussball-team.jpg",     950,   0, 1150, 130, .50),
    ("li-fussball-bild.jpg",       0, 230,  170, 380, .45),
    ("li-anzug-trio.jpg",        160, 380,  376, 546, .28),
    ("li-workshop-selfie.jpg",   960, 130, 1150, 246, .72),
]

basis = Image.open(HIER / "basis.png").convert("RGB"); W, H = basis.size
for datei, x0, y0, x1, y1, fokus in NEU:
    kasten = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    foto = ImageOps.fit(Image.open(HIER / "neu" / datei).convert("RGB"), (kasten[2] - kasten[0], kasten[3] - kasten[1]), Image.LANCZOS, centering=(.5, fokus))
    basis.paste(foto, kasten[:2])
for datei, l, o, r, u, fokus in LINKEDIN:
    kasten = (int(l / 1920 * W), int(o / 1080 * H), int(r / 1920 * W), int(u / 1080 * H))
    foto = ImageOps.fit(Image.open(HIER / "neu" / datei).convert("RGB"), (kasten[2] - kasten[0], kasten[3] - kasten[1]), Image.LANCZOS, centering=(.5, fokus))
    basis.paste(foto, kasten[:2])
ImageOps.fit(basis, (2560, 1440), Image.LANCZOS).save(ZIEL, quality=86, optimize=True)
print("gebaut:", ZIEL)
