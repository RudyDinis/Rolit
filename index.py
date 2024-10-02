#Bibliothèques
import time
import random
from fltk import *

#Fonctions
from fonctions.plateau import charge_plateau_vide
from fonctions.ordre_joueur import ordre_joueur



# Variable global
plateau = []
ordre = []



# création de la fenêtre initiale
cree_fenetre(1200, 1200)


#plateau = charge_plateau_vide()
ordre = ordre_joueur(4)

print(ordre)


while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        x_clic, y_clic = abscisse(ev), ordonnee(ev)


        for cercle_info in plateau:
            x_centre, y_centre = cercle_info['centre'] #récupère les centre x, y depuis la variable plateau
            rayon = cercle_info['rayon'] #récupère le rayon depuis la variable plateau

            distance = ((x_clic - x_centre) ** 2 + (y_clic - y_centre) ** 2) ** 0.5 #Formule distance euclidienne
            if distance <= rayon:
                cercle(x_centre, y_centre, rayon, remplissage="red")
                cercle_info['etat'] = "R"

    elif tev == "Quitte": 
        break

    mise_a_jour()

ferme_fenetre()

