# EDGE Digital · Unternehmenspräsentation

Reveal.js Deck, 10 Folien, 1920 x 1080. Gestaltung aus dem Stamm `cbl-ueberblick`:
Raumschwarz, Galaxie, Avenir Next, Schimmer Verlauf.

**Dramaturgie:** von ROT und vielen Ecken (Würfel, Pixel) über PINK (weiche Dreiecke),
LILA (zwei Kreise) und DUNKELBLAU (einzelne Kreise) zu HELLBLAU: am Ende bleibt nur
die Kante, die EDGE. Das Deckblatt zeigt diese Kante schon mit allen Farben des Wegs.

## Live

**https://bereit.edge-digital.ai/**
GitHub Pages aus `main`, Repo `EdgarPaulEDGE/edge-praesentation`. Jeder Push geht nach etwa einer Minute live.
DNS: CNAME `bereit` auf `edgarpauledge.github.io` bei Wix. Suchmaschinen sind per `noindex, nofollow` ausgesperrt.

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

- Collage: entsteht mit `python3 werkzeuge/collage.py` aus der Keynote Collage plus neuen Fotos. Anleitung steht oben im Skript.
- Kontaktadresse und Preisliste prüfen (`KONTAKT_MAIL`, `PREISE`).

## Ordner

- `Team PNGs transparent/`: freigestellte Mitarbeiterfotos in voller Auflösung.
- `assets/logos/ref-*.png`: alle Referenzlogos als weiße Fassung für dunklen Grund.

## Prüfen in Safari

Chrome und Safari rendern SVG Filter unterschiedlich. Vor jedem Push beide prüfen. `werkzeuge/webkitshot.swift`
fotografiert eine Folie mit WebKit, also Safaris Engine, ohne Fenster:

```bash
swiftc -O werkzeuge/webkitshot.swift -o /tmp/webkitshot && /tmp/webkitshot "http://localhost:8791/?nofrag#/0" folie1.png
```

Die leuchtende Kante auf Deckblatt und Schlussfolie ist deshalb bewusst reines CSS (Verlauf plus Maske) und kein SVG Filter.
`werkzeuge/freistellen.swift` stellt Fotos lokal frei, `werkzeuge/gesicht.swift` liefert den Gesichtsrahmen für mittige Zuschnitte.
