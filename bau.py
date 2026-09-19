"""Baut index.html für die EDGE Unternehmenspräsentation.

Aufruf:  python3 bau.py
Folien, Texte, Logos und Collage werden hier gepflegt, nie direkt in index.html.
Gestaltung: Stamm aus cbl-ueberblick (Raumschwarz, Galaxie, Avenir Next, Schimmer).
Dramaturgie: von ROT und vielen ECKEN zu BLAU ohne Ecken, am Ende bleibt nur die Kante: die EDGE.
"""
import json
import math
import random
from pathlib import Path

ORDNER = Path(__file__).parent

# ----------------------------------------------------------------------------
# Inhalte
# ----------------------------------------------------------------------------

BAUSTELLEN = [
    ("fachkraefte", "Fachkräfte", "Gute Menschen werden schwerer zu gewinnen und teurer zu verlieren.", "Recruiting · Arbeitgeberattraktivität · Wissen"),
    ("kundengewinnung", "Kundengewinnung", "Aufmerksamkeit wird knapper. Akquise wird aufwendiger. Geschwindigkeit entscheidet.", "Leads · Vertrieb · Neukunden"),
    ("sichtbarkeit", "Sichtbarkeit", "Wer digital nicht relevant ist, findet immer weniger statt.", "KI statt Google · Social Media · Content"),
    ("kundenverstaendnis", "Kundenverständnis", "Märkte verändern sich schneller, als klassische Analysen mithalten können.", "Zielgruppen · Daten · Trends"),
    ("erreichbarkeit", "Erreichbarkeit", "Kunden erwarten Antworten sofort, unabhängig von Uhrzeit und Kanal.", "Telefon · Website · Support"),
    ("prozesse", "Prozesse &amp; KI", "Mitarbeiter nutzen KI längst. Prozesse, Systeme und Datenschutz hinken hinterher.", "Datenschutz · Digitale Souveränität · Automatisierung"),
]

# Referenzen, für die es noch keine Logodatei gibt: erscheinen als Schriftzug. Ziel ist eine leere Liste.
NUR_TEXT = ["Rotary Club", "Forum Ehrenamt", "TH Lübeck", "Energiecluster", "Stadtwerke Geesthacht", "Sprungtuch",
            "Change School Summit", "Digital für alle", "TQ", "K2Konzept", "HanseFriseur", "EGOH"]

# (name, kennung eines Trägerlogos oder None). Der Überflieger hat kein eigenes Logo, er läuft unter StartUp SH.
PREISE = [("Existenzgründerpreis", "lnpreis"), ("Gründerpreis der Sparkasse zu Lübeck", "sparkasse"), ("Social Hackathon", "socialhackathon"), ("Überflieger Wettbewerb", "startupsh")]

# Team: (name, rolle, bilddatei oder None)
SERVICE_KOPF = ("Eddie", "Head of AI-Services", "eddie.png")
SERVICE = [("Chakira", "AI Content Creatorin", "chakira.png"), ("Sohal", "AI Network Expertin", "sohal.png"), ("Jorge", "Data Scientist", "jorge.png")]
SOFTWARE_KOPF = ("Dom", "Head of AI-Software", "dom.png")
SOFTWARE = [("Mats", "Frontend Entwickler", "mats.png"), ("Saroj", "Backend Entwickler", "saroj.png"), ("Nadira", "AI und Software Engineer", "nadira.png")]

SERVICE_PUNKTE = ["Fachkräftesicherung (+2000 Bewerbungen allein in 2025)", "Kundengewinnung (wöchentliche Neukundengespräche)",
                  "Digitale Sichtbarkeit (Tausende Follower aufgebaut)", "Zielgruppenanalysen mit Millionen von Datenpunkten",
                  "Schulungen, Workshops und Webinare für Ihr Team", "Websites, Werbekampagnen, Content und vieles mehr"]
SOFTWARE_PUNKTE = ["KI aus Deutschland, für Deutschland", "Datenschutzkonforme KI", "Telefon-KI: rund um die Uhr erreichbar für Ihre Kunden",
                   "Website Chatbots für Ihre Kunden", "Schnittstellen zu all Ihren Tools", "KI-Workflows in Ihrer Firma implementieren"]

KONTAKT_MAIL = "emre@edge-digital.com"
KONTAKT_TEL = "0157 72461737"

# ----------------------------------------------------------------------------
# Formen als SVG. Fester Zufallsstart, damit jeder Bau gleich aussieht.
# ----------------------------------------------------------------------------

def wuerfel(cx, cy, s):
    """Isometrischer Drahtwürfel: Sechseck plus drei Kanten zur Mitte."""
    w, h = 0.866 * s, 0.5 * s
    aussen = [(cx, cy - s), (cx + w, cy - h), (cx + w, cy + h), (cx, cy + s), (cx - w, cy + h), (cx - w, cy - h)]
    pfad = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in aussen) + " Z"
    pfad += f" M{cx:.0f},{cy:.0f} L{cx:.0f},{cy + s:.0f} M{cx:.0f},{cy:.0f} L{cx + w:.0f},{cy - h:.0f} M{cx:.0f},{cy:.0f} L{cx - w:.0f},{cy - h:.0f}"
    return pfad


def kunst_rot():
    """Würfel und Pixel mit roten Neonkanten. Digitale Bedrohung, links bleibt Platz für die Schrift."""
    z = random.Random(7)
    lagen = [(1490, 520, 250), (1180, 250, 110), (1760, 190, 90), (1820, 820, 150), (1230, 860, 130), (960, 640, 60),
             (1610, 960, 70), (1010, 130, 50), (1380, 90, 40), (700, 960, 46), (380, 110, 38), (1900, 480, 60), (120, 900, 70), (860, 380, 34)]
    pfade = " ".join(wuerfel(*l) for l in lagen)
    pixel = []
    for _ in range(95):
        # Pixel häufen sich rechts und an den Rändern, wie ein Befall, der sich ausbreitet
        x = int(z.triangular(0, 1920, 1560)); y = int(z.uniform(0, 1080)); g = z.choice([8, 8, 12, 12, 16, 22, 30])
        x -= x % 16; y -= y % 16
        if 120 < x < 1000 and 330 < y < 760:
            continue
        pixel.append(f'<rect x="{x}" y="{y}" width="{g}" height="{g}" fill="#FF2D3D" opacity="{z.uniform(.12, .75):.2f}"/>')
    balken = "".join(f'<rect x="{int(z.uniform(900, 1700))}" y="{int(z.uniform(60, 1020))}" width="{int(z.uniform(80, 340))}" height="3" fill="#FF5A3C" opacity="{z.uniform(.25, .6):.2f}"/>' for _ in range(9))
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="\1" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="9"/></filter></defs>
  <g fill="none" stroke="#FF1F3D" stroke-width="7" stroke-linejoin="miter" filter="url(#gl-rot)" opacity=".75"><rect width="1920" height="1080" fill="none" stroke="none"/><path d="{pfade}"/></g>
  <g fill="rgba(255,31,61,.05)" stroke="#FF5468" stroke-width="2.5" stroke-linejoin="miter"><path d="{pfade}"/></g>
  {"".join(pixel)}{balken}
</svg>'''


def dreieck(cx, cy, r, dreh):
    """Gleichseitiges Dreieck, Spitze nach oben, um wenige Grad gedreht."""
    punkte = []
    for k in range(3):
        a = math.radians(-90 + 120 * k + dreh)
        punkte.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in punkte) + " Z"


def kunst_pink():
    """Weiche Dreiecke mit runden Ecken, die Spitze zeigt immer leicht nach oben."""
    lagen = [(1480, 560, 330, 8, .30), (1130, 300, 150, -14, .22), (1790, 250, 120, 19, .26), (1760, 880, 170, -9, .20),
             (1150, 850, 120, 12, .24), (880, 170, 70, -20, .20), (330, 930, 90, 16, .16), (150, 170, 60, -11, .16), (960, 960, 50, 6, .20)]
    teile = []
    for cx, cy, r, dreh, deck in lagen:
        d = dreieck(cx, cy, r, dreh); rund = max(14, r * .22)
        # Dicke Kontur in Füllfarbe mit runden Ecken ergibt die iPhone Ecke
        teile.append(f'<path d="{d}" fill="url(#vl-pink)" stroke="url(#vl-pink)" stroke-width="{rund:.0f}" stroke-linejoin="round" opacity="{deck}"/>')
    glut = "".join(f'<path d="{dreieck(cx, cy, r, dreh)}" fill="none" stroke="#FF6FBA" stroke-width="{max(14, r * .22) + 8:.0f}" stroke-linejoin="round" opacity=".28"/>' for cx, cy, r, dreh, _ in lagen[:5])
    kontur = "".join(f'<path d="{dreieck(cx, cy, r + max(14, r * .22) / 2, dreh)}" fill="none" stroke="#FFB3DC" stroke-width="2" stroke-linejoin="round" opacity=".55"/>' for cx, cy, r, dreh, _ in lagen)
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="\1" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="26"/></filter>
  <linearGradient id="vl-pink" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC2E4"/><stop offset="1" stop-color="#FF3D9A"/></linearGradient></defs>
  <g filter="url(#gl-pink)"><rect width="1920" height="1080" fill="none" stroke="none"/>{glut}</g>{"".join(teile)}{kontur}
</svg>'''


def kunst_lila():
    """Zwei Kreise, die sich überlappen, in zwei Lilatönen, die das Auge noch unterscheidet."""
    return '''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="\1" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="34"/></filter></defs>
  <g filter="url(#gl-lila)" opacity=".55"><rect width="1920" height="1080" fill="none" stroke="none"/><circle cx="1260" cy="560" r="330" fill="none" stroke="#7C3AED" stroke-width="16"/><circle cx="1570" cy="560" r="330" fill="none" stroke="#C77DFF" stroke-width="16"/></g>
  <g style="mix-blend-mode:screen"><circle cx="1260" cy="560" r="330" fill="#6D28D9" opacity=".42"/><circle cx="1570" cy="560" r="330" fill="#B565F2" opacity=".38"/></g>
  <circle cx="1260" cy="560" r="330" fill="none" stroke="#9F67FF" stroke-width="2.5" opacity=".9"/><circle cx="1570" cy="560" r="330" fill="none" stroke="#DDA8FF" stroke-width="2.5" opacity=".9"/>
</svg>'''


def kunst_dunkelblau():
    """Einzelne Kreise, jeder für sich. Sie kündigen die runden Portraits der nächsten Folie an."""
    lagen = [(1500, 540, 250, .34), (1130, 250, 96, .26), (1800, 190, 70, .30), (1790, 900, 110, .24), (1120, 880, 74, .28), (870, 140, 40, .22), (250, 930, 56, .18), (140, 160, 34, .18)]
    voll = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#vl-db)" opacity="{o}"/>' for x, y, r, o in lagen)
    rand = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#5B8CFF" stroke-width="2.5" opacity=".85"/>' for x, y, r, _ in lagen)
    glut = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#2F5BFF" stroke-width="14"/>' for x, y, r, _ in lagen[:5])
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="\1" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="22"/></filter>
  <radialGradient id="vl-db" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#3D6BFF"/><stop offset="1" stop-color="#0B1E8A"/></radialGradient></defs>
  <g filter="url(#gl-db)" opacity=".6"><rect width="1920" height="1080" fill="none" stroke="none"/>{glut}</g>{voll}{rand}
</svg>'''


def kunst_kante(kennung, stopps):
    """Die EDGE: eine leuchtende Kante am Rand eines dunklen Körpers. stopps = Farbverlauf entlang der Kante.

    Bewusst OHNE SVG Filter gebaut: Safari schneidet deren Schein an der Formgrenze ab.
    Ein senkrechter Farbverlauf wird durch einen kreisförmigen Verlauf maskiert, das rendert überall gleich.
    """
    # Oben und unten läuft die Kante ins Nichts aus, dazwischen liegen die Farben
    farben = ", ".join(f"{f} {18 + o * 64:.0f}%" for o, f in stopps)
    verlauf = f"linear-gradient(to bottom, transparent 3%, {farben}, transparent 97%)"
    mitte = "1640px 540px"
    schein = f"radial-gradient(circle at {mitte}, transparent 0, transparent 637px, rgba(0,0,0,.95) 639px, #000 641px, rgba(0,0,0,.62) 645px, rgba(0,0,0,.34) 664px, rgba(0,0,0,.16) 710px, rgba(0,0,0,.06) 790px, transparent 900px)"
    koerper = f"radial-gradient(circle at {mitte}, #030309 0, #030309 637px, transparent 640px)"
    return f'''<div class="kunst kante" aria-hidden="true">
  <div style="position:absolute;inset:0;background:{koerper};"></div>
  <div style="position:absolute;inset:0;background:{verlauf};-webkit-mask-image:{schein};mask-image:{schein};"></div>
</div>'''


# ----------------------------------------------------------------------------
# Bausteine
# ----------------------------------------------------------------------------

def kopf_kreis(name, rolle, bild, klasse, gross=False):
    """Rundes Portrait mit farbigem Ring. Ohne Bild erscheint ein markierter Platzhalter."""
    if bild:
        innen = f'<img src="assets/team/{bild}" alt="{name}" width="720" height="720">'
    else:
        innen = f'<span class="leer">{name[0]}</span>'
    zusatz = (" gross" if gross else "") + ("" if bild else " fehlt")
    return f'''<figure class="person {klasse}{zusatz}">
  <div class="rund">{innen}</div>
  <figcaption><b>{name}</b><span>{rolle}</span></figcaption>
</figure>'''


def team_seite(klasse, titel, kopf, leute, punkte):
    reihe = "".join(kopf_kreis(n, r, b, klasse) for n, r, b in leute)
    liste = "".join(f"<li>{p}</li>" for p in punkte)
    return f'''<div class="seite {klasse}">
  <p class="seiten-titel">{titel}</p>
  {kopf_kreis(*kopf, klasse, gross=True)}
  <div class="reihe">{reihe}</div>
  <ul class="punkte">{liste}</ul>
</div>'''


def bau():
    logos = json.loads((ORDNER / "assets/logos/referenzen.json").read_text(encoding="utf8"))
    gross = [l for l in logos if l["klasse"] == "g"]
    klein = [l for l in logos if l["klasse"] == "k"]
    logo_img = lambda l: f'<div><img src="assets/logos/ref-{l["id"]}.png" alt="{l["name"]}" width="{l["w"]}" height="{l["h"]}"></div>'

    # Schriftzüge nur für Referenzen, die noch kein Logo haben
    vorhanden = {l["name"] for l in logos}
    rest = [n for n in NUR_TEXT if n not in vorhanden]
    namen_zeile = f'<p class="namen">{" · ".join(rest)}</p>' if rest else ""
    preis_chips = "".join(
        f'<span class="preis"><b>{n}</b>' + (f'<img src="assets/logos/ref-{k}.png" alt="">' if k else "") + "</span>" for n, k in PREISE)
    # Spaltenzahl des kleinen Rasters wächst mit der Anzahl, damit immer alle Logos auf die Folie passen
    spalten = 10 if len(klein) <= 40 else (11 if len(klein) <= 44 else 12)
    karten = "".join(f'<article class="kachel-rot"><div><div class="kr-kopf"><img class="kr-icon" src="assets/icons/{i}.jpg" alt="" width="400" height="400"><p class="kr-titel">{t}</p><p class="kr-satz">{s}</p></div><p class="kr-tags">{g}</p></div></article>' for i, t, s, g in BAUSTELLEN)

    kante_titel = kunst_kante("titel", [(0, "#FF1F3D"), (.3, "#FF4FA3"), (.55, "#A855F7"), (.78, "#2F5BFF"), (1, "#7FD4FF")])
    kante_ende = kunst_kante("ende", [(0, "#A8E4FF"), (.5, "#7FD4FF"), (1, "#4FC3FF")])

    folien = f'''
<!-- ============ 1: DECKBLATT ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  {kante_titel}
  <div class="slide" style="justify-content:center;">
    <img class="titel-logo" src="assets/logos/edge-logo-white.png" alt="EDGE Digital">
    <p class="label" style="margin-top:44px;">Künstliche Intelligenz. Echte Wirkung.</p>
    <aside class="notes">Deckblatt. Die Kante rechts trägt schon alle Farben des Vortrags: von Rot über Pink und Lila bis Blau.</aside>
  </div>
</section>

<!-- ============ 2: ROT · KI VERÄNDERT ALLES ============ -->
<section class="f-rot" data-chrome="aus" data-stimmung="rot">
  {kunst_rot()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt">KI verändert<br><span class="schimmer">alles…</span></h2>
    <aside class="notes">Pause nach dem Satz. Das Bild arbeitet: Würfel, Pixel, rote Kanten. Stress, Bruch, Risiko.</aside>
  </div>
</section>

<!-- ============ 3: ROT · SECHS BAUSTELLEN ============ -->
<section class="f-rot" data-stimmung="rot">
  <div class="slide">
    <p class="label">Was Unternehmen gerade spüren</p>
    <h2 class="headline" style="margin-top:14px;">Der Druck kommt von <span class="schimmer">überall.</span></h2>
    <div class="raster-rot">{karten}</div>
    <aside class="notes">Sechs Baustellen, alle gleichzeitig. Nicht vorlesen: zwei herausgreifen, die zum Publikum passen.</aside>
  </div>
</section>

<!-- ============ 4: PINK · INS POSITIVE ============ -->
<section class="f-pink" data-chrome="aus" data-stimmung="pink">
  {kunst_pink()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt">…manchmal auch<br>ins <span class="schimmer">Positive…</span></h2>
    <aside class="notes">Stimmungswechsel. Die Ecken werden weich, die Spitzen zeigen nach oben.</aside>
  </div>
</section>

<!-- ============ 5: PINK · COLLAGE ============ -->
<section class="f-pink" data-chrome="aus" data-stimmung="pink">
  <!-- Eine gewachsene Collage wie in der IHK Kneipentalk Keynote: randlos, überlappend. Das Bild entsteht in werkzeuge/collage.py -->
  <img class="collage" src="assets/collage/collage.jpg" alt="EDGE unterwegs: Vorträge, Preise, Kunden, Team" width="2560" height="1440">
  <aside class="notes">Collage. Kurz stehen lassen, zwei Geschichten erzählen: Günther in der Mitte, die Urkunde unten links.</aside>
</section>

<!-- ============ 6: LILA · PARTNER UND KUNDEN ============ -->
<section class="f-lila" data-chrome="aus" data-stimmung="lila">
  {kunst_lila()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt">…sagen zahlreiche<br><span class="schimmer">Partner &amp; Kunden…</span></h2>
    <aside class="notes">Zwei Kreise, die sich überlappen: Partnerschaft.</aside>
  </div>
</section>

<!-- ============ 7: LILA · REFERENZEN ============ -->
<section class="f-lila" data-stimmung="lila">
  <div class="slide wand">
    <div class="logos gross">{"".join(logo_img(l) for l in gross)}</div>
    <hr class="trenner">
    <div class="logos klein" style="--spalten:{spalten};">{"".join(logo_img(l) for l in klein)}</div>
    {namen_zeile}
    <div class="preise"><span class="label">Preise &amp; Nominierungen</span><div class="preis-reihe">{preis_chips}</div></div>
    <aside class="notes">Nichts vorlesen. Die Menge wirkt. Einen Namen nennen, den das Publikum kennt.</aside>
  </div>
</section>

<!-- ============ 8: DUNKELBLAU · ZUSAMMENARBEIT ============ -->
<section class="f-dblau" data-chrome="aus" data-stimmung="dblau">
  {kunst_dunkelblau()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt">…die mit uns<br><span class="schimmer">zusammenarbeiten…</span></h2>
    <aside class="notes">Die einzelnen Kreise werden auf der nächsten Folie zu Gesichtern.</aside>
  </div>
</section>

<!-- ============ 9: TEAM ============ -->
<section data-stimmung="neutral">
  <div class="slide team">
    {team_seite("service", "„KI &amp; Daten für Ihre Firma nutzen“", SERVICE_KOPF, SERVICE, SERVICE_PUNKTE)}
    <div class="mitte">
      {kopf_kreis("Emre", "Geschäftsführer", "emre.png", "gf", gross=True)}
      <div class="gag">
        {kopf_kreis("Donald", "Head of Sales", "sales.png", "fremd")}
        <p class="gag-text"><b>Unser bester Mann im Vertrieb.</b><br>Er macht Ihnen das Leben schwer.<br>Wir machen es Ihnen leicht.</p>
      </div>
    </div>
    {team_seite("software", "„KI in Ihrer Firma implementieren“", SOFTWARE_KOPF, SOFTWARE, SOFTWARE_PUNKTE)}
    <aside class="notes">Links Service mit Eddie, rechts Software mit Dom, in der Mitte Emre. Der Gag in der Mitte kommt zuletzt.</aside>
  </div>
</section>

<!-- ============ 10: HELLBLAU · ENDE ============ -->
<section class="f-hblau" data-chrome="aus" data-stimmung="hblau">
  {kante_ende}
  <div class="slide ende">
    <h2 class="hero gesetzt">…so wie bald<br>auch <span class="schimmer">Sie.</span></h2>
    <p class="lead">Wir sind bereit, wenn Sie es sind: um mit Ihnen gemeinsam an die EDGE des Möglichen zu gehen.</p>
    <div class="kontakt"><img src="assets/logos/edge-logo-white.png" alt="EDGE Digital"><p>{KONTAKT_MAIL}<br>{KONTAKT_TEL}</p></div>
    <aside class="notes">Alle Ecken sind weg. Übrig bleibt nur die Kante: die EDGE.</aside>
  </div>
</section>
'''
    html = (ORDNER / "stamm.html").read_text(encoding="utf8").replace("<!--FOLIEN-->", folien)
    (ORDNER / "index.html").write_text(html, encoding="utf8")
    print("index.html gebaut:", len(html) // 1024, "KB,", len(gross), "große und", len(klein), "kleine Logos")


if __name__ == "__main__":
    bau()
