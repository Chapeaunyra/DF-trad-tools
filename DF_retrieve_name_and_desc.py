import os
import re
import json

# Définir le chemin du dossier à parcourir
dossier_jeu = "C:\\SCRIPTS\\trad dwarf fortress\\Traduction_Dwarft_Fortress-main\\vanilla_creatures"

# Définir un dictionnaire pour stocker les données
donnees_objets = {}

# Fonction pour extraire le titre d'un objet
def extraire_titre(fichier):
    with open(fichier, "r", encoding="ISO-8859-1") as f:
        contenu = f.read()
        return contenu

print("Début de l'extraction...")

# Parcourir le dossier du jeu
for repertoire, sous_repertoires, fichiers in os.walk(os.path.join(dossier_jeu, "objects")):
    for fichier in fichiers:
        chemin_fichier = os.path.join(repertoire, fichier)
        objet_data = extraire_titre(chemin_fichier)
        
        match_name = re.search(r"\[NAME:(.*):(.*):(.*?)\]", objet_data)
        match_description = re.search(r"\[DESCRIPTION:(.*?)\]", objet_data)

        if match_name and match_description:
            singular, plural, adjective = match_name.group(1), match_name.group(2), match_name.group(3)
            donnees_objets[fichier] = {
                "NAME": {
                    "singular": singular,
                    "plural": plural,
                    "adjective": adjective
                },
                "DESCRIPTION": match_description.group(1)
            }
            print(f"Extraction du fichier : {fichier}")

# Écrire les données dans un fichier JSON
with open("donnees_objets.json", "w", encoding="utf-8") as json_file:
    json.dump(donnees_objets, json_file, indent=4, ensure_ascii=False)

print("Extraction terminée. Les données ont été enregistrées dans 'donnees_objets.json'.")
