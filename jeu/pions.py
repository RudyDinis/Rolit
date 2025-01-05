from fltk import *

from jeu.joueurs import recupere_points

RAYON = 50


def remplissage(plateau, indice_ligne, indice_colonne, ordre):
    remplissage_effectue = False
    
    # Gauche a Droite
    for i in range((7 - indice_colonne)):  # Tour des indices de droite
        current_index = i + indice_colonne + 1  # Indice actuel

        # Si la boucle passe sur un None on stop
        if plateau[indice_ligne][current_index]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[indice_ligne][current_index]['etat'] == list(ordre[0].keys())[0]:
            for j in range(indice_colonne + 1, current_index):

                x_centre, y_centre = plateau[indice_ligne][j]["centre"]
                plateau[indice_ligne][j]["etat"] = list(ordre[0].keys())[0]
                cercle(x_centre,y_centre,RAYON,remplissage=list(ordre[0].values())[0],tag=[x_centre, y_centre, RAYON],)
                remplissage_effectue = True  # Un espace a été rempli


    # Droite a Gauche 
    for i in range(indice_colonne , -1, -1):  # Parcours à partir de l'indice jusqu'à 0
        current_index = i  # Indice actuel

        # Si la boucle passe sur un None on stop
        if plateau[indice_ligne][current_index]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[indice_ligne][current_index]['etat'] == list(ordre[0].keys())[0]:
            for j in range(indice_colonne - 1, current_index, -1):  # On parcourt de l'indice vers le current_index

                x_centre, y_centre = plateau[indice_ligne][j]["centre"]
                plateau[indice_ligne][j]["etat"] = list(ordre[0].keys())[0]
                cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                remplissage_effectue = True  # Un espace a été rempli


    # Bas en Haut
    for i in range(indice_ligne, -1, -1):  # Parcours à partir de l'indice vers 0
        current_index = i  # Indice actuel dans la colonne

        # Si la boucle passe sur un None, on stop
        if plateau[current_index][indice_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index][indice_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(current_index + 1, indice_ligne):  # Parcours de l'indice vers l'indice_ligne

                x_centre, y_centre = plateau[j][indice_colonne]["centre"]
                plateau[j][indice_colonne]["etat"] = list(ordre[0].keys())[0]
                cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                remplissage_effectue = True  # Un espace a été rempli


    # Haut en Bas
    for i in range(indice_ligne, len(plateau)):  # Parcours du sommet vers le bas
        current_index = i  # Indice actuel dans la colonne

        # Si la boucle passe sur un None, on stop
        if plateau[current_index][indice_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index][indice_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(indice_ligne + 1, current_index):  # On parcourt de l'indice_ligne à l'indice actuel

                x_centre, y_centre = plateau[j][indice_colonne]["centre"]
                plateau[j][indice_colonne]["etat"] = list(ordre[0].keys())[0]
                cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                remplissage_effectue = True  # Un espace a été rempli


    #Diagonale Haut à Droite
    for i in range(indice_ligne, -1, -1):  # Parcours de haut en bas de la ligne
        current_index_ligne = i  # Indice de la ligne actuelle
        current_index_colonne = indice_colonne + (indice_ligne - i)  # Parcours de droite à gauche pour la colonne

        if current_index_colonne >= len(plateau[0]) or current_index_colonne < 0:
            break  # On sort si la colonne dépasse les limites du plateau

        # Si la boucle rencontre un None, on arrête
        if plateau[current_index_ligne][current_index_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index_ligne][current_index_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(current_index_ligne + 1, indice_ligne):  # On parcourt de l'indice actuel à l'indice de départ
                new_ligne = j
                new_colonne = indice_colonne + (indice_ligne - j)
                if new_colonne < len(plateau[0]) and new_colonne >= 0:
                    x_centre, y_centre = plateau[new_ligne][new_colonne]["centre"]
                    plateau[new_ligne][new_colonne]["etat"] = list(ordre[0].keys())[0]
                    cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                    remplissage_effectue = True  # Un espace a été rempli

    #Diagonale Haut à Gauche
    for i in range(indice_ligne, -1, -1):  # Parcours de haut en bas de la ligne
        current_index_ligne = i  # Indice de la ligne actuelle
        current_index_colonne = indice_colonne - (indice_ligne - i)  # Parcours de gauche à droite pour la colonne

        if current_index_colonne < 0:  # Sortir si la colonne dépasse les limites
            break

        # Si la boucle rencontre un None, on arrête
        if plateau[current_index_ligne][current_index_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index_ligne][current_index_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(current_index_ligne + 1, indice_ligne):  # On parcourt de l'indice actuel à l'indice de départ
                new_ligne = j
                new_colonne = indice_colonne - (indice_ligne - j)
                if new_colonne >= 0:
                    x_centre, y_centre = plateau[new_ligne][new_colonne]["centre"]
                    plateau[new_ligne][new_colonne]["etat"] = list(ordre[0].keys())[0]
                    cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                    remplissage_effectue = True  # Un espace a été rempli

    #Diagonale Bas à Droite
    for i in range(indice_ligne, len(plateau)):  # Parcours du bas vers le haut
        current_index_ligne = i  # Indice de la ligne actuelle
        current_index_colonne = indice_colonne + (i - indice_ligne)  # Parcours vers la droite pour la colonne

        if current_index_colonne >= len(plateau[0]):  # Sortir si la colonne dépasse les limites
            break

        # Si la boucle rencontre un None, on arrête
        if plateau[current_index_ligne][current_index_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index_ligne][current_index_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(current_index_ligne - 1, indice_ligne, -1):  # On parcourt de l'indice actuel à l'indice de départ
                new_ligne = j
                new_colonne = indice_colonne + (j - indice_ligne)
                if new_colonne < len(plateau[0]):
                    x_centre, y_centre = plateau[new_ligne][new_colonne]["centre"]
                    plateau[new_ligne][new_colonne]["etat"] = list(ordre[0].keys())[0]
                    cercle(x_centre, y_centre, RAYON,remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                    remplissage_effectue = True  # Un espace a été rempli

    #Diagonale Bas à Gauche
    for i in range(indice_ligne, len(plateau)):  # Parcours du bas vers le haut
        current_index_ligne = i  # Indice de la ligne actuelle
        current_index_colonne = indice_colonne - (i - indice_ligne)  # Parcours vers la gauche pour la colonne

        if current_index_colonne < 0:  # Sortir si la colonne dépasse les limites
            break

        # Si la boucle rencontre un None, on arrête
        if plateau[current_index_ligne][current_index_colonne]['etat'] == None:
            break

        # Si la boucle rencontre un pion de la même couleur alors on change les pions entre
        if plateau[current_index_ligne][current_index_colonne]['etat'] == list(ordre[0].keys())[0]:
            for j in range(current_index_ligne - 1, indice_ligne, -1):  # On parcourt de l'indice actuel à l'indice de départ
                new_ligne = j
                new_colonne = indice_colonne - (j - indice_ligne)
                if new_colonne >= 0:
                    x_centre, y_centre = plateau[new_ligne][new_colonne]["centre"]
                    plateau[new_ligne][new_colonne]["etat"] = list(ordre[0].keys())[0]
                    cercle(x_centre, y_centre, RAYON, remplissage=list(ordre[0].values())[0], tag=[x_centre, y_centre, RAYON])
                    remplissage_effectue = True  # Un espace a été rempli


    nb_points = recupere_points(plateau, list(ordre[0].keys())[0])

    if remplissage_effectue == True:
        ordre.append(ordre.pop(0))
        efface("tour_joueur")
        texte(250,30,"Au tour du joueur : " + list(ordre[0].keys())[0],couleur="white" ,taille=40,tag="tour_joueur")
        return plateau, ordre, remplissage_effectue
    elif remplissage_effectue == False:
        if nb_points <= 1:
            ordre.append(ordre.pop(0))
            efface("tour_joueur")
            texte(250,30,"Au tour du joueur : " + list(ordre[0].keys())[0],couleur="white" ,taille=40,tag="tour_joueur")
            return plateau, ordre, "ok"
        else:
            return plateau, ordre, remplissage_effectue
    


def place_pion(x_clic, y_clic, plateau, ordre):
    temp_plateau = plateau
    temp_ordre = ordre

    INDICE_LIGNE = ""

    for indice_ligne, ligne in enumerate(temp_plateau):
        for indice_colonne, cercle_info in enumerate(ligne):

            INDICE_LIGNE = indice_ligne
            INDICE_COLONE = indice_colonne

            x_centre, y_centre = cercle_info["centre"]  # récupère les centre x, y depuis la variable plateau
            distance = ((x_clic - x_centre) ** 2 + (y_clic - y_centre) ** 2) ** 0.5  # Formule distance euclidienne

            if distance <= RAYON:
                if (cercle_info["etat"] == None):  # Si le joueur clique sur une case qui ne lui appartient pas:
                    cercle_info["etat"] = list(ordre[0].keys())[0]
                    plateau, ordre, remplissage_effectue = remplissage(temp_plateau, INDICE_LIGNE, INDICE_COLONE, temp_ordre)

                    if remplissage_effectue == True:
                        cercle(x_centre,y_centre,RAYON,remplissage=list(ordre[-1].values())[0],tag=[x_centre, y_centre, RAYON])
                        return plateau, ordre
                    elif remplissage_effectue == "ok":
                        cercle(x_centre,y_centre,RAYON,remplissage=list(ordre[-1].values())[0],tag=[x_centre, y_centre, RAYON])
                        return plateau, ordre
                    elif remplissage_effectue == False:
                        cercle_info["etat"] = None
                        return temp_plateau, temp_ordre
                    

                    

            else: 
                pass
    return temp_plateau, temp_ordre 
