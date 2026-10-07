#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIA GNOSIS — générateur du site (tvt90.github.io/via-gnosis)

Toute modification du site passe par ce fichier, jamais par l'édition directe des HTML.
  - le menu, le pied de page et l'en-tête sont définis UNE SEULE FOIS ci-dessous ;
  - chaque page est un appel page(...) avec son fichier, sa rubrique du menu,
    son titre, sa description (pour les moteurs de recherche) et son contenu.
Usage : python3 build.py   → régénère tous les .html dans le dossier courant.
"""

# ── Menu : un mot = une destination ─────────────────────────────────────────
MENU = [
    ("la-source",     "la-source.html",     "La source"),
    ("atelier",       "atelier.html",       "L'atelier"),
    ("materialiser",  "materialiser.html",  "Matérialiser"),
    ("prestations",   "prestations.html",   "Prestations"),
    ("presse-agenda", "presse-agenda.html", "Presse &amp; agenda"),
    ("echanger",      "echanger.html",      "Échanger"),
]

# ── Pied de page : même vocabulaire que le menu et les titres de pages ──────
PIED = [
    ("La source", [("la-source.html", "Pourquoi Via Gnosis ?"), ("la-demarche.html", "La démarche"),
                   ("les-valeurs.html", "Les valeurs"), ("le-fondateur.html", "Le fondateur")]),
    ("L'atelier", [("atelier-musical.html", "L'atelier musical"), ("atelier-visuel.html", "L'atelier visuel")]),
    ("Matérialiser", [("arts-visuels.html", "Arts visuels"), ("musique.html", "Musique"),
                      ("cahiers.html", "Les Cahiers")]),
    ("Prestations", [("formations.html", "Formations"), ("conseil.html", "Conseil"),
                     ("chanson-personnalisee.html", "Chanson personnalisée")]),
    ("Presse &amp; contact", [("presse-agenda.html", "Presse &amp; agenda"), ("echanger.html", "Échanger"),
                         ("https://tvt90.github.io/artist-presentation/", "Site artiste ↗")]),
]

LOGO_SVG = '''<svg class="mark" viewBox="0 0 100 104" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><circle cx="50" cy="56" r="40" fill="none" stroke="#E8C97A" stroke-width="2" stroke-linecap="round" stroke-dasharray="226 25" stroke-dashoffset="-12.5" transform="rotate(-90 50 56)"/><path d="M53.6 3 L55.2 11 L52.1 17.5 L55.8 25 L52.4 32 L56.6 39.5 L52.2 46.5 L56.4 53.5 L52.6 61 L54.4 68.5 L51.6 75 L50.4 82 L52.9 75.4 L57.1 68.2 L55.2 60.6 L59.1 53.2 L55.0 46.2 L59.4 39.2 L55.3 31.8 L58.7 24.7 L55.0 17.2 L57.9 10.8 L55.1 3 Z" fill="#D4A843"/></svg>'''

ACTIF = ' class="active"'

def en_tete(rubrique):
    liens = "\n".join(
        f'    <a href="{f}"{ACTIF if r == rubrique else ""}>{t}</a>' for r, f, t in MENU)
    return f'''<header class="hdr">
  <a href="index.html" class="brand">{LOGO_SVG}<span>Via Gnosis</span></a>
  <nav class="nav">
{liens}
  </nav>
</header>'''

def pied():
    cols = []
    for titre, liens in PIED:
        a = []
        for f, t in liens:
            ext = ' target="_blank" rel="noopener"' if f.startswith("http") else ""
            a.append(f'      <a href="{f}"{ext}>{t}</a>')
        cols.append(f'    <div class="ftr-col">\n      <h4>{titre}</h4>\n' + "\n".join(a) + "\n    </div>")
    return '''<footer class="ftr">
  <div class="ftr-top">
    <div class="ftr-brand">
      <img src="logo-light.png" alt="VIA GNOSIS">
      <p>Une voie contemporaine de connaissance et de création.</p>
      <p class="accent">L'humain imagine. L'IA amplifie. Ensemble, ils créent.</p>
    </div>
''' + "\n".join(cols) + '''
  </div>
  <div class="ftr-bot">
    <p>© 2026 VIA GNOSIS — Thierry Voitot</p>
    <p>Fait en Franche-Comté</p>
  </div>
</footer>'''

PAGES = []

def page(fichier, rubrique, title, desc, body_class, body):
    PAGES.append(dict(fichier=fichier, rubrique=rubrique, title=title, desc=desc,
                      body_class=body_class, body=body.strip("\n")))

def rendu(p):
    classe = f' class="{p["body_class"]}"' if p["body_class"] else ""
    # l'accueil n'a pas de pied de page : rien sous l'image, aucun défilement
    bas = "" if p["fichier"] == "index.html" else "\n" + pied() + "\n"
    desc = p["desc"].replace('"', "&quot;")
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body{classe}>

{en_tete(p["rubrique"])}

{p["body"]}
{bas}
</body>
</html>
'''

# ════════════════════════════════════════════════════════════════════════════
#  LES PAGES
# ════════════════════════════════════════════════════════════════════════════

page("index.html", "",
  title='VIA GNOSIS — Une voie contemporaine de connaissance et de création',
  desc='VIA GNOSIS — Thierry Voitot, formateur en intelligence artificielle et artiste. Conseil en transmission des connaissances et ingénierie pédagogique.',
  body_class='splash',
  body="""
<section class="hero">
  <div class="hero-bg" style="background-image:url('hero-accueil.jpg')"></div>
  <div class="hero-fracture" aria-hidden="true"></div>
  <div class="hero-inner">
    <h1>VIA GNOSIS</h1>
    <p class="hero-lead">Une voie contemporaine de connaissance et de création.</p>
    <p class="hero-tag">L'humain imagine. L'IA amplifie. Ensemble, ils créent.</p>
    <a href="la-source.html" class="btn">Entrer &nbsp;→</a>
  </div>
</section>
""")

page("la-source.html", "la-source",
  title='Pourquoi Via Gnosis ? — VIA GNOSIS',
  desc="L'histoire, la démarche et les valeurs de VIA GNOSIS — Thierry Voitot, formateur en intelligence artificielle et artiste.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="la-source-bandeau-v2.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — La source</p>
  <h1>Pourquoi Via Gnosis ?</h1>
  <p>L'histoire, la démarche et les convictions derrière le projet.</p>
</section>

<section class="rich">
  <p class="rich-lead">Vous n'entrez pas sur un site. Vous entrez dans un atelier.</p>
  <p>Parce qu'une idée ne vaut que si elle devient une expérience. Parce qu'une technologie ne vaut que si elle révèle davantage d'humanité.</p>
  <p>Parce que créer, transmettre et comprendre ne sont pas trois chemins différents. Ils sont les trois visages d'une même aventure.</p>
  <p>VIA GNOSIS réunit deux activités : le conseil en transmission des connaissances et ingénierie pédagogique d'une part, la formation et l'exploration en intelligence artificielle d'autre part.</p>
</section>

<section class="blocks">
  <a href="la-demarche.html" class="block block-link">
    <div class="block-media"><img src="source-atelier.jpg" alt="La démarche"></div>
    <div class="block-body"><h3>La démarche</h3><p>Démystifier plutôt qu'impressionner. Faire pratiquer plutôt que faire écouter. L'humain reste au centre du processus créatif.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="le-fondateur.html" class="block block-link">
    <div class="block-media"><img src="fondateur-portrait.jpg" alt="Le fondateur"></div>
    <div class="block-body"><h3>Le fondateur</h3><p>Thierry Voitot — vingt-huit ans de conseil en transmission des connaissances, auteur-compositeur SACEM et artiste sous le nom Nova and I.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="les-valeurs.html" class="block block-link">
    <div class="block-media"><img src="valeurs-transmission.jpg" alt="Les valeurs"></div>
    <div class="block-body"><h3>Les valeurs</h3><p>L'accessibilité avant la performance, la pratique avant la théorie, le lien avant l'outil.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="section-band">
  <div class="band-head">
    <h2>Trois chemins, une même aventure</h2>
  </div>
<div class="pillars">
  <a href="atelier.html" class="pillar">
    <div class="pillar-media"><img src="pilier-atelier.jpg" alt="L'atelier"></div>
    <div class="pillar-body">
      <div class="pillar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></svg></div>
      <h3>L'atelier</h3>
      <p>Comment naissent les œuvres.</p>
      <span class="more">Découvrir</span>
    </div>
  </a>
  <a href="materialiser.html" class="pillar">
    <div class="pillar-media"><img src="pilier-materialiser.jpg" alt="Matérialiser"></div>
    <div class="pillar-body">
      <div class="pillar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M9 18V5l10-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="16" cy="16" r="3"/></svg></div>
      <h3>Matérialiser</h3>
      <p>Donner forme à une idée.</p>
      <span class="more">Découvrir</span>
    </div>
  </a>
  <a href="prestations.html" class="pillar">
    <div class="pillar-media"><img src="pilier-formations.jpg" alt="Prestations"></div>
    <div class="pillar-body">
      <div class="pillar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 8h5M18.5 5.5v5"/></svg></div>
      <h3>Prestations</h3>
      <p>Ce que Via Gnosis propose.</p>
      <span class="more">Découvrir</span>
    </div>
  </a>
</div>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Et si nous créions ensemble ?</h2>
    <p>Une idée, un projet, une envie de collaboration ? Écrivons la suite.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("la-demarche.html", "la-source",
  title='La démarche — VIA GNOSIS',
  desc="La démarche de VIA GNOSIS — démystifier plutôt qu'impressionner, faire pratiquer plutôt que faire écouter.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="source-atelier.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — La source</p>
  <h1>La démarche</h1>
  <p>Démystifier plutôt qu'impressionner. Faire pratiquer plutôt que faire écouter.</p>
</section>

<section class="rich">
  <p class="rich-lead">L'humain reste au centre du processus créatif.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une question sur la démarche ?</h2>
    <p>Écrivez-moi, je vous répondrai volontiers.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("le-fondateur.html", "la-source",
  title='Le fondateur — VIA GNOSIS',
  desc='Thierry Voitot — vingt-huit ans de conseil en transmission des connaissances, auteur-compositeur SACEM et artiste sous le nom Nova and I.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="fondateur-portrait.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — La source</p>
  <h1>Le fondateur</h1>
  <p>Thierry Voitot — conseil en transmission des connaissances, auteur-compositeur et artiste.</p>
</section>

<section class="rich">
  <p class="rich-lead">Vingt-huit ans à transmettre, quelques années à créer autrement.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie d'échanger ?</h2>
    <p>Formations, missions de conseil, collaborations — la porte est ouverte.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("les-valeurs.html", "la-source",
  title='Les valeurs — VIA GNOSIS',
  desc="Les valeurs de VIA GNOSIS — l'accessibilité avant la performance, la pratique avant la théorie.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="valeurs-transmission.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — La source</p>
  <h1>Les valeurs</h1>
  <p>L'accessibilité avant la performance, la pratique avant la théorie, le lien avant l'outil.</p>
</section>

<section class="rich">
  <p class="rich-lead">Ce qui ne se négocie pas.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Ces valeurs vous parlent ?</h2>
    <p>Parlons de ce que nous pourrions construire ensemble.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("atelier.html", "atelier",
  title="L'atelier — VIA GNOSIS",
  desc="L'atelier VIA GNOSIS — comment naissent les œuvres : l'intention humaine d'abord, puis la structuration, puis le dialogue avec l'intelligence artificielle.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="atelier-methode.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — L'atelier</p>
  <h1>L'atelier</h1>
  <p>Comment naissent les œuvres — un établi par médium, un même mouvement en trois temps.</p>
</section>

<section class="rich">
  <p class="rich-lead">L'idée vient d'abord. Toujours.</p>
  <p>Chaque création part d'une intention humaine, souvent déjà très aboutie mentalement — une image, une couleur, une intention musicale. Cette idée est voulue et assumée : elle n'est pas suggérée par la machine.</p>
  <p>Vient ensuite la structuration, puis le dialogue : requêtes, instructions, allers-retours, jusqu'à l'aboutissement attendu. L'humain imagine, l'IA amplifie.</p>
  <p>Les manières de faire varient selon ce que l'on fabrique — une chanson ne se conduit pas comme une image. D'où plusieurs établis dans le même atelier.</p>
</section>

<section class="blocks">
  <a href="atelier-musical.html" class="block block-link">
    <div class="block-media"><img src="atelier-musical-duo.jpg" alt="L'atelier musical"></div>
    <div class="block-body"><h3>L'atelier musical</h3><p>Comment naît une chanson : l'intention musicale, les paroles écrites avec Marie-Thérèse Lecrille, puis le dialogue jusqu'à la composition.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="atelier-visuel.html" class="block block-link">
    <div class="block-media"><img src="atelier-visuel-fusain.jpg" alt="L'atelier visuel"></div>
    <div class="block-body"><h3>L'atelier visuel</h3><p>Comment naît une image : l'intuition picturale, la structuration du projet, puis les échanges successifs jusqu'à l'œuvre.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Curieux de la méthode ?</h2>
    <p>Formations, ateliers, démonstrations — la porte de l'atelier est ouverte.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("atelier-musical.html", "atelier",
  title="L'atelier musical — VIA GNOSIS",
  desc="L'atelier musical de VIA GNOSIS — comment naît une chanson, de l'intention à la composition.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="atelier-musical-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — L'atelier</p>
  <h1>L'atelier musical</h1>
  <p>Comment naît une chanson — l'intention musicale, les paroles, puis la composition.</p>
</section>

<section class="rich">
  <p class="rich-lead">Une intention musicale précise, avant toute machine.</p>
  <p>Texte à rédiger.</p>
  <p><span style='font-size:13px'>Photo : C. Gauchet — L'Est Républicain</span></p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie d'écouter ou d'apprendre ?</h2>
    <p>Les albums sont en ligne, et les ateliers ouverts.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("atelier-visuel.html", "atelier",
  title="L'atelier visuel — VIA GNOSIS",
  desc="L'atelier visuel de VIA GNOSIS — comment naît une image, de l'intuition picturale à l'œuvre.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="atelier-visuel-fusain.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — L'atelier</p>
  <h1>L'atelier visuel</h1>
  <p>Comment naît une image — l'intuition picturale, la structuration, puis les échanges.</p>
</section>

<section class="rich">
  <p class="rich-lead">L'image existe mentalement avant d'exister à l'écran.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie de voir ou d'apprendre ?</h2>
    <p>Les collections sont en ligne, et les ateliers ouverts.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("materialiser.html", "materialiser",
  title='Matérialiser — VIA GNOSIS',
  desc="Le volet création de VIA GNOSIS : arts visuels et musique — les œuvres abouties d'une démarche de symbiose humain-IA.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="materialiser-lune.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Matérialiser</p>
  <h1>Matérialiser</h1>
  <p>Les œuvres abouties. Arts visuels et musique — la matière première reste humaine.</p>
</section>

<section class="rich">
  <p class="rich-lead">Ce qui existait mentalement existe désormais pour de bon.</p>
  <p>Sous le nom Nova and I pour les arts visuels, et avec le duo Les Fêlés pour la musique, la création est le terrain d'expérimentation d'où sortent toutes les formations.</p>
  <p>On ne transmet bien que ce que l'on pratique. Les ateliers proposés ne sont pas théoriques : ils reprennent, pas à pas, les gestes de cette pratique quotidienne.</p>
</section>

<section class="blocks">
  <a href="arts-visuels.html" class="block block-link">
    <div class="block-media"><img src="arts-visuels-resistance.jpg" alt="Arts visuels — Nova and I"></div>
    <div class="block-body"><h3>Arts visuels — Nova and I</h3><p>Sept collections picturales, du kintsugi aux hautes coutures culturelles, chacune explorant ce que l'humain seul ne saurait imaginer.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="musique.html" class="block block-link">
    <div class="block-media"><img src="musique-yeux-du-pere.jpg" alt="Musique — Les Fêlés"></div>
    <div class="block-body"><h3>Musique — Les Fêlés</h3><p>Avec Marie-Thérèse Lecrille — poétesse et parolière — plus de cent compositions mêlant poésie, mélodie et symbiose IA.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="cahiers.html" class="block block-link">
    <div class="block-media"><img src="cahiers-jack.jpg" alt="Les Cahiers Via Gnosis"></div>
    <div class="block-body"><h3>Les Cahiers Via Gnosis</h3><p>Récits et carnets illustrés accompagnant chaque création : un objet hybride où se rejoignent littérature, arts visuels et musique.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un projet de création ?</h2>
    <p>Collaborations artistiques, commandes, projets culturels — écrivons la suite.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("arts-visuels.html", "materialiser",
  title='Arts visuels — VIA GNOSIS',
  desc="Arts visuels — Nova and I : sept collections picturales nées d'une symbiose humain-IA.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="arts-visuels-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Matérialiser</p>
  <h1>Arts visuels</h1>
  <p>Nova and I — sept collections picturales, du kintsugi aux hautes coutures culturelles.</p>
</section>

<section class="rich">
  <p class="rich-lead">Ce que l'humain seul ne saurait imaginer, ce que l'IA seule ne saurait vouloir.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une œuvre, une exposition ?</h2>
    <p>Commandes, expositions, collaborations — écrivons la suite.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("musique.html", "materialiser",
  title='Musique — VIA GNOSIS',
  desc='Musique — Les Fêlés : plus de cent compositions mêlant poésie, mélodie et symbiose IA.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="musique-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Matérialiser</p>
  <h1>Musique</h1>
  <p>Les Fêlés — avec Marie-Thérèse Lecrille, poétesse et parolière.</p>
</section>

<section class="rich">
  <p class="rich-lead">Des mots d'abord. La mélodie vient ensuite.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie d'écouter ?</h2>
    <p>Les albums sont en ligne, et les collaborations toujours ouvertes.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("cahiers.html", "materialiser",
  title='Les Cahiers Via Gnosis — VIA GNOSIS',
  desc='Les Cahiers Via Gnosis — récits et carnets illustrés accompagnant chaque création.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="cahiers-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Matérialiser</p>
  <h1>Les Cahiers Via Gnosis</h1>
  <p>Récits et carnets illustrés — la trace écrite du chemin parcouru.</p>
</section>

<section class="rich">
  <p class="rich-lead">Chaque œuvre laisse un carnet derrière elle.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie de lire un cahier ?</h2>
    <p>Écrivez-moi, je vous en enverrai volontiers un.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("formations.html", "prestations",
  title='Formations — VIA GNOSIS',
  desc='Formations-actions en intelligence artificielle : ateliers de création, formation pédagogique, jeune public — sur mesure et sur devis.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="echanger-formations.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Prestations</p>
  <h1>Formations</h1>
  <p>Ce que Via Gnosis propose — des formations-actions participatives, où chacun met les mains dans la matière.</p>
</section>

<section class="rich">
  <p class="rich-lead">Pas de conférences à l'ancienne. Apprendre, c'est créer.</p>
  <p>Chaque intervention part de ce que les participants apportent — une photographie, un souvenir, un mot — et le transforme en œuvre. L'intelligence artificielle n'est jamais le sujet : elle est le moyen.</p>
  <p>Vingt-huit ans de conseil en transmission des connaissances et en ingénierie pédagogique nourrissent chaque format proposé. La pédagogie passe avant l'outil.</p>
  <p>Chaque besoin est unique : chacun de ces formats s'adapte au public, à la durée et à l'objectif visé, sur devis personnalisé.</p>
</section>

<section class="blocks">
  <a href="creation-artistique.html" class="block block-link">
    <div class="block-media"><img src="https://tvt90.github.io/artist-presentation/images/homme-nature-1.jpg" alt="Création artistique avec IA"></div>
    <div class="block-body"><h3>Création artistique avec IA</h3><p>Atelier-découverte ouvert aux familles, aux individus et aux groupes : prendre une photographie, un souvenir ou un mot, et le transformer en œuvre.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="formation-pedagogique.html" class="block block-link">
    <div class="block-media"><img src="https://tvt90.github.io/artist-presentation/images/cafe-debat-ia.png" alt="Formation pédagogique"></div>
    <div class="block-body"><h3>Formation pédagogique</h3><p>Pour les enseignants, animateurs et médiateurs culturels : intégrer l'intelligence artificielle dans la transmission, sans la subir.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="ateliers-jeune-public.html" class="block block-link">
    <div class="block-media"><img src="https://tvt90.github.io/artist-presentation/images/atelier-ia-chatenois-2026-06.png" alt="Ateliers jeune public"></div>
    <div class="block-body"><h3>Ateliers jeune public</h3><p>Pour les enfants de 8 à 12 ans : une sensibilisation aux bonnes pratiques de l'IA par la pratique artistique.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une formation à organiser ?</h2>
    <p>Parlons de votre public, de vos objectifs et du format qui conviendra.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("creation-artistique.html", "prestations",
  title='Création artistique avec IA — VIA GNOSIS',
  desc='Atelier-découverte de création artistique avec intelligence artificielle, pour familles, individus et groupes.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="https://tvt90.github.io/artist-presentation/images/homme-nature-1.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Formations</p>
  <h1>Création artistique avec IA</h1>
  <p>Prendre une photographie, un souvenir ou un mot, et le transformer en œuvre.</p>
</section>

<section class="rich">
  <p class="rich-lead">Tous publics — familles, individus, groupes.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Envie d'essayer ?</h2>
    <p>Décrivez votre contexte, je vous proposerai un format adapté.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("formation-pedagogique.html", "prestations",
  title='Formation pédagogique — VIA GNOSIS',
  desc="Formation à l'intelligence artificielle pour enseignants, animateurs et médiateurs culturels.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="https://tvt90.github.io/artist-presentation/images/cafe-debat-ia.png" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Formations</p>
  <h1>Formation pédagogique</h1>
  <p>Intégrer l'intelligence artificielle dans la transmission, sans la subir.</p>
</section>

<section class="rich">
  <p class="rich-lead">Pour les enseignants, animateurs et médiateurs culturels.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une équipe à former ?</h2>
    <p>Parlons de vos objectifs et du format qui conviendra.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("ateliers-jeune-public.html", "prestations",
  title='Ateliers jeune public — VIA GNOSIS',
  desc="Ateliers de sensibilisation à l'intelligence artificielle pour les enfants de 8 à 12 ans, par la pratique artistique.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="https://tvt90.github.io/artist-presentation/images/atelier-ia-chatenois-2026-06.png" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Formations</p>
  <h1>Ateliers jeune public</h1>
  <p>Sensibiliser aux bonnes pratiques de l'IA par la pratique artistique.</p>
</section>

<section class="rich">
  <p class="rich-lead">Pour les enfants de 8 à 12 ans.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un atelier à organiser ?</h2>
    <p>Écoles, médiathèques, centres de loisirs — parlons-en.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("conseil.html", "prestations",
  title='Conseil — VIA GNOSIS',
  desc="Conseil en transmission des connaissances et ingénierie pédagogique — vingt-huit ans d'expérience au service des organisations et des institutions.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="echanger-conseil.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Prestations</p>
  <h1>Conseil</h1>
  <p>Transmission des connaissances et ingénierie pédagogique — la seconde activité de Via Gnosis.</p>
</section>

<section class="rich">
  <p class="rich-lead">Vingt-huit ans à concevoir des dispositifs qui transmettent vraiment.</p>
  <p>Avant l'intelligence artificielle, il y a la pédagogie. Structurer un savoir, identifier ce qui doit être transmis, concevoir le dispositif qui le rendra assimilable : c'est le métier exercé pendant vingt-huit ans, et c'est lui qui fonde tout le reste.</p>
  <p>Cette activité s'adresse aux organisations, collectivités et institutions qui ont un savoir à transmettre et cherchent la manière de le faire.</p>
  <p>Texte à compléter.</p>
</section>

<section class="blocks">
  <a href="ingenierie-pedagogique.html" class="block block-link">
    <div class="block-media"><img src="pilier-explorer.jpg" alt="Ingénierie pédagogique"></div>
    <div class="block-body"><h3>Ingénierie pédagogique</h3><p>Conception de dispositifs de formation : analyse du besoin, architecture des contenus, scénarisation et évaluation.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="transmission-connaissances.html" class="block block-link">
    <div class="block-media"><img src="source-atelier.jpg" alt="Transmission des connaissances"></div>
    <div class="block-body"><h3>Transmission des connaissances</h3><p>Structuration et formalisation des savoirs d'une organisation, pour qu'ils survivent aux départs et se transmettent.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une mission à confier ?</h2>
    <p>Décrivez votre contexte et vos objectifs — nous verrons ensemble ce qui convient.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("ingenierie-pedagogique.html", "prestations",
  title='Ingénierie pédagogique — VIA GNOSIS',
  desc='Ingénierie pédagogique — conception de dispositifs de formation : analyse du besoin, architecture des contenus, scénarisation et évaluation.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="pilier-explorer.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Conseil</p>
  <h1>Ingénierie pédagogique</h1>
  <p>Concevoir des dispositifs de formation qui transmettent vraiment.</p>
</section>

<section class="rich">
  <p class="rich-lead">Un dispositif de formation se conçoit avant de s'animer.</p>
  <p>Analyse du besoin, architecture des contenus, scénarisation des séquences, modalités d'évaluation : chaque étape conditionne ce que les participants retiendront.</p>
  <p>Texte à rédiger.</p>
  <p><strong>Références</strong> — à compléter.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un dispositif à concevoir ?</h2>
    <p>Décrivez votre contexte et vos objectifs — nous verrons ensemble ce qui convient.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("transmission-connaissances.html", "prestations",
  title='Transmission des connaissances — VIA GNOSIS',
  desc="Transmission des connaissances — structuration et formalisation des savoirs d'une organisation pour qu'ils survivent aux départs.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="source-atelier.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Conseil</p>
  <h1>Transmission des connaissances</h1>
  <p>Formaliser ce qui ne s'écrit nulle part, pour que cela survive aux départs.</p>
</section>

<section class="rich">
  <p class="rich-lead">Un savoir qui ne circule pas est un savoir qui se perd.</p>
  <p>Dans toute organisation, l'essentiel du savoir-faire n'est écrit nulle part : il vit dans les gestes, les habitudes et la mémoire de quelques personnes. Le formaliser, c'est le rendre transmissible.</p>
  <p>Texte à rédiger.</p>
  <p><strong>Références</strong> — à compléter.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un savoir à préserver ?</h2>
    <p>Parlons de votre organisation et de ce qui mérite d'être transmis.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("presse-agenda.html", "presse-agenda",
  title='Presse &amp; agenda — VIA GNOSIS',
  desc='Articles de presse, reportages et prochains rendez-vous de VIA GNOSIS.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="presse-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Presse &amp; agenda</p>
  <h1>Presse &amp; agenda</h1>
  <p>Ce que la presse en dit, et où nous croiser.</p>
</section>

<section class="rich">
  <p class="eyebrow">Agenda</p>
  <p class="rich-lead">Les derniers rendez-vous.</p>
</section>
<section class="blocks">
  <article class="block block-agenda">
    <div class="block-body"><span class="agenda-date">29 &amp; 30 août 2026</span><h3>24ᵉ Salon des Arts de Sochaux</h3><p>Avec Marie-Thérèse Lecrille — neuf œuvres exposées. Vernissage le vendredi 28 août à 17h30, salons de l'Hôtel de Ville.</p></div>
  </article>
  <article class="block block-agenda">
    <div class="block-body"><span class="agenda-date">1er au 25 septembre 2026</span><h3>Héros du quotidien</h3><p>Exposition personnelle à l'Hôpital Nord Franche-Comté — trente illustrations en six séries, dans le cadre du dispositif Culture &amp; Santé.</p></div>
  </article>
</section>

<section class="rich">
  <p class="eyebrow">Presse</p>
  <p class="rich-lead">Ils en ont parlé.</p>
  <p>Dix parutions depuis décembre 2024 — expositions, ateliers, portraits. Cliquez sur un article
  pour le lire en entier.</p>
</section>
<section class="blocks">
  <a href="presse-2026-06-13-mediatheque.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2026-06-13-mediatheque.jpg" alt="Une initiation à l'intelligence artificielle par la musique"></div>
    <div class="block-body">
      <span class="agenda-date">13 juin 2026 · L'Est Républicain</span>
      <h3>Une initiation à l'intelligence artificielle par la musique</h3>
      <p>Atelier parent-enfant à la médiathèque de Châtenois-les-Forges : composer une chanson en deux heures.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2026-04-10-feles-poesie.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2026-04-10-feles-poesie.jpg" alt="Les Fêlés mêlent poésie et intelligence artificielle"></div>
    <div class="block-body">
      <span class="agenda-date">10 avril 2026 · L'Est Républicain</span>
      <h3>Les Fêlés mêlent poésie et intelligence artificielle</h3>
      <p>Portrait du duo et de ses projets d'animations et de compositions sur mesure.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-12-15-lorius.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-12-15-lorius.jpg" alt="Intelligence artificielle et tradition se rencontrent lors d'une exposition"></div>
    <div class="block-body">
      <span class="agenda-date">15 décembre 2025 · L'Est Républicain</span>
      <h3>Intelligence artificielle et tradition se rencontrent lors d'une exposition</h3>
      <p>Exposition chez Lorius à Brognard, avec les arrapolisculptures de Marie-Thérèse Lecrille.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-09-19-duo.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-09-19-duo.jpg" alt="Un duo d'artistes met la poésie en musique au cœur de l'ère numérique"></div>
    <div class="block-body">
      <span class="agenda-date">19 septembre 2025 · L'Est Républicain</span>
      <h3>Un duo d'artistes met la poésie en musique au cœur de l'ère numérique</h3>
      <p>Les Fêlés : écriture poétique, composition méticuleuse, et l'IA comme partenaire.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-06-04-guilde.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-06-04-guilde.jpg" alt="La Guilde des poètes renoue avec la tradition des salons des Lumières"></div>
    <div class="block-body">
      <span class="agenda-date">4 juin 2025 · L'Est Républicain</span>
      <h3>La Guilde des poètes renoue avec la tradition des salons des Lumières</h3>
      <p>Un cercle créatif collaboratif né à Châtenois-les-Forges, à l'initiative de Thierry Voitot.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-05-24-partenaire.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-05-24-partenaire.jpg" alt="L'IA comme partenaire artistique, le pari audacieux de Thierry Voitot"></div>
    <div class="block-body">
      <span class="agenda-date">24 mai 2025 · L'Est Républicain</span>
      <h3>L'IA comme partenaire artistique, le pari audacieux de Thierry Voitot</h3>
      <p>Portrait : art numérique, poésie, musique et pédagogie sous le pseudonyme Nova and I.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-04-01-vauthiermont.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-04-01-vauthiermont.jpg" alt="L'art sous toutes ses formes à Vauthiermont"></div>
    <div class="block-body">
      <span class="agenda-date">1er avril 2025 · L'Est Républicain</span>
      <h3>L'art sous toutes ses formes à Vauthiermont</h3>
      <p>Exposition et atelier sur l'art généré par IA, aux côtés d'une trentaine d'artistes.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2025-02-21-cafe-debat.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2025-02-21-cafe-debat.jpg" alt="L'intelligence artificielle a passionné soixante-dix personnes"></div>
    <div class="block-body">
      <span class="agenda-date">21 février 2025 · L'Est Républicain</span>
      <h3>L'intelligence artificielle a passionné soixante-dix personnes</h3>
      <p>Café-débat à la maison de quartier du centre-ville de Belfort, de 17 à 80 ans.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2024-12-24-france3.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2024-12-24-france3.jpg" alt="« Il y a un processus de création derrière tout ça »"></div>
    <div class="block-body">
      <span class="agenda-date">24 décembre 2024 · France 3 Bourgogne-Franche-Comté</span>
      <h3>« Il y a un processus de création derrière tout ça »</h3>
      <p>Reportage sur l'exposition de Brognard : peintures, photos et dessins entièrement créés avec l'IA.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
  <a href="presse-2024-12-15-lorius.jpg" target="_blank" rel="noopener" class="block block-link">
    <div class="block-media"><img src="presse-2024-12-15-lorius.jpg" alt="Chez Lorius, une expo photo réalisée avec l'intelligence artificielle"></div>
    <div class="block-body">
      <span class="agenda-date">15 décembre 2024 · L'Est Républicain</span>
      <h3>Chez Lorius, une expo photo réalisée avec l'intelligence artificielle</h3>
      <p>Exposition immersive à Brognard : flashcodes, musique et collections Fashion Week.</p>
      <span class="more">Lire l'article</span>
    </div>
  </a>
</section>

<section class="rich">
  <p class="eyebrow">Documents</p>
  <p class="rich-lead">À télécharger.</p>
  <p><a href="dossier-presse-les-feles.pdf" target="_blank" rel="noopener">Dossier de presse Les Fêlés (PDF)</a><br>
  <a href="article-france3-2024.pdf" target="_blank" rel="noopener">Article France 3 Bourgogne-Franche-Comté, décembre 2024 (PDF)</a></p>
</section>

<section class="rich">
  <p style="font-size:13px;">Crédits photographiques et rédactionnels : L'Est Républicain,
  France 3 Bourgogne-Franche-Comté. Reproduction avec autorisation.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un événement, une interview ?</h2>
    <p>Journalistes, organisateurs, structures culturelles — écrivons la suite.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("echanger.html", "echanger",
  title='Échanger — VIA GNOSIS',
  desc='Contacter VIA GNOSIS — Thierry Voitot : formations, missions de conseil et collaborations artistiques.',
  body_class='',
  body="""
<section class="page-banner">
  <img src="echanger-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Échanger</p>
  <h1>Échanger</h1>
  <p>Une idée, un projet, une envie de collaboration ? Écrivons la suite.</p>
</section>

<section class="rich">
  <p class="rich-lead">Chaque projet commence par une conversation.</p>
  <p>Formations et ateliers, missions de conseil en ingénierie pédagogique, chansons personnalisées,
  projets culturels ou artistiques — décrivez votre contexte et vos objectifs, je vous répondrai rapidement.</p>
</section>

<section class="contact-band">
  <a class="contact-card" href="mailto:tvoitot.ia@gmail.com">
    <span class="contact-label">Courriel</span>
    <span class="contact-value">tvoitot.ia@gmail.com</span>
  </a>
  <a class="contact-card" href="tel:+33683582755">
    <span class="contact-label">Téléphone</span>
    <span class="contact-value">06 83 58 27 55</span>
  </a>
</section>

<section class="rich">
  <p class="eyebrow">Les prestations</p>
  <p class="rich-lead">Ce que Via Gnosis peut prendre en charge.</p>
</section>
<section class="blocks">
  <article class="block">
    <div class="block-media"><img src="echanger-formations.jpg" alt="Formations &amp; ateliers"></div>
    <div class="block-body"><h3>Formations &amp; ateliers</h3><p>Ateliers de création artistique avec IA, formations pour professionnels de la transmission, ateliers jeune public. Durée, public et contenu adaptés à votre contexte, sur devis.</p><span class="tag">Devis personnalisé</span></div>
  </article>
  <article class="block">
    <div class="block-media"><img src="echanger-conseil.jpg" alt="Conseil &amp; ingénierie pédagogique"></div>
    <div class="block-body"><h3>Conseil &amp; ingénierie pédagogique</h3><p>Conception de dispositifs de formation, structuration et formalisation des savoirs d'une organisation, accompagnement des équipes. Vingt-huit ans d'expérience au service des institutions et des collectivités.</p><span class="tag">Missions</span></div>
  </article>
  <article class="block">
    <div class="block-media"><img src="echanger-collaborations.jpg" alt="Collaborations artistiques"></div>
    <div class="block-body"><h3>Collaborations artistiques</h3><p>Expositions, commandes d'œuvres, projets culturels, résidences ou créations communes — en arts visuels comme en musique.</p><span class="tag">Projets</span></div>
  </article>
</section>

<section class="rich">
  <p class="eyebrow">Formulaire</p>
  <p class="rich-lead">Écrivez-moi directement.</p>
</section>
<section class="form-wrap">
  <form class="contact-form" action="https://formspree.io/f/mbgrzdga" method="POST">
    <div class="field-row">
      <label>Nom
        <input type="text" name="nom" required>
      </label>
      <label>Courriel
        <input type="email" name="_replyto" required>
      </label>
    </div>
    <div class="field-row">
      <label>Téléphone <span class="opt">(facultatif)</span>
        <input type="tel" name="telephone">
      </label>
      <label>Objet
        <select name="objet">
          <option>Formation ou atelier</option>
          <option>Conseil et ingénierie pédagogique</option>
          <option>Chanson personnalisée</option>
          <option>Collaboration artistique</option>
          <option>Presse</option>
          <option>Autre</option>
        </select>
      </label>
    </div>
    <label>Votre message
      <textarea name="message" rows="7" required></textarea>
    </label>
    <input type="hidden" name="_subject" value="Nouveau message depuis via-gnosis.fr">
    <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
    <button type="submit" class="btn btn-fill">Envoyer &nbsp;→</button>
  </form>
</section>
""")

page("prestations.html", "prestations",
  title='Prestations — VIA GNOSIS',
  desc="Les prestations de VIA GNOSIS : formations en intelligence artificielle, conseil en transmission des connaissances et ingénierie pédagogique, chansons personnalisées.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="formations-transmission.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Prestations</p>
  <h1>Prestations</h1>
  <p>Ce que Via Gnosis propose.</p>
</section>

<section class="rich">
  <p class="rich-lead">Former, conseiller, créer sur commande.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="blocks">
  <a href="formations.html" class="block block-link">
    <div class="block-media"><img src="pilier-formations.jpg" alt="Formations"></div>
    <div class="block-body"><h3>Formations</h3><p>Des formations-actions participatives, où chacun met les mains dans la matière : ateliers de création, formation pédagogique, jeune public.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="conseil.html" class="block block-link">
    <div class="block-media"><img src="echanger-conseil.jpg" alt="Conseil"></div>
    <div class="block-body"><h3>Conseil</h3><p>Transmission des connaissances et ingénierie pédagogique : vingt-huit ans d'expérience au service des organisations.</p>
      <span class="more">En savoir plus</span></div>
  </a>
  <a href="chanson-personnalisee.html" class="block block-link">
    <div class="block-media"><img src="musique-yeux-du-pere.jpg" alt="Chanson personnalisée"></div>
    <div class="block-body"><h3>Chanson personnalisée</h3><p>Une chanson écrite et composée pour une occasion particulière : un anniversaire, un cadeau original.</p>
      <span class="more">En savoir plus</span></div>
  </a>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Un projet en tête ?</h2>
    <p>Décrivez votre contexte et vos envies — nous verrons ensemble ce qui convient.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

page("chanson-personnalisee.html", "prestations",
  title='Chanson personnalisée — VIA GNOSIS',
  desc="Une chanson écrite et composée sur mesure pour une occasion particulière : anniversaire, cadeau original.",
  body_class='',
  body="""
<section class="page-banner">
  <img src="musique-bandeau.jpg" alt="">
</section>
<section class="page-head">
  <p class="crumb">Via Gnosis — Prestations</p>
  <h1>Chanson personnalisée</h1>
  <p>Une chanson écrite et composée pour une occasion particulière.</p>
</section>

<section class="rich">
  <p class="rich-lead">Offrir une chanson qui n'existe pour personne d'autre.</p>
  <p>Texte à rédiger.</p>
</section>

<section class="cta">
  <div class="cta-fracture" aria-hidden="true"></div>
  <div>
    <h2>Une chanson à offrir ?</h2>
    <p>Racontez-moi l'occasion et la personne — nous écrirons la suite.</p>
  </div>
  <a href="echanger.html" class="btn btn-fill">Échanger avec moi &nbsp;→</a>
</section>
""")

# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import os
    for p in PAGES:
        with open(p["fichier"], "w", encoding="utf-8") as f:
            f.write(rendu(p))
    print(f"{len(PAGES)} pages générées.")
