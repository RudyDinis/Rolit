import fltk
from assets.bouton import Boutton

def charge_joueurs():
    fltk.image(600, 460, "./assets/img/background.png", largeur=1200, hauteur=900)
    fltk.texte(400, 30, "Nombre de joueurs", couleur="white", taille=40, tag="tour_joueur")

    page_width = 1200
    page_height = 900
    button_width = 100
    button_height = 80
    button_spacing = 50
    num_buttons = 3  # Nous avons 3 boutons, avec les numéros 2, 3, et 4

    total_buttons_width = (button_width * num_buttons) + (button_spacing * (num_buttons - 1))
    start_x = (page_width - total_buttons_width) // 2
    y_position = (page_height - button_height) // 2

    buttons = []

    for i in range(2, 5):  # Créez seulement les boutons 2, 3, et 4
        button_x_position = start_x + (i - 2) * (button_width + button_spacing)

        button = Boutton(
            button_x_position,
            y_position,
            button_x_position + button_width,
            y_position + button_height,
            font_size=15,
            tag=f"button_{i}",
            color="red",
        )
        buttons.append(button)

        text_x = button_x_position + button_width // 2
        text_y = y_position + button_height // 2
        fltk.texte(text_x, text_y, str(i), couleur="white", taille=20, tag=f"text_{i}", ancrage="center")

    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if tev == "ClicGauche":
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)

            for index, button in enumerate(buttons):
                if button.est_clique(x, y):
                    return index+2
        fltk.mise_a_jour()
