#Bibliothèques
import time
import random
from fltk import *

#Fonctions
from fonctions.plateau import charge_plateau_vide
from fonctions.ordre_joueur import ordre_joueur
from fonctions.pions import place_pion



# Variable global
plateau = []
ordre = []
points = {"Rouge": 0, "Jaune": 0, "Vert": 0, "Bleu": 0}



# création de la fenêtre initiale
cree_fenetre(1200, 1000)

#Apelle le module ordre_joueur avec comme arg le nb de joueurs
ordre = ordre_joueur(4)
plateau = charge_plateau_vide(ordre, points) #charge le plateau
print(plateau)

texte(90, 10, "au tour du joueur : " + list(ordre[0].keys())[0], couleur="black", taille=40, tag="tour_joueur") # affiche le premier joueur



while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        plateau, ordre, points = place_pion(abscisse(ev), ordonnee(ev), plateau, ordre, points)

    elif tev == "Quitte": 
        break

    mise_a_jour()

ferme_fenetre()

