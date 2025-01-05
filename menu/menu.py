import fltk
import pygame

from assets.bouton import Boutton

def affiche_menu():
    fltk.image(600, 460, './assets/img/menu.png', largeur=1200, hauteur=900)

    solo_button = Boutton(445, 340, 745, 480, font_size=50, tag='solo')
    ia_button = Boutton(445, 535, 745, 680, font_size=50, tag='ia')

    music_button = Boutton(1000, 715, 1100, 830, font_size=0, tag='settings')
    fltk.image(1030+20, 755+20, './assets/img/musical.png', largeur=100, hauteur=100, ancrage="center", tag="music_icon")


    fltk.mise_a_jour()
    return solo_button, ia_button, music_button

def music(bool):
    fltk.efface('music_icon')
    if bool == True:
        fltk.image(1030+20, 755+20, './assets/img/musical.png', largeur=100, hauteur=100, ancrage="center", tag="music_icon")
        pygame.mixer.music.unpause()
    else:
        fltk.image(1030+20, 755+20, './assets/img/volume-mute.png', largeur=100, hauteur=100, ancrage="center", tag="music_icon")
        pygame.mixer.music.pause()


    return bool
