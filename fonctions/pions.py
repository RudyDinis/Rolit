from fltk import *

RAYON = 50


def remplissage(plateau, indice_ligne, indice, ordre, points):
    # Droite
    for i in range((7 - indice)):  # Tour des indices de droite
        current_index = i + indice + 1  # Indice actuel

        # Si la boucle passe sur un None on stop
        if plateau[indice_ligne][current_index]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[indice_ligne][current_index]['etat'] == list(ordre[0].keys())[0]:
            for j in range(indice + 1, current_index):
                x_centre, y_centre = plateau[indice_ligne][j]["centre"]
                plateau[indice_ligne][j]["etat"] = list(ordre[0].keys())[0]
                cercle(x_centre,y_centre,RAYON,remplissage=list(ordre[0].values())[0],tag=[x_centre, y_centre, RAYON],)




    ordre.append(ordre.pop(0))
    efface("tour_joueur")
    texte(90,10,"au tour du joueur : " + list(ordre[0].keys())[0],couleur="black",taille=40,tag="tour_joueur")

    return plateau, ordre, points


def place_pion(x_clic, y_clic, plateau, ordre, points):

    INDICE_LIGNE = ""
    INDICE = ""


    for indice_ligne, ligne in enumerate(plateau):
        for indice, cercle_info in enumerate(ligne):

            INDICE_LIGNE = indice_ligne
            INDICE = indice

            x_centre, y_centre = cercle_info["centre"]  # récupère les centre x, y depuis la variable plateau

            distance = ((x_clic - x_centre) ** 2 + (y_clic - y_centre) ** 2) ** 0.5  # Formule distance euclidienne

            if distance <= RAYON:
                if (list(ordre[0].keys())[0] != cercle_info["etat"]):  # Si le joueur clique sur une case qui ne lui appartient pas:
                    cercle(x_centre,y_centre,RAYON,remplissage=list(ordre[0].values())[0],tag=[x_centre, y_centre, RAYON],)

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

                    return remplissage(plateau, INDICE_LIGNE, INDICE, ordre, points)

            else: 
                pass
    return plateau, ordre, points 
