# EDGE Digital · Unternehmenspräsentation

Reveal.js Deck, 10 Folien, 1920 x 1080. Gestaltung aus dem Stamm `cbl-ueberblick`:
Raumschwarz, Galaxie, Avenir Next, Schimmer Verlauf.

**Dramaturgie:** von ROT und vielen Ecken (Würfel, Pixel) über PINK (weiche Dreiecke),
LILA (zwei Kreise) und DUNKELBLAU (einzelne Kreise) zu HELLBLAU: am Ende bleibt nur
die Kante, die EDGE. Das Deckblatt zeigt diese Kante schon mit allen Farben des Wegs.

## Ändern

Folien, Texte, Team, Collage und Preise stehen in `bau.py`, der Stil in `stamm.html`.
**Nie `index.html` direkt ändern**, danach immer:

```bash
python3 bau.py
```

## Lokal ansehen

```bash
python3 -m http.server 8791
```

Dann http://localhost:8791 öffnen. Tasten: Pfeile blättern, `F` Vollbild, `S` Redneransicht,
`O` Übersicht. `?nofrag` an die Adresse hängen für Standbilder und PDF Export.

## Offene Platzhalter

- Collage: zwei Felder für neue LinkedIn Motive. Bild nach `assets/collage/` legen und in
  `KACHELN` den Dateinamen statt `None` eintragen (2 x 1 Feld = 640 x 360 Pixel).
- Kontaktadresse und Preisliste prüfen (`KONTAKT_MAIL`, `PREISE`).

## Ordner

- `Team PNGs transparent/`: freigestellte Mitarbeiterfotos in voller Auflösung.
- `assets/logos/ref-*.png`: alle Referenzlogos als weiße Fassung für dunklen Grund.
