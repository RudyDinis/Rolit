from fltk import *


def remplissage(plateau, indice, ordre, points):
    cases_a_remplir = []
    largeur = 8  # Nombre de cases par ligne
    couleur = list(ordre[0].values())[0]

    # Décalage pour les directions (horizontale, verticale, diagonales)
    decalages = {
        "droite": 1,
        "gauche": -1,
        "bas": largeur,
        "haut": -largeur,
        "diagonale_bas_droite": largeur + 1,
        "diagonale_bas_gauche": largeur - 1,
        "diagonale_haut_droite": -(largeur - 1),
        "diagonale_haut_gauche": -(largeur + 1),
    }

    for direction, decalage in decalages.items():
        indice_courant = indice + decalage
        cases_a_remplir = []

        # Parcours dans la direction
        while 0 <= indice_courant < len(plateau):
            case = plateau[indice_courant]

            # Si une case est vide, on arrête (pas de remplissage possible)
            if case["etat"] is None:
                break

            # Si on trouve un pion de la même couleur, on remplit les cases collectées
            if case["etat"] == list(ordre[0].keys())[0]:
                for indice in cases_a_remplir:
                    plateau[indice]["etat"] = list(ordre[0].keys())[0]

                    # Mettre à jour l'affichage (optionnel)
                    x_centre, y_centre = plateau[indice]["centre"]
                    rayon = plateau[indice]["rayon"]
                    cercle(x_centre,y_centre,rayon,remplissage=couleur,tag=[x_centre, y_centre, rayon],)
                break

            # Sinon, on ajoute la case à remplir à la liste
            cases_a_remplir.append(indice_courant)

            # Passer à la case suivante dans la direction donnée
            indice_courant += decalage
    
    ordre.append(ordre.pop(0))
    efface("tour_joueur")
    texte(90,10,"au tour du joueur : " + list(ordre[0].keys())[0],couleur="black",taille=40,tag="tour_joueur")

    return plateau, points, ordre


def place_pion(x_clic, y_clic, plateau, ordre, points):
    for indice, cercle_info in enumerate(plateau):
        x_centre, y_centre = cercle_info["centre"]  # récupère les centre x, y depuis la variable plateau
        rayon = cercle_info["rayon"]  # récupère le rayon depuis la variable plateau

        distance = ((x_clic - x_centre) ** 2 + (y_clic - y_centre) ** 2) ** 0.5  # Formule distance euclidienne

        if distance <= rayon:
            if (list(ordre[0].keys())[0] != cercle_info["etat"]):  # Si le joueur clique sur une case qui ne lui appartient pas:
                cercle(x_centre,y_centre,rayon,remplissage=list(ordre[0].values())[0],tag=[x_centre, y_centre, rayon],)

                # Modification des points
                points[list(ordre[0].keys())[0]] += 1
                if cercle_info["etat"] != None:
                    points[cercle_info["etat"]] -= 1

                efface("points")
                texte(900, 150, "Rouge : " + str(points["Rouge"]), tag="points")
                texte(900, 250, "Jaune : " + str(points["Jaune"]), tag="points")
                texte(900, 350, "Vert : " + str(points["Vert"]), tag="points")
                texte(900, 450, "Bleu : " + str(points["Bleu"]), tag="points")

                # change l'etat de notre case
                cercle_info["etat"] = list(ordre[0].keys())[0]
                break
    return remplissage(plateau, indice, ordre, points)
