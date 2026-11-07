"""Generates index.html, competenties/*.html and projects/*.html for the portfolio.

Edit COMPETENTIES, TAGS and PROJECTS below, then run:  python3 build.py
Generated pages are overwritten, so don't edit them by hand.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))

# Each competentie has numbered leerdoelen. Their codes ("1.1", "1.2", ...) are what projects refer to.
# Optional: "diagram" (image in images/ with alt and caption) shown below the leerdoelen.
COMPETENTIES = [
    {
        "number": "1",
        "slug": "digitale-expert",
        "name": "De digitale expert: onderzoeker & uitvoerder",
        "leerdoelen": [
            "Formuleert relevante digitale onderzoek- of ontwerpvragen binnen de gebouwde omgeving en kiest hiervoor passende methoden.",
            "Verzamelt, analyseert en interpreteert data kritisch om onderbouwde oplossingen te ontwikkelen.",
            "Integreert en prototypeert digitale tools/technieken in innovatieve oplossingen voor opgaven in de gebouwde omgeving.",
            "Reflecteert kritisch op het onderzoek en/of ontwerpproces en valideert de impact van “oplossingen” met stakeholders (opdrachtgever, adviseurs, medestudenten etc.).",
        ],
    },
    {
        "number": "2",
        "slug": "teamspeler",
        "name": "De teamspeler in digitale context",
        "leerdoelen": [
            "Werkt effectief samen in multidisciplinaire teams met behulp van digitale middelen & processen.",
            "Communiceert bevindingen en ontwerpkeuzes helder, visueel en doelgroepgericht om besluitvorming en overdracht te ondersteunen.",
            "Bouwt en onderhoudt een professioneel (online) netwerk en draagt actief bij aan kennisdeling binnen de vak-gemeenschap.",
        ],
    },
    {
        "number": "3",
        "slug": "zelfsturende-professional",
        "name": "De zelfsturende digitale professional",
        "leerdoelen": [
            "Stelt meetbare persoonlijke leerdoelen op en stuurt bij op basis van voortdurende kritisch reflectie.",
            "Toont een zelflerende houding in het eigen maken van zowel digitale vakbekwaamheid als softskills.",
            "Signaleert technologische innovaties en eigent zich zelfstandig nieuwe tools en werkwijzen toe om de professionele praktijk te versterken.",
        ],
    },
    {
        "number": "4",
        "slug": "professioneel-handelen",
        "name": "Professioneel handelen HBO",
        "leerdoelen": [
            "De student handelt professioneel. Zie onderstaand diagram, professioneel handelen HBO.",
        ],
        "diagram": {
            "image": None,  # e.g. "professioneel-handelen-hbo.png" in images/
            "alt": "Diagram professioneel handelen HBO",
            "caption": "Professioneel handelen HBO.",
        },
    },
]

# Tags shown on project cards and pages (the former themes). Projects refer to them by key.
TAGS = {
    "parametrisch": "Parametrisch ontwerpen",
    "arcgis": "ArcGIS",
    "fabricage": "Digitale fabricage",
    "python": "Python",
}

# The home-page timeline covers these months ("YYYY-MM", inclusive).
# Projects dated outside this range are left out of the timeline.
TIMELINE = {"start": "2026-09", "end": "2027-01"}

# Required per project: slug, title, leerdoelen (codes; the first one's competentie is the primary one),
#   tags (keys from TAGS), lead, role, date ("YYYY-MM", e.g. "2026-10"), tools.
# Optional: challenge, process, steps (list), result, image (file in images/ or URL), image_alt, caption.
# Optional fields that are left out get placeholder text (see CONTENT_DEFAULTS).
PROJECTS = [
    {
        "slug": "parametrische-gevel",
        "title": "Parametrische gevel",
        "leerdoelen": ["1.1", "1.3", "2.2"],
        "tags": ["parametrisch", "python"],
        "lead": "Een adaptief gevelsysteem waarvan de lamellen zich afstemmen op de zonnestand, ontworpen in Grasshopper en geoptimaliseerd met een Python-script.",
        "role": "Ontwerper", "date": "2026-11", "tools": "Rhino, Grasshopper, Ladybug, Python",
    },
    {
        "slug": "houten-paviljoen",
        "title": "Houten paviljoen",
        "leerdoelen": ["1.3", "1.4", "2.1"],
        "tags": ["parametrisch", "fabricage"],
        "lead": "Een paviljoen van gefreesde houten platen, parametrisch ontworpen en volledig digitaal geproduceerd.",
        "role": "Ontwerper & maker", "date": "2026-09", "tools": "Rhino, Grasshopper, CNC-frees",
    },
    {
        "slug": "hittestress-analyse",
        "title": "Hittestress-analyse",
        "leerdoelen": ["1.2", "2.2"],
        "tags": ["arcgis", "python"],
        "lead": "Een analyse van hittestress in een stadswijk, met aanbevelingen voor vergroening en materiaalgebruik.",
        "role": "Onderzoeker", "date": "2026-12", "tools": "ArcGIS Pro, Python (ArcPy)",
    },
    {
        "slug": "locatieanalyse-woningbouw",
        "title": "Locatieanalyse woningbouw",
        "leerdoelen": ["2.1", "1.2", "4.1"],
        "tags": ["arcgis"],
        "lead": "Een GIS-analyse om geschikte locaties voor nieuwe woningbouw te vinden op basis van bereikbaarheid, voorzieningen en ruimtelijke beperkingen.",
        "role": "Onderzoeker", "date": "2026-10", "tools": "ArcGIS Pro",
    },
    {
        "slug": "cnc-houtverbindingen",
        "title": "CNC-houtverbindingen",
        "leerdoelen": ["3.2", "1.3", "3.1"],
        "tags": ["fabricage"],
        "lead": "Een onderzoek naar demontabele houtverbindingen zonder lijm of metaal, getest met gefreesde prototypes.",
        "role": "Onderzoeker & maker", "date": "2026-10", "tools": "Rhino, Fusion 360, CNC-frees",
    },
    {
        "slug": "bim-automatisering",
        "title": "BIM-automatisering",
        "leerdoelen": ["3.3", "2.3", "4.1"],
        "tags": ["python"],
        "lead": "Een set Python-scripts die controles en hoeveelheden uit een BIM-model automatisch genereren.",
        "role": "Ontwikkelaar", "date": "2027-01", "tools": "Python, Revit, Dynamo",
    },
]

# Content of the standalone reflectie page (reflectie.html), written as a STAR-reflectie.
# Each step has a letter, a heading and a list of paragraphs (plain text, one string per paragraph).
REFLECTIE = {
    "title": "STAR-reflectie",
    "lead": "Een reflectie op mijn ontwikkeling als bouwkundige in een digitale context, over alle competenties en projecten heen, volgens de STAR-methode.",
    "sections": [
        {
            "letter": "S",
            "heading": "Situatie",
            "paragraphs": [
                "Beschrijf de context: in welke periode, opleiding of omgeving speelde dit zich af, en met wie werkte je samen?",
            ],
        },
        {
            "letter": "T",
            "heading": "Taak",
            "paragraphs": [
                "Wat was jouw taak of rol, en wat werd er van je verwacht? Welke leerdoelen wilde je in deze periode aantonen?",
            ],
        },
        {
            "letter": "A",
            "heading": "Actie",
            "paragraphs": [
                "Wat heb je concreet gedaan? Beschrijf je aanpak, de keuzes die je maakte en waarom, met verwijzingen naar je projecten.",
            ],
        },
        {
            "letter": "R",
            "heading": "Resultaat",
            "paragraphs": [
                "Wat was het resultaat van je acties? Welke leerdoelen heb je aangetoond, wat ging goed en wat zou je een volgende keer anders doen?",
            ],
        },
    ],
}

# Placeholder case-study text, used for any of these fields a project leaves out.
CONTENT_DEFAULTS = {
    "challenge": "Beschrijf de ontwerp- of onderzoeksvraag. Wat moest er worden opgelost, voor wie en binnen welke randvoorwaarden?",
    "process": "Licht je aanpak toe: analyse, ontwerpvarianten, berekeningen, prototypes en de keuzes die je onderweg maakte.",
    "steps": ["Analyse en onderzoek", "Ontwerp en modellering", "Uitwerking, testen en evaluatie"],
    "result": "Laat het eindresultaat zien, wat je hebt geleerd en wat je een volgende keer anders zou doen.",
    "caption": "Bijschrift bij de afbeelding.",
}

# ---------------------------------------------------------------------------
# Lookups and validation

COMP_BY_NUMBER = {c["number"]: c for c in COMPETENTIES}
LEERDOELEN = {  # "1.2" -> (competentie, text)
    f"{c['number']}.{i}": (c, text)
    for c in COMPETENTIES
    for i, text in enumerate(c["leerdoelen"], start=1)
}

for _p in PROJECTS:
    for _code in _p["leerdoelen"]:
        if _code not in LEERDOELEN:
            raise SystemExit(f"error: project '{_p['slug']}' refers to unknown leerdoel {_code}")
    for _tag in _p["tags"]:
        if _tag not in TAGS:
            raise SystemExit(f"error: project '{_p['slug']}' refers to unknown tag '{_tag}'")

MONTHS = ["januari", "februari", "maart", "april", "mei", "juni",
          "juli", "augustus", "september", "oktober", "november", "december"]


def parse_month(value, where):
    try:
        year, month = (int(n) for n in value.split("-"))
        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        raise SystemExit(f"error: {where} has date '{value}'; use \"YYYY-MM\", e.g. \"2026-10\"")
    return year, month


def format_month(value):
    """ "2026-10" -> "oktober 2026" """
    year, month = parse_month(value, "a date")
    return f"{MONTHS[month - 1]} {year}"


for _p in PROJECTS:
    parse_month(_p["date"], f"project '{_p['slug']}'")
parse_month(TIMELINE["start"], "TIMELINE start")
parse_month(TIMELINE["end"], "TIMELINE end")


def comp_of(code):
    return LEERDOELEN[code][0]


def projects_for(comp):
    return [p for p in PROJECTS if any(comp_of(code) is comp for code in p["leerdoelen"])]


def codes_for(p, comp):
    return [code for code in p["leerdoelen"] if comp_of(code) is comp]


def comps_of(p):
    result = []
    for code in p["leerdoelen"]:
        if comp_of(code) not in result:
            result.append(comp_of(code))
    return result


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


# ---------------------------------------------------------------------------
# Shared markup


def page(*, title, description, prefix, body, current=None):
    def link(href, label, key):
        aria = ' aria-current="page"' if current == key else ""
        return f'<li><a class="nav__link" href="{prefix}{href}"{aria}>{label}</a></li>'

    return f"""<!DOCTYPE html>
<html lang="nl" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">

  <link rel="stylesheet" href="{prefix}css/variables.css">
  <link rel="stylesheet" href="{prefix}css/base.css">
  <link rel="stylesheet" href="{prefix}css/style.css">
  <script src="{prefix}js/main.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Direct naar de inhoud</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-header__logo" href="{prefix}index.html" aria-label="Shena, terug naar home">Shena</a>

      <nav class="nav" aria-label="Hoofdmenu">
        <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-list">
          <span class="nav__toggle-icon" aria-hidden="true"></span>
          Menu
        </button>
        <ul class="nav__list" id="nav-list">
          {link("index.html#home", "Home", "home")}
          {link("index.html#competenties", "Competenties", "competenties")}
          {link("reflectie.html", "Reflectie", "reflectie")}
          {link("index.html#contact", "Contact", "contact")}
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container site-footer__inner">
      <p>&copy; <span data-year>2026</span> Shena. Alle rechten voorbehouden.</p>
      <p><a href="{prefix}index.html">Terug naar home</a></p>
    </div>
  </footer>
</body>
</html>
"""


def tag_list(p):
    tags = "\n".join(f'                  <li class="tag">{escape(TAGS[t])}</li>' for t in p["tags"])
    return f"""                <ul class="tag-list" aria-label="Tags">
{tags}
                </ul>"""


def picsum(seed, width, height):
    """Stand-in photo from picsum.photos; the seed keeps the same photo on every load."""
    return f"https://picsum.photos/seed/{seed}/{width}/{height}"


def image_src(p, prefix, width, height):
    """A project's own image (file in images/ or a full URL), or a Picsum stand-in."""
    image = p.get("image")
    if not image:
        return picsum(f"shena-{p['slug']}", width, height)
    if image.startswith(("http://", "https://")):
        return image
    return f"{prefix}images/{image}"


def card_image(p, prefix):
    # Decorative here: the card title already names the project
    src = image_src(p, prefix, 800, 500)
    return f'<img src="{escape(src)}" alt="" width="800" height="500" loading="lazy">'


def project_card(p, prefix, comp):
    codes = ", ".join(codes_for(p, comp))
    label = "Leerdoel" if len(codes_for(p, comp)) == 1 else "Leerdoelen"
    return f"""          <li class="reveal">
            <article class="project-card">
              <div class="project-card__media">
                {card_image(p, prefix)}
              </div>
              <div class="project-card__body">
                <h3 class="project-card__title">
                  <a class="project-card__link" href="{prefix}projects/{p['slug']}.html">{escape(p['title'])}</a>
                </h3>
{tag_list(p)}
                <p class="project-card__description">{escape(p['lead'])}</p>
                <p class="project-card__leerdoelen">{label} {codes}</p>
                <p class="project-card__cta" aria-hidden="true">Bekijk project &rarr;</p>
              </div>
            </article>
          </li>"""


def competentie_card(c):
    counts = f"{plural(len(c['leerdoelen']), 'leerdoel', 'leerdoelen')} · {plural(len(projects_for(c)), 'project', 'projecten')}"
    return f"""          <li class="reveal">
            <article class="project-card theme-card">
              <div class="project-card__body">
                <p class="theme-card__number" aria-hidden="true">{c['number']}</p>
                <p class="theme-card__label">Competentie {c['number']}</p>
                <h3 class="project-card__title">
                  <a class="project-card__link" href="competenties/{c['slug']}.html">{escape(c['name'])}</a>
                </h3>
                <p class="theme-card__count">{counts}</p>
                <p class="project-card__cta" aria-hidden="true">Bekijk competentie &rarr;</p>
              </div>
            </article>
          </li>"""


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


# ---------------------------------------------------------------------------
# Pages


def build_index():
    cards = "\n\n".join(competentie_card(c) for c in COMPETENTIES)
    body = f"""    <!-- Hero -->
    <section class="hero" id="home" aria-labelledby="hero-title">
      <div class="container hero__inner">
        <div class="hero__content">
          <p class="hero__greeting">Hoi, ik ben Shena</p>
          <h1 class="hero__title" id="hero-title">
            Bouwkundige die ontwerp, data en <span class="hero__title-accent">techniek</span> verbindt.
          </h1>
          <p class="hero__text">
            Ik studeer bouwkunde en werk op het snijvlak van architectuur en techniek: van parametrisch
            ontwerpen en ruimtelijke analyses tot digitale fabricage en programmeren.
          </p>
          <div class="hero__actions">
            <a class="button button--primary" href="#competenties">Bekijk mijn werk</a>
            <a class="button button--outline" href="#contact">Neem contact op</a>
          </div>
        </div>
        <figure class="hero__image">
          <img src="{picsum('shena-hero', 800, 1000)}" alt="Voorbeeldfoto (placeholder)" width="800" height="1000">
        </figure>
      </div>
    </section>

    <!-- Competenties overview -->
    <section class="section" id="competenties" aria-labelledby="competenties-title">
      <div class="container">
        <p class="section__eyebrow">Mijn werk</p>
        <h2 id="competenties-title">Competenties</h2>
        <p class="section__intro">Mijn portfolio is opgebouwd rond vier competenties. Kies een competentie om de leerdoelen en de bijbehorende projecten te bekijken.</p>

        <ul class="project-grid theme-grid">
{cards}
        </ul>
      </div>
    </section>

{timeline()}

    <!-- Contact -->
    <section class="section contact" id="contact" aria-labelledby="contact-title">
      <div class="container">
        <p class="section__eyebrow">Contact</p>
        <h2 id="contact-title">Laten we samenwerken</h2>
        <p class="section__intro">Op zoek naar een stagiair, een samenwerking of gewoon benieuwd naar mijn werk? Neem gerust contact op.</p>

        <address>
          <ul class="contact__list">
            <li class="contact__item reveal">
              <span class="contact__label">E-mail</span>
              <a class="contact__value" href="mailto:hello@example.com">hello@example.com</a>
            </li>
            <li class="contact__item reveal">
              <span class="contact__label">Telefoon</span>
              <a class="contact__value" href="tel:+31600000000">+31 6 00 00 00 00</a>
            </li>
            <li class="contact__item reveal">
              <span class="contact__label">LinkedIn</span>
              <a class="contact__value" href="https://www.linkedin.com/" rel="noopener noreferrer" target="_blank">
                linkedin.com/in/shena<span class="visually-hidden"> (opent in een nieuw tabblad)</span>
              </a>
            </li>
            <li class="contact__item reveal">
              <span class="contact__label">GitHub</span>
              <a class="contact__value" href="https://github.com/" rel="noopener noreferrer" target="_blank">
                github.com/shena<span class="visually-hidden"> (opent in een nieuw tabblad)</span>
              </a>
            </li>
          </ul>
        </address>
      </div>
    </section>"""
    html = page(
        title="Shena | Portfolio bouwkunde",
        description="Portfolio van Shena, student bouwkunde, opgebouwd rond vier competenties.",
        prefix="", body=body,
    )
    # The home page links to its own sections
    html = html.replace('href="index.html#', 'href="#')
    write("index.html", html)


def diagram_figure(c):
    d = c.get("diagram")
    if not d:
        return ""
    if d.get("image"):
        media = f'<img src="../images/{escape(d["image"])}" alt="{escape(d["alt"])}">'
    else:
        media = (
            '<!-- Zet "image" bij het diagram van deze competentie in build.py om het diagram te tonen -->\n'
            '          <div class="project-detail__image-placeholder" role="img" aria-label="Placeholder voor diagram"></div>'
        )
    return f"""
        <figure class="project-detail__image competentie-diagram">
          {media}
          <figcaption>{escape(d['caption'])}</figcaption>
        </figure>"""


def build_competentie(c):
    prefix = "../"
    leerdoelen = "\n".join(
        f"""          <li class="leerdoel">
            <span class="leerdoel__code">{c['number']}.{i}</span>
            <p class="leerdoel__text">{escape(text)}</p>
          </li>"""
        for i, text in enumerate(c["leerdoelen"], start=1)
    )
    projects = projects_for(c)
    if projects:
        cards = "\n\n".join(project_card(p, prefix, c) for p in projects)
        project_html = f"""        <ul class="project-grid">
{cards}
        </ul>"""
    else:
        project_html = '        <p class="section__intro">Er zijn nog geen projecten aan deze competentie gekoppeld.</p>'
    others = "\n".join(
        f'          <li><a class="button button--outline" href="{o["slug"]}.html">Competentie {o["number"]}</a></li>'
        for o in COMPETENTIES if o is not c
    )
    body = f"""    <div class="container">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../index.html#competenties">Competenties</a></li>
          <li><span aria-current="page">Competentie {c['number']}</span></li>
        </ol>
      </nav>

      <header class="theme-header">
        <p class="section__eyebrow">Competentie {c['number']}</p>
        <h1>{escape(c['name'])}</h1>
      </header>

      <section class="leerdoelen" aria-labelledby="leerdoelen-title">
        <h2 id="leerdoelen-title">Leerdoelen</h2>
        <ol class="leerdoel-list">
{leerdoelen}
        </ol>{diagram_figure(c)}
      </section>

      <section class="competentie-projects" aria-labelledby="projects-title">
        <h2 id="projects-title">Projecten</h2>
{project_html}
      </section>

      <nav class="theme-nav" aria-labelledby="other-title">
        <h2 class="theme-nav__title" id="other-title">Andere competenties</h2>
        <ul class="theme-nav__list">
{others}
        </ul>
      </nav>
    </div>"""
    write(f"competenties/{c['slug']}.html", page(
        title=f"Competentie {c['number']}: {c['name']} | Shena",
        description=f"Leerdoelen en projecten van Shena voor competentie {c['number']}: {c['name']}.",
        prefix=prefix, body=body, current="competenties",
    ))


def detail_image(p):
    src = image_src(p, "../", 1200, 675)
    alt = p.get("image_alt") if p.get("image") else "Voorbeeldfoto (placeholder)"
    return f'<img src="{escape(src)}" alt="{escape(alt or "")}" width="1200" height="675">'


def build_project(p):
    c = {**CONTENT_DEFAULTS, **p}
    steps = "\n".join(f"              <li>{escape(s)}</li>" for s in c["steps"])
    steps_html = f"\n            <ul>\n{steps}\n            </ul>" if c["steps"] else ""
    comp = comp_of(p["leerdoelen"][0])  # primary competentie drives breadcrumb and navigation
    siblings = projects_for(comp)
    nxt = siblings[(siblings.index(p) + 1) % len(siblings)]
    next_link = (
        f'\n        <a class="button button--primary" href="{nxt["slug"]}.html">Volgende: {escape(nxt["title"])} &rarr;</a>'
        if nxt is not p else ""
    )
    comp_links = ", ".join(
        f'<a href="../competenties/{x["slug"]}.html">Competentie {x["number"]}</a>' for x in comps_of(p)
    )
    leerdoelen = "\n".join(
        f"""            <li class="leerdoel">
              <a class="leerdoel__code" href="../competenties/{comp_of(code)['slug']}.html" aria-label="Leerdoel {code}, competentie {comp_of(code)['number']}">{code}</a>
              <p class="leerdoel__text">{escape(LEERDOELEN[code][1])}</p>
            </li>"""
        for code in sorted(p["leerdoelen"], key=code_key)
    )
    body = f"""    <div class="container container--narrow">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../index.html#competenties">Competenties</a></li>
          <li><a href="../competenties/{comp['slug']}.html">Competentie {comp['number']}</a></li>
          <li><span aria-current="page">{escape(p['title'])}</span></li>
        </ol>
      </nav>

      <article class="project-detail">
        <header class="project-detail__header">
          <p class="section__eyebrow">Project</p>
          <h1>{escape(p['title'])}</h1>
          <p class="project-detail__lead">{escape(p['lead'])}</p>
{tag_list(p)}

          <dl class="project-detail__meta">
            <div>
              <dt>Rol</dt>
              <dd>{escape(p['role'])}</dd>
            </div>
            <div>
              <dt>Periode</dt>
              <dd>{format_month(p['date'])}</dd>
            </div>
            <div>
              <dt>Software &amp; tools</dt>
              <dd>{escape(p['tools'])}</dd>
            </div>
            <div>
              <dt>Competenties</dt>
              <dd>{comp_links}</dd>
            </div>
          </dl>
        </header>

        <figure class="project-detail__image">
          {detail_image(p)}
          <figcaption>{escape(c['caption'])}</figcaption>
        </figure>

        <div class="project-detail__content">
          <section aria-labelledby="opgave-title">
            <h2 id="opgave-title">De opgave</h2>
            <p>{escape(c['challenge'])}</p>
          </section>

          <section aria-labelledby="proces-title">
            <h2 id="proces-title">Het proces</h2>
            <p>{escape(c['process'])}</p>{steps_html}
          </section>

          <section aria-labelledby="resultaat-title">
            <h2 id="resultaat-title">Het resultaat</h2>
            <p>{escape(c['result'])}</p>
          </section>

          <section aria-labelledby="leerdoelen-title">
            <h2 id="leerdoelen-title">Aangetoonde leerdoelen</h2>
            <ol class="leerdoel-list">
{leerdoelen}
            </ol>
          </section>
        </div>
      </article>

      <nav class="project-nav" aria-label="Projectnavigatie">
        <a class="button button--outline" href="../competenties/{comp['slug']}.html">&larr; Terug naar competentie {comp['number']}</a>{next_link}
      </nav>
    </div>"""
    write(f"projects/{p['slug']}.html", page(
        title=f"{p['title']} | Shena",
        description=f"Project van Shena: {p['title']}.",
        prefix="../", body=body, current="competenties",
    ))


def code_key(code):
    return [int(n) for n in code.split(".")]


def timeline_projects():
    """Projects dated within the TIMELINE range, oldest first.

    Dates are zero-padded "YYYY-MM" strings (checked by parse_month), so they sort correctly as text.
    sorted() is stable: projects from the same month keep their order in PROJECTS.
    """
    in_range = [p for p in PROJECTS if TIMELINE["start"] <= p["date"] <= TIMELINE["end"]]
    return sorted(in_range, key=lambda x: x["date"])


def timeline():
    """Home-page slider of projects in the TIMELINE range, with cumulative leerdoel progress."""
    total = len(LEERDOELEN)
    shown = set()
    items = []
    for p in timeline_projects():
        new = sorted((code for code in p["leerdoelen"] if code not in shown), key=code_key)
        shown.update(p["leerdoelen"])
        percent = round(len(shown) / total * 100)
        when = escape(format_month(p["date"]))
        new_html = (
            f'\n              <p class="timeline-card__new">Nieuw: {", ".join(new)}</p>' if new else ""
        )
        items.append(f"""          <li class="timeline__item">
            <p class="timeline__date">{when}</p>
            <article class="project-card timeline-card">
              <div class="project-card__media">
                {card_image(p, "")}
              </div>
              <div class="project-card__body">
                <h3 class="project-card__title">
                  <a class="project-card__link" href="projects/{p['slug']}.html">{escape(p['title'])}</a>
                </h3>
{tag_list(p)}
                <div class="timeline-card__progress">
                  <p class="timeline-card__progress-label">{len(shown)} van {total} leerdoelen aangetoond</p>
                  <div class="progress-bar" aria-hidden="true"><span style="width: {percent}%"></span></div>
                </div>{new_html}
              </div>
            </article>
          </li>""")
    cards = "\n".join(items)
    period = f"{format_month(TIMELINE['start'])} – {format_month(TIMELINE['end'])}"
    return f"""    <!-- Timeline -->
    <section class="section timeline" id="tijdlijn" aria-labelledby="timeline-title" data-slider>
      <div class="container">
        <div class="timeline__header">
          <div>
            <p class="section__eyebrow">Tijdlijn · {period}</p>
            <h2 id="timeline-title">Mijn ontwikkeling</h2>
            <p class="timeline__intro">Mijn projecten van {period}, met de groei in aangetoonde leerdoelen. Klik op een project voor de details.</p>
          </div>
          <div class="timeline__controls" hidden>
            <button class="timeline__button" type="button" data-slider-prev aria-controls="timeline-track">
              <span aria-hidden="true">&larr;</span><span class="visually-hidden">Vorige projecten</span>
            </button>
            <button class="timeline__button" type="button" data-slider-next aria-controls="timeline-track">
              <span aria-hidden="true">&rarr;</span><span class="visually-hidden">Volgende projecten</span>
            </button>
          </div>
        </div>

        <ol class="timeline__track" id="timeline-track" data-slider-track>
{cards}
        </ol>
      </div>
    </section>"""


def build_reflectie():
    sections = "\n\n".join(
        f"""          <section class="star-step" aria-labelledby="reflectie-{i}-title">
            <h2 class="star-step__title" id="reflectie-{i}-title"><span class="star-step__letter" aria-hidden="true">{escape(s['letter'])}</span> {escape(s['heading'])}</h2>
""" + "\n".join(f"            <p>{escape(par)}</p>" for par in s["paragraphs"]) + """
          </section>"""
        for i, s in enumerate(REFLECTIE["sections"], start=1)
    )
    body = f"""    <div class="container container--narrow">
      <nav class="breadcrumb" aria-label="Kruimelpad">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li><span aria-current="page">{escape(REFLECTIE['title'])}</span></li>
        </ol>
      </nav>

      <header class="project-detail__header">
        <p class="section__eyebrow">Reflectie</p>
        <h1>{escape(REFLECTIE['title'])}</h1>
        <p class="project-detail__lead">{escape(REFLECTIE['lead'])}</p>
      </header>

      <section class="project-detail__content" aria-label="STAR-reflectie">
{sections}
      </section>

      <nav class="project-nav" aria-label="Paginanavigatie">
        <a class="button button--outline" href="index.html#competenties">&larr; Naar de competenties</a>
      </nav>
    </div>"""
    write("reflectie.html", page(
        title=f"{REFLECTIE['title']} | Shena",
        description="Reflectie van Shena op de eigen ontwikkeling en het portfolio.",
        prefix="", body=body, current="reflectie",
    ))


build_index()
build_reflectie()
for comp in COMPETENTIES:
    build_competentie(comp)
for proj in PROJECTS:
    build_project(proj)

# Pages left over from renamed or removed projects/competenties are not deleted automatically
expected = {f"competenties/{x['slug']}.html" for x in COMPETENTIES} | {f"projects/{x['slug']}.html" for x in PROJECTS}
for folder in ("competenties", "projects", "themes"):
    folder_path = os.path.join(ROOT, folder)
    if not os.path.isdir(folder_path):
        continue
    for name in sorted(os.listdir(folder_path)):
        if name.endswith(".html") and f"{folder}/{name}" not in expected:
            print(f"warning: {folder}/{name} is not in build.py anymore; delete it if it is no longer needed")
