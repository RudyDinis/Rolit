#Bibliotèques
import fltk
import pygame

#Imports
from menu.menu import affiche_menu, music
from random import *
from jeu.joueurs import ordre_joueur, calcul_points
from jeu.pions import place_pion
from jeu.plateau import charge_plateau_vide, charge_plateau
from jeu.nb_joueurs import charge_joueurs

from sauvegarde.save import new_save, save_loader, get_data_by_id, supprimer_sauvegarde

#constante ia
ordre_ia=[{'Rouge': 'red'}, {'Jaune': 'yellow'}]


#variable global
solo_button = None
ia_button = None
music_button = None
musicbool = True
button_save = None
new_game_button = None


page = "menu"

plateau = []
ordre = []
points = {"Rouge": 0, "Jaune": 0, "Vert": 0, "Bleu": 0}

game_id = ""


#Initialisation
fltk.cree_fenetre(1200, 900)
solo_button,ia_button,music_button = affiche_menu()
fltk.mise_a_jour()

pygame.mixer.init()
pygame.mixer.music.load("./assets/musique.mp3")
pygame.mixer.music.play(-1)

while True:
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)

    if tev == "ClicGauche":
        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
        if page == "menu":
            if ia_button.est_clique(x,y): #bouton IA
                fltk.efface_tout()
                    
                page ="ia_mode"
                nb_joueur = 2
                ordre = ordre_ia
                plateau = charge_plateau_vide(ordre)
                fltk.texte(250, 30, "Au tour du joueur : " + list(ordre[0].keys())[0], couleur="white", taille=40, tag="tour_joueur")
                page ="jeu_ia"
                
            if solo_button.est_clique(x, y):  # Bouton Solo
                fltk.efface_tout()
                button_save, new_game_button = save_loader()

                if button_save == []:
                    page = "charge_joueurs"
                    nb_joueur = charge_joueurs

                    ordre = ordre_joueur(nb_joueur)
                    plateau = charge_plateau_vide(ordre)
                    fltk.texte(250, 30, "Au tour du joueur : " + list(ordre[0].keys())[0], couleur="white", taille=40, tag="tour_joueur")
                    page = "jeu"
                    game_id = new_save(plateau, ordre, points)

            try :
                for button in button_save:
                    if button.est_clique(x, y):
                        data = get_data_by_id(button.texte)
                        if data:
                            fltk.efface_tout()
                            ordre = data["ordre"]
                            plateau = charge_plateau(data)
                            page = "jeu" 
                            game_id = button.texte
                            fltk.texte(250, 30, "Au tour du joueur : " + list(ordre[0].keys())[0], couleur="white", taille=40, tag="tour_joueur")
            except:
                pass

            if music_button.est_clique(x, y):  # Bouton Music
                musicbool = music(not(musicbool))

            try :
                if new_game_button.est_clique(x, y): 
                    fltk.efface_tout()

                    page = "charge_joueurs"
                    nb_joueur = charge_joueurs()

                    ordre = ordre_joueur(nb_joueur)
                    plateau = charge_plateau_vide(ordre)
                    fltk.texte(250, 30, "Au tour du joueur : " + list(ordre[0].keys())[0], couleur="white", taille=40, tag="tour_joueur")
                    page = "jeu"
                    game_id = new_save(plateau, ordre, points)
            except:
                pass

        elif page == "jeu":
            plateau, ordre = place_pion(x, y, plateau, ordre)
            points = calcul_points(plateau)
            
            supprimer_sauvegarde(game_id)
            game_id = new_save(plateau, ordre, points)

        elif page == "jeu_ia":
            while ordre[0]=={'Jaune': 'yellow'}:
                x=randint(0,800)
                y=randint(0,800)
                plateau, ordre = place_pion(x, y, plateau, ordre)
                points = calcul_points(plateau)
            else:
                plateau, ordre = place_pion(x, y, plateau, ordre)
                points = calcul_points(plateau)
            

    if tev == "Quitte":
        break

    fltk.mise_a_jour()
