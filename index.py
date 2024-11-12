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
points = {"Rouge": 0, "Jaune": 0, "Vert": 0, "Bleu": 0}



# création de la fenêtre initiale
cree_fenetre(1200, 1000)

#Apelle le module ordre_joueur avec comme arg le nb de joueurs
ordre = ordre_joueur(4)
plateau = charge_plateau_vide() #charge le plateau
texte(90, 10, "au tour du joueur : " + list(ordre[0].keys())[0], couleur="black", taille=40, tag="tour_joueur") # affiche le premier joueur





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
                if list(ordre[0].keys())[0] != cercle_info['etat']: #Si le joueur clique sur une case qui ne lui appartient pas:
                    cercle(x_centre, y_centre, rayon, remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, rayon])
                    #Modification des points
                    points[list(ordre[0].keys())[0]] += 1
                    if cercle_info['etat'] != None:
                        points[cercle_info['etat']] -= 1
                    efface("points")
                    texte(900, 150, "Rouge : " + str(points["Rouge"]), tag="points")
                    texte(900, 250, "Jaune : " + str(points["Jaune"]), tag="points")
                    texte(900, 350, "Vert : " + str(points["Vert"]), tag="points")
                    texte(900, 450, "Bleu : " + str(points["Bleu"]), tag="points")

                    #change l'etat de notre case
                    cercle_info['etat'] = list(ordre[0].keys())[0]
                    #changement de l'ordre
                    ordre.append(ordre.pop(0))
                    efface("tour_joueur")
                    texte(90, 10, "au tour du joueur : " + list(ordre[0].keys())[0], couleur="black", taille=40, tag="tour_joueur")


    elif tev == "Quitte": 
        break

    mise_a_jour()

ferme_fenetre()

