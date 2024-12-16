import fltk

fltk.cree_fenetre(1200, 900)



def affiche_menu():


affiche_menu()

while True:
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)

    if tev == "ClicGauche":
        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
        
    if tev == "Quitte":
        break
    
    fltk.mise_a_jour()
