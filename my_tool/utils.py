# Cette page contient des finctions utilitaire réutilisable

# Fonction qui récupère l'extension d'un fichier
def obtenir_extension(fichier):
    # Récupère l'extension et la convertit en minuscules
    extension = fichier.suffix.lower()

    # Retourne l'extension obtenue
    return extension