import os
import re
import json
import argparse

# Fonction pour extraire le titre d'un objet
def extraire_titre(fichier):
    with open(fichier, "r", encoding="ISO-8859-1") as f:
        contenu = f.read()
        return contenu

def extraire_donnees(repertoire, fichier):
    # Définir un dictionnaire pour stocker les données
    donnees_objets = {}

    chemin_fichier = os.path.join(repertoire, fichier)
    objet_data = extraire_titre(chemin_fichier)

    matches_name = re.findall(r"\[NAME:(.*):(.*):(.*?)\]", objet_data)
    matches_description = re.findall(r"\[DESCRIPTION:(.*?)\]", objet_data)

    #if matches_name and matches_description:
    name_data = []
    for match_name in matches_name:
        singular, plural, adjective = match_name
        if(singular.find("][NAME_PLURAL")):
            singular = singular.replace("][NAME_PLURAL", "")
        if(plural.find("][ADJ")):
            plural = singular.replace("][ADJ", "")

        name_data.append({
            "singular": singular,
            "plural": plural,
            "adjective": adjective
        })

    # Initialiser les valeurs pour "en-EN" et "fr-FR"
    if(matches_description and matches_name):
        donnees_objets[fichier] = {
                "en-EN": {
                    "NAME": name_data,
                    "DESCRIPTION": matches_description
                },
                "fr-FR": {
                    "NAME": [{
                        "singular": "",
                        "plural": "",
                        "adjective": ""
                    }],
                    "DESCRIPTION": [""]
                }
        }
    elif(matches_name):
        donnees_objets[fichier] = {
                "en-EN": {
                    "NAME": name_data
                },
                "fr-FR": {
                    "NAME": [{
                        "singular": "",
                        "plural": "",
                        "adjective": ""
                    }]
                }
        }
    elif(matches_description):
        donnees_objets[fichier] = {
                "en-EN": {
                    "DESCRIPTION": matches_description
                },
                "fr-FR": {
                    "DESCRIPTION": [""]
                }
        }
    else:
        donnees_objets[fichier] = {}

    return donnees_objets

def enregistrer_donnees_en_json(donnees, nom_fichier):
    # Écrire les données dans un fichier JSON
    with open(nom_fichier, "w", encoding="utf-8") as json_file:
        json.dump(donnees, json_file, indent=4, ensure_ascii=False)
    print("Extraction terminée. Les données ont été enregistrées dans '{}'.".format(nom_fichier))

def definir_nom_fichier(args):
    if(args.dossier_jeu.find('/') != -1):
        return args.dossier_jeu.rsplit('/', 1)[-1] + ".json"
    elif(args.dossier_jeu.find('\\') != -1):
        return args.dossier_jeu.rsplit('\\', 1)[-1] + ".json"
    else:
        return "data.json"

def main():
    parser = argparse.ArgumentParser(description="Extraction de données depuis un dossier de jeu.")
    parser.add_argument("dossier_jeu", help="Chemin du dossier du jeu à analyser")

    args = parser.parse_args()

    if not args.dossier_jeu:
        parser.error("Le chemin du dossier du jeu est obligatoire. Utilisez -h pour obtenir de l'aide.")

    dossier_jeu = args.dossier_jeu
    data = {}
    for repertoire, sous_repertoires, fichiers in os.walk(os.path.join(dossier_jeu, "objects")):
        for fichier in fichiers:
            print("Début de l'extraction. Les données sont recherché dans "+ fichier)
            donnees_objets = extraire_donnees(repertoire, fichier)
            data.update(donnees_objets)

    enregistrer_donnees_en_json(data, definir_nom_fichier(args))

if __name__ == "__main__":
    main()
