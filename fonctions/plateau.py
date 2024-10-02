from fltk import *


# Variable global
plateau = []

def charge_plateau_vide():
    centre_x = 125
    centre_y = 62.5
    rayon = 62.5

    for i in range(0, 8):
        for j in range(0, 8):
            cercle(centre_x, centre_y, rayon)
            plateau.append({'centre': (centre_x, centre_y), 'rayon': rayon, 'etat': None})
            centre_x += 125
        centre_y += 125
        centre_x = 125
    return plateau