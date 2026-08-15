# VIA GNOSIS — site web

Site statique publié via GitHub Pages : https://tvt90.github.io/via-gnosis/

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` | Page d'accueil — image plein écran + bouton « Explorer », sans défilement |
| `la-source.html` | Page pivot « Pourquoi Via Gnosis ? » — démarche, 4 piliers, projets |
| `creer.html` | Pilier Créer — arts visuels, musique, vidéo |
| `explorer.html` | Pilier Explorer — laboratoire, recherche |
| `transmettre.html` | Pilier Transmettre — les 5 formats de formation |
| `decouvrir.html` | Pilier Découvrir — l'univers, lien vers le site artiste |
| `rencontres.html` | Agenda, presse, partenaires |
| `echanger.html` | Contact |
| `style.css` | Feuille de style unique |
| `build.py` | Script de génération des 8 pages (non publié, outil de travail) |

## Images

| Fichier | Emplacement | Format |
|---|---|---|
| `hero-accueil.jpg` | Accueil, plein écran | 16:9 |
| `source-atelier.jpg` | En-tête La source / Échanger | 4:3 |
| `pilier-creer.jpg` | Vignette + en-tête Créer | 1:1 |
| `pilier-explorer.jpg` | Vignette + en-tête Explorer | 1:1 |
| `projet-couture.jpg` | Vignette projet Nova and I | 4:5 |
| `creer-couture.jpg` | Bloc Arts visuels | 4:3 |
| `logo.png` / `logo-light.png` | Logo (fond clair / fond sombre) | — |
| `favicon.png` | Icône d'onglet | 1:1 |

Le logo de l'en-tête est un tracé SVG intégré au code (net à toutes les tailles).

## Images restant à produire

- `pilier-transmettre.jpg` (1:1)
- `pilier-decouvrir.jpg` (1:1)
- Vignettes projets en 4:5

En attendant, ces emplacements utilisent des images du site artiste.

## Règles pour les nouvelles images

- Piliers : carré 1:1, export 1000×1000 px
- Projets : portrait 4:5, export 1000×1250 px
- Blocs : 4:3, export 1200×900 px
- JPEG, moins de 300 Ko
- Noms sans accent ni espace
- Aucune contrainte de composition : le texte ne se superpose plus aux images
