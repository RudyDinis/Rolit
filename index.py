#Bibliothèques
from fltk import *

#Fonctions
from fonctions.joueurs import ordre_joueur, calcul_points
from fonctions.pions import place_pion
from fonctions.plateau import charge_plateau_vide



# Variable global
plateau = []
ordre = []
points = {"Rouge": 0, "Jaune": 0, "Vert": 0, "Bleu": 0}

# création de la fenêtre initiale
cree_fenetre(1200, 900)

#Apelle le module ordre_joueur avec comme arg le nb de joueurs
ordre = ordre_joueur(4)
plateau = charge_plateau_vide(ordre) #charge le plateau

texte(250, 30, "Au tour du joueur : " + list(ordre[0].keys())[0], couleur="black", taille=40, tag="tour_joueur") # affiche le premier joueur



while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        plateau, ordre = place_pion(abscisse(ev), ordonnee(ev), plateau, ordre)
        points = calcul_points(plateau)
    elif tev == "Quitte": 
        break

    mise_a_jour()

ferme_fenetre()
