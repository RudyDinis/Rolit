from fltk import *

#Fonctions
from fonctions.joueurs import calcul_points



# Variable global
RAYON = 50
plateau = []


def middle(plateau, ordre):
    centres = [(3, 3), (3, 4), (4, 3), (4, 4)]

    for x, y in centres:
        x_centre, y_centre = plateau[x][y]['centre']
        cercle(
            x_centre, y_centre, 50,
            remplissage=list(ordre[0].values())[0],
            tag=[x_centre, y_centre, 50]
        )
        plateau[x][y]["etat"] = list(ordre[0].keys())[0]
        ordre.append(ordre.pop(0))





def charge_plateau_vide(ordre):
    centre_x = 100
    centre_y = 150

    for i in range(0, 8):
        ligne = []
        for j in range(0, 8):
            cercle(centre_x, centre_y, RAYON)
            ligne.append({'centre': (centre_x, centre_y), 'etat': None})
            centre_x += 100
        global plateau
        plateau.append(ligne)
        
        centre_y += 100
        centre_x = 100

        # 27/28/35/36

    middle(plateau, ordre)

    texte(900, 150, "Rouge : 0", tag="points")
    texte(900, 250, "Jaune : 0", tag="points")
    texte(900, 350, "Vert : 0", tag="points")
    texte(900, 450, "Bleu : 0", tag="points")

    calcul_points(plateau)
    return plateau
