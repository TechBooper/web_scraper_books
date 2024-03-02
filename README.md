# Web_scraper_BooksOnline

#Extracteur de Livres

Ce script Python est conçu pour extraire les données des livres depuis "https://books.toscrape.com/", un site web dédié à la présentation d'une large variété de livres à travers différentes catégories. Il automatise la collecte d'informations à partir d'une liste de data demandées et produit un fichier csv contenant toutes ces informations ainsi qu'un directory images contenant toutes les images de chaque livres et de chaque catégorie.

#Fonctionnalités

- Extraire les catégories : Identifie et extrait automatiquement les catégories de livres du site web.
- Collecter les données des livres : Pour chaque livre, le script collecte les détails incluant l'UPC, le titre, le prix (avec et sans taxe), la disponibilité, la description du produit, la catégorie, l'évaluation des critiques, et l'URL de l'image.
- Télécharger les images : Télécharge et enregistre les images des livres dans un format de répertoire structuré.
- Gestion de pagination : Navigue à travers plusieurs pages au sein de chaque catégorie pour assurer une collecte complète des données.
- Sauvegarder les données : Enregistre les données extraites dans des fichiers CSV, organisés par catégorie de livre.

#Fonctionnement

1. Extraire les catégories : Le script commence par récupérer la liste des catégories de livres depuis la page d'accueil du site web.
2. Extraire les données des livres : Pour chaque catégorie, il extrait les données de tous les livres listés, gérant la pagination pour couvrir toutes les pages disponibles.
3. Télécharger les images : L'image de chaque livre est téléchargée et sauvegardée dans un répertoire nommé selon la catégorie.
4. Sauvegarder les données dans un CSV : Compile et sauvegarde les données des livres dans des fichiers CSV nommés selon le format `<nom_categorie>_livres.csv`.

#Utilisation

Pour utiliser ce script, exécutez-le dans un environnement où Python 3 est installé ainsi que les bibliothèques requises : `requests` et `BeautifulSoup4` de `bs4`.

#Prérequis

- Python 3.x
- Package `requests`
- Package `BeautifulSoup4`

Vous pouvez installer les packages requises en utilisant pip dans un terminal : pip install requests beautifulsoup4

Vous pouvez ouvrir votre terminal avec la commande windows + R et en tapant "cmd" dans la barre d'exécution.
  
Pour isoler ces packages dans un environnement virtuel, veuillez suivre ces instructions:
- Installer le package 'virtualenv' avec la commande: pip install virtualenv
- Donner le nom de votre choix à votre environnement (je choisi le nom Scraper): virtualenv Scraper
- Quand vous utilisez votre environnement, activez le avec ces commandes:
Windows: Scraper\Scripts\activate
MacOS ou Linux: Source Scraper\bin\activate
- Pour désactiver votre environnement: deactivate
