import time
import random
from fltk import *

#Variables Globales
ordre = []
couleurs = [{"Rouge":"red"}, {"Vert":"green"}, {"Jaune":"yellow"}, {"Bleu":"blue"}]

def dessiner_de(face, decalage_x):
    # Dessiner le contour du dé (un carré) avec un zoom x10 et un décalage
    rectangle(100 + decalage_x, 100, 200 + decalage_x, 200, tag="ordre_joueur")

    # Rayon des points sur le dé, ajusté pour le zoom
    r = 5

    # Coordonnées des points pour chaque face du dé, avec un zoom x10
    faces = {
        1: [(50, 50)],
        2: [(30, 30), (70, 70)],
        3: [(30, 30), (50, 50), (70, 70)],
        4: [(30, 30), (30, 70), (70, 30), (70, 70)],
        5: [(30, 30), (30, 70), (70, 30), (70, 70), (50, 50)],
        6: [(30, 30), (30, 50), (30, 70), (70, 30), (70, 50), (70, 70)],
    }

    # Dessiner les points sur la face du dé spécifiée
    if face in faces:
        for (x, y) in faces[face]:
            cercle(x + decalage_x +100 , y+100, r, tag="nombre")
    mise_a_jour()

# Dessiner les 4 dés en ligne
def ordre_joueur(playerNB):
    ordre_temp = [0] * playerNB  # Initialiser une liste pour enregistrer le dernier nombre de chaque joueur
    
    for _ in range(6):
        efface("nombre")
        nombres_disponibles = [1, 2, 3, 4, 5, 6]
        for i in range(playerNB):
            nb = random.choice(nombres_disponibles)
            nombres_disponibles.remove(nb)

            dessiner_de(nb, i * 300)
            texte(i * 300 + 90, -10, list(couleurs[i].keys())[0], couleur="red", taille=40, tag="ordre_joueur")

            ordre_temp[i] = nb  
        time.sleep(1)
    for i in range(playerNB):
        min_value = min(ordre_temp)
        min_index = ordre_temp.index(min_value)
        ordre.append(couleurs.pop(min_index))
        ordre_temp.remove(min_value)


    time.sleep(3)
    efface("ordre_joueur")
    efface("nombre")
    return ordre
    

