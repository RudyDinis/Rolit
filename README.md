Projet Rolit
(Si vous êtes sur vsc, utilisez le raccourci clavier Ctrl + Maj + V (ou Cmd + Shift + V sur macOS) pour ouvrir l'aperçu du fichier.)

## Fonctionnalités principales

- **Interface graphique** : Développée avec **FLTK**, elle offre une navigation simple et fluide entre les différents menus et le plateau de jeu.
- **Musique et effets sonores** : Gérés avec **Pygame**, pour ajouter une ambiance.
- **Modes de jeu** :
  - **Jouer en local** : Jusqu'à 4 joueurs peuvent s'affronter sur le même appareil.
  - **Jouer contre une IA** : Défiez une intelligence artificielle.
- **Menus complets** :
  - **Menu principal** : Accédez aux différents modes de jeu, coupez la musique.
  - **Menu sauvegarde** : Chargez une partie ou jouez une nouvelle.
  - **Menu choix des joueurs** : Configurez les participants (2 à 4 joueurs).


## Prérequis

Pour jouer à Rolit, vous aurez besoin de :

- **Python 3.x.x**
- **FLTK** pour l'interface graphique
- **Pygame** pour les musiques et sons

### Installation des dépendances

```bash
pip install pygame
```
pour fltk il faut se rendre sur le site de [Antoine Meyer](https://antoinemeyer.frama.io/fltk/)

### Lancement du jeu

aller dans le dossier de votre rolit:
```bash
cd ./rolit/
```

puis lancer le avec python :
```bash
python index.py
```

## Pour les developpeurs

### structure du projet

- **rolit/**
  - `index.py`  # Cœur du jeu
  - `fltk.py`  # Librairie graphique
  - **menu/**
    - `menu.py`  # Menu d'accueil du joueur
  - **jeu/**
    - `joueurs.py`  # Gère les points, le choix de l'ordre des joueurs
    - `nb_joueurs.py`  # Menu pour choisir le nombre de joueurs
    - `pions.py`  # Gère le placement des pions et le fait de manger
    - `plateau.py`  # Permet de charger le plateau quand on utilise une sauvegarde, ou d'en créer un nouveau
  - **assets/**
    - **img/**
      - `background.png`
      - `menu.png`
      - `musical.png`
      - `rectangle_noir.png`
      - `volume-mute.png`
    - `bouton.py`  # Classe permettant de gérer les boutons
    - `musique.mp3`
  - **sauvegarde/**
    - `save.py`  # Toute la partie sauvegarde du code, modifier, supprimer ou faire une nouvelle sauvegarde
    - `save.json`
  - `README.md`


## Crédits
### developpeurs :
  - DEBEURÉ TOM
  - DINIS RUDY
  - MECHRI YANIS

## Licence
GPL