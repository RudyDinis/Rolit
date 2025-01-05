import fltk

class Boutton:
    def __init__(self, pos_x, pos_y, taille_x, taille_y, font_size, tag='', texte='', color=""):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.font_size = font_size
        self.nom = tag
        self.texte = texte
        self.color = color

        fltk.rectangle(self.pos_x, self.pos_y, self.taille_x, self.taille_y, couleur=self.color, remplissage=self.color)
        if texte:
            fltk.texte(self.pos_x+120, self.pos_y+40, self.texte, taille=self.font_size, couleur="white", ancrage="center")
        

    def est_clique(self, souris_x, souris_y):
        if self.pos_x <= souris_x <= self.taille_x and self.pos_y <= souris_y <= self.taille_y:
            return True

    def obtenir_coordonnee(self):
        return self.pos_x, self.pos_y, self.taille_x, self.taille_y