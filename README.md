Bien sûr ! Voici le même texte au format Markdown :

markdown

# Scripts d'extraction de données depuis Dwarf Fortress

## Introduction
Ces scripts ont été créés pour extraire des données spécifiques à partir du jeu Dwarf Fortress et les stocker dans un format JSON. Dwarf Fortress est un jeu complexe avec une grande quantité de contenu, y compris des noms d'objets et des descriptions. Ces scripts vous permettent de collecter ces informations pour une utilisation ultérieure, telles que la traduction du jeu dans différentes langues.

## Objectifs
Les principaux objectifs de ces scripts sont les suivants :
1. Extraire les noms et les descriptions d'objets à partir des fichiers de données du jeu Dwarf Fortress.
2. Organiser ces données dans une structure JSON pour une utilisation future.
3. Permettre de spécifier le chemin du dossier du jeu en tant que paramètre d'entrée.
4. Générer un fichier JSON contenant les données collectées.

## Informations Complémentaires

**Limitations des Balises** : Ces scripts ne gèrent QUE les informations liées à deux balises spécifiques :
- [NAME]
- [DESCRIPTION]

Cela est réalisé grâce à deux lignes de code dans les scripts :
```python
matches_name = re.findall(r"\[NAME:(.*):(.*):(.*?)\]", objet_data)
matches_description = re.findall(r"\[DESCRIPTION:(.*?)\]", objet_data)
```

Vous avez la possibilité de modifier ce comportement en personnalisant la méthode nommée **extraire_donnees(repertoire, fichier)** qui traite l'extraction des données depuis les fichiers. Pour cela, il est essentiel de s'assurer que les hypothèses de base sont vérifiées, à savoir que la balise [NAME] existe dans le fichier ET qu'elle soit présente en plus grand nombre.

Si vous avez une connaissance avancée du jeu et des données que vous souhaitez extraire, vous pouvez également envisager de découper l'extraction par balise en externalisant ces opérations dans des sous-méthodes avant de construire votre structure JSON.

## Exemples d'utilisation

### Script 1 - Extraction de données depuis un dossier du jeu
```shell
python DF_retrieve_name_and_desc_v2.py "Chemin/Vers/Le/Dossier/De/Traduction"
```
Cela exécutera le script 1 pour extraire les données à partir du dossier spécifié et générer un fichier JSON nommé d'après le dossier.


### Script 2 - Extraction de données depuis un dossier parent
```shell
python DF_retrieve_name_and_desc_v3.py "Chemin/Vers/Le/Dossier/Parent"
```
Ce script parcourra tous les sous-dossiers du dossier parent à la recherche de données. Il générera un fichier JSON à partir des données collectées, en utilisant le nom du dernier sous-dossier trouvé comme nom de fichier.


## Axes d'amélioration

    Gestion des erreurs : Les scripts actuels supposent que les fichiers de données sont au format attendu. Une meilleure gestion des erreurs serait bénéfique pour gérer les cas où les données ne sont pas formatées comme prévu.

    Paramètres avancés : Ajouter des paramètres avancés pour personnaliser le comportement des scripts, tels que spécifier un nom de fichier de sortie personnalisé.

    Interface utilisateur : Créer une interface utilisateur simple pour faciliter l'exécution des scripts sans avoir à utiliser la ligne de commande.

    Documentation étendue : Fournir une documentation plus détaillée sur l'utilisation des scripts, y compris des exemples avancés et des explications sur la structure du JSON généré.

    Tests unitaires : Mettre en place des tests unitaires pour vérifier que les scripts fonctionnent correctement.

## Conclusion

Ces scripts sont des outils utiles pour extraire des données à partir du jeu Dwarf Fortress. Ils peuvent être améliorés pour répondre à des besoins spécifiques et pour une utilisation plus conviviale. N'hésitez pas à les personnaliser selon vos besoins ou à contribuer à leur amélioration.