import fltk
import json
from datetime import datetime

#Imports
from assets.bouton import Boutton


def new_save(plateau, ordre, points):
    date = datetime.now()
    date_formatee = date.strftime("%d/%m/%Y %H:%M:%S")

    data = {"id": date_formatee, "plateau": plateau, "ordre": ordre, "points": points}

    fichier_sauvegarde = "./sauvegarde/save.json"
    sauvegardes = []

    try:
        with open(fichier_sauvegarde, "r", encoding="utf-8") as f:
            contenu = json.load(f)
            if isinstance(contenu, list):
                sauvegardes = contenu
            else:
                print("Fichier JSON corrompu. Réinitialisation en tant que liste.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Aucun fichier ou fichier vide. Création d'une nouvelle liste.")

    sauvegardes.append(data)

    with open(fichier_sauvegarde, "w", encoding="utf-8") as f:
        json.dump(sauvegardes, f, indent=4, ensure_ascii=False)

    return date_formatee


def list_last_saves():
    fichier_sauvegarde = "./sauvegarde/save.json"

    try:
        with open(fichier_sauvegarde, "r", encoding="utf-8") as f:
            sauvegardes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    try:
        sauvegardes_triees = sorted(
            sauvegardes,
            key=lambda x: datetime.strptime(x["id"], "%d/%m/%Y %H:%M:%S"),
            reverse=True,
        )
    except KeyError:
        print("Format de sauvegarde incorrect. Certaines entrées sont manquantes.")
        return []

    ids = [sauvegarde["id"] for sauvegarde in sauvegardes_triees[:3]]
    return ids


def get_save():
    try:
        with open("./sauvegarde/save.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def get_data_by_id(id_sauvegarde):
    with open("./sauvegarde/save.json", "r", encoding="utf-8") as f:
        sauvegardes = json.load(f)

    for sauvegarde in sauvegardes:
        if sauvegarde["id"] == id_sauvegarde:
            return sauvegarde
    return None


def edit_save(plateau, ordre, points, date_formatee):
    sauvegardes = get_save()

    data = {"plateau": plateau, "ordre": ordre, "points": points}

    for sauvegarde in sauvegardes:
        if sauvegarde.get("id") == date_formatee:
            sauvegarde.update(data)
            break
    else:
        print("Aucune sauvegarde trouvée avec cette date.")
        return

    with open("./sauvegarde/save.json", "w", encoding="utf-8") as f:
        json.dump(sauvegardes, f, indent=4, ensure_ascii=False)


def save_loader():
    last_save = list_last_saves()
    fltk.image(600, 460, "./assets/img/background.png", largeur=1200, hauteur=900)

    x_position = 200
    y_position = 200
    button_width = 230
    button_height = 80
    x_offset = 250

    boutons_sauvegarde = []

    for idx, save_id in enumerate(last_save):
        button_x_position = x_position + (idx * x_offset)

        New_save = Boutton(
            button_x_position,
            y_position,
            button_x_position + button_width,
            y_position + button_height,
            font_size=15,
            tag="save",
            texte=save_id,
            color="red",
        )

        boutons_sauvegarde.append(New_save)

    new_game = Boutton(
        450,
        310,
        680,
        390,
        font_size=15,
        tag="save",
        texte="Nouvelle Partie",
        color="red",
    )

    return boutons_sauvegarde, new_game


def supprimer_sauvegarde(id):
    """
    Supprime une sauvegarde du tableau 'sauvegardes' en fonction de l'ID.
    """
    sauvegardes = get_save()
    for i, sauvegarde in enumerate(sauvegardes):
        if sauvegarde["id"] == id:
            del sauvegardes[i]
            with open("./sauvegarde/save.json", "w", encoding="utf-8") as f:
                json.dump(sauvegardes, f, ensure_ascii=False, indent=4)
            return sauvegardes
    return sauvegardes
