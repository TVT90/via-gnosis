# VIA GNOSIS — site web

Site statique publié via GitHub Pages : https://tvt90.github.io/via-gnosis/
Toutes les pages sont générées par `build.py` (gabarit commun) : on modifie le script, on régénère, on ne retouche jamais un HTML à la main.

## Architecture (figée le 6 octobre 2026)

Menu — un mot = une destination :
La source · L'atelier · Matérialiser · Prestations · Presse & agenda · Échanger

| Rubrique | Page | Sous-pages |
|---|---|---|
| Accueil | `index.html` | image plein écran + bouton « Entrer », sans défilement |
| La source | `la-source.html` | `la-demarche.html`, `le-fondateur.html`, `les-valeurs.html` |
| L'atelier | `atelier.html` | `atelier-musical.html`, `atelier-visuel.html` |
| Matérialiser | `materialiser.html` | `arts-visuels.html`, `musique.html`, `cahiers.html` |
| Prestations | `prestations.html` | `formations.html` (→ `creation-artistique.html`, `formation-pedagogique.html`, `ateliers-jeune-public.html`), `conseil.html` (→ `ingenierie-pedagogique.html`, `transmission-connaissances.html`), `chanson-personnalisee.html` |
| Presse & agenda | `presse-agenda.html` | articles en JPEG, 2 PDF à télécharger |
| Échanger | `echanger.html` | formulaire Formspree (identifiant mbgrzdga) |

La page La source présente 3 piliers : L'atelier, Matérialiser, Prestations.

## Règles pour les images

- Ses propres œuvres plutôt que des images génériques ; sujet lisible en vignette 280 px
- Aucun texte inscrit dans l'image, pas de personnification de l'IA en aura lumineuse, pas de scène surchargée
- Hero 16:9, piliers 1:1, bandeaux de page très panoramiques (cadrage ajusté par `object-position` dans style.css), blocs 4:3
- JPEG, moins de 300 Ko, noms sans accent ni espace
