from fltk import *


# Variable global
plateau = []


def middle(points, cercle_info, ordre):
    # récupère les centre x, y depuis la variable plateau
    x_centre, y_centre = cercle_info["centre"]
    cercle(x_centre,y_centre,50,remplissage=list(ordre[0].values())[0],tag=[x_centre, y_centre, 50])

    points[list(ordre[0].keys())[0]] += 1
    print("test")

    cercle_info["etat"] = list(ordre[0].keys())[0]
    ordre.append(ordre.pop(0))

    efface("tour_joueur")
    texte(90,10,"au tour du joueur : " + list(ordre[0].keys())[0],couleur="black",taille=40,tag="tour_joueur")

    efface("points")
    texte(900, 150, list(ordre[0].keys()) + str(list(ordre[0].values())), tag="points")

    return ordre, points, cercle_info

def charge_plateau_vide(ordre, points):
    centre_x = 100
    centre_y = 150
    rayon = 50

    for i in range(0, 8):
        ligne = []
        for j in range(0, 8):
            cercle(centre_x, centre_y, rayon)
            ligne.append({'centre': (centre_x, centre_y), 'rayon': rayon, 'etat': None})
            centre_x += 100
        plateau.append(ligne)
        
        centre_y += 100
        centre_x = 100

        # 27/28/35/36
    for indice, cercle_info in enumerate(plateau):
        print(indice)
        if indice == 27:
            ordre, points, cercle_info = middle(points, cercle_info, ordre)
            print(points)

    texte(900, 150, "Rouge : 0", tag="points")
    texte(900, 250, "Jaune : 0", tag="points")
    texte(900, 350, "Vert : 0", tag="points")
    texte(900, 450, "Bleu : 0", tag="points")

    return plateau, ordre, points
