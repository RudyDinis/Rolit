from fltk import *


# Variable global
plateau = []

def charge_plateau_vide():
    centre_x = 100
    centre_y = 150
    rayon = 50

    for i in range(0, 8):
        for j in range(0, 8):
            cercle(centre_x, centre_y, rayon)
            plateau.append({'centre': (centre_x, centre_y), 'rayon': rayon, 'etat': None})
            centre_x += 100
        centre_y += 100
        centre_x = 100

    texte(900, 150, "Rouge : 0", tag="points")
    texte(900, 250, "Jaune : 0", tag="points")
    texte(900, 350, "Vert : 0", tag="points")
    texte(900, 450, "Bleu : 0", tag="points")

    return plateau