from pathlib import Path
import shutil
from my_tool.utils import obtenir_extension

# Cette fonction cherche et catégorise les fichiers
def organiser_dossier(chemin_dossier):
    # Transforme le chemin reçu en objet Path
    dossier = Path(chemin_dossier)

    # Vérifie si le dossier existe réellement
    if not dossier.exists():
        print("❌ Le dossier n'existe pas.")
        return

    # Vérifie que le chemin correspond bien à un dossier
    if not dossier.is_dir():
        print("❌ Le chemin indiqué n'est pas un dossier.")
        return

    print("✅ Dossier trouvé !")
    print("Dossier à organiser :", dossier)

    # Définit les catégories et leurs extensions
    categories = {
        "documents": [".pdf", ".docx", ".txt"],
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "musiques": [".mp3", ".wav", ".aiff"]
    }

    # Parcourt les éléments présents dans le dossier
    for fichier in dossier.iterdir():

        # Vérifie si l'élément est bien un fichier
        if fichier.is_file():
            print("Fichier trouvé :", fichier)

            # Récupère l'extension du fichier
            extension = obtenir_extension(fichier)
            print("Extension :", extension)

            # Indique si une catégorie a été trouvée
            categorie_trouvee = False

            # Parcourt les différentes catégories
            for categorie, extensions in categories.items():

                # Vérifie si l'extension appartient à cette catégorie
                if extension in extensions:
                    categorie_trouvee = True

                    print("Catégorie :", categorie)

                    # Crée le chemin du dossier correspondant à la catégorie
                    dossier_categorie = dossier / categorie

                    # Crée le dossier s'il n'existe pas encore
                    dossier_categorie.mkdir(exist_ok=True)

                    # Déplace le fichier
                    deplacer_fichier(fichier, dossier_categorie)

                    # La catégorie a été trouvée, inutile de continuer
                    break

            # Si aucune catégorie n'a été trouvée
            if not categorie_trouvee:
                categorie = "autres"

                print("Catégorie :", categorie)

                # Crée le dossier "autres"
                dossier_categorie = dossier / categorie
                dossier_categorie.mkdir(exist_ok=True)

                # Déplace le fichier
                deplacer_fichier(fichier, dossier_categorie)


# Fonction pour déplacer les fichiers
def deplacer_fichier(fichier, dossier_categorie):

    # Crée le chemin complet de destination
    destination = dossier_categorie / fichier.name

    # Vérifie si un fichier du même nom existe déjà
    if destination.exists():

        print(f"⚠️ Le fichier '{fichier.name}' existe déjà.")
        reponse = input("Voulez-vous le remplacer ? (oui/annuler) : ")

        # Vérifie la réponse de l'utilisateur
        if reponse.strip().lower() != "oui":
            print("❌ Remplacement annulé.")
            return

    try:
        # Déplace le fichier vers sa destination
        shutil.move(fichier, destination)

        print("✅ Fichier déplacé vers :", destination)

    except Exception as erreur:
        # Affiche l'erreur rencontrée
        print("❌ Erreur lors du déplacement :", erreur)


# Appel de la fonction
# print(Path.cwd()) permet de connaître le dossier de travail actuel

# Execute le programme uniquement si ce fichier est lancé directement

if __name__ == "__main__":
        organiser_dossier("../A_trier")

# __name__ est une variable spéciale de python