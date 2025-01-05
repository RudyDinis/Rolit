from fltk import *

#Fonctions
from jeu.joueurs import calcul_points



# Variable global
RAYON = 50
plateau = []


def charge_fond():
    image(600, 460, './assets/img/background.png', largeur=1200, hauteur=900)


def middle(plateau, ordre):
    centres = [(3, 3), (3, 4), (4, 3), (4, 4)]

    for x, y in centres:
        x_centre, y_centre = plateau[x][y]['centre']
        cercle(
            x_centre, y_centre, 50,
            remplissage=list(ordre[0].values())[0],
            tag=[x_centre, y_centre, 50],
            couleur="white"
        )
        plateau[x][y]["etat"] = list(ordre[0].keys())[0]
        ordre.append(ordre.pop(0))


def charge_plateau_vide(ordre):
    charge_fond()
    centre_x = 100
    centre_y = 150

    for i in range(0, 8):
        ligne = []
        for j in range(0, 8):
            cercle(centre_x, centre_y, RAYON, couleur="white")
            ligne.append({'centre': (centre_x, centre_y), 'etat': None})
            centre_x += 100
        global plateau
        plateau.append(ligne)
        
        centre_y += 100
        centre_x = 100

    middle(plateau, ordre)

    texte(900, 150, "Rouge : 0", couleur="white", tag="points")
    texte(900, 250, "Jaune : 0", couleur="white", tag="points")
    texte(900, 350, "Vert : 0", couleur="white", tag="points")
    texte(900, 450, "Bleu : 0", couleur="white", tag="points")

    calcul_points(plateau)
    return plateau


def charge_plateau(data):
    charge_fond()
    centre_x = 100
    centre_y = 150

    plateau = []
    for i in range(8):
        ligne = []
        for j in range(8):
            ligne.append({'centre': (centre_x, centre_y), 'etat': None})
            centre_x += 100
        plateau.append(ligne)
        
        centre_y += 100
        centre_x = 100

    texte(900, 150, "Rouge : 0", couleur="white", tag="points")
    texte(900, 250, "Jaune : 0",couleur="white", tag="points")
    texte(900, 350, "Vert : 0",couleur="white", tag="points")
    texte(900, 450, "Bleu : 0",couleur="white", tag="points")

    placer_points(plateau, data)

    calcul_points(plateau)

    return plateau

def placer_points(plateau, data):
    """
    Met à jour le plateau avec les états des cases en fonction de data['plateau'].
    Cette fonction place également les points en fonction de data['points'].
    """
    for i in range(8):
        for j in range(8):
            case = plateau[i][j]
            etat = data['plateau'][i][j] 
            case['etat'] = etat['etat'] if etat else None 
            
            if case['etat'] == "Rouge":
                cercle(case['centre'][0], case['centre'][1], RAYON, couleur="white", remplissage="red")
            elif case['etat'] == "Jaune":
                cercle(case['centre'][0], case['centre'][1], RAYON, couleur="white", remplissage="yellow")
            elif case['etat'] == "Vert":
                cercle(case['centre'][0], case['centre'][1], RAYON, couleur="white", remplissage="green")
            elif case['etat'] == "Bleu":
                cercle(case['centre'][0], case['centre'][1], RAYON, couleur="white", remplissage="blue")
            else:
                cercle(case['centre'][0], case['centre'][1], RAYON, couleur="white")

    mise_a_jour()
    points = data['points']
    texte(900, 150, f"Rouge : {points['Rouge']}", tag="points", couleur="white")
    texte(900, 250, f"Jaune : {points['Jaune']}", tag="points", couleur="white")
    texte(900, 350, f"Vert : {points['Vert']}", tag="points", couleur="white")
    texte(900, 450, f"Bleu : {points['Bleu']}", tag="points", couleur="white")

    calcul_points(plateau)

    return plateau