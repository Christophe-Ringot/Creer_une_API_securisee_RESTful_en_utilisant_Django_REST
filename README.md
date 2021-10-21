# Projet 10:  Créer une API securisée RESTful en utilisant Django REST.
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


## Description :


SoftDesk est une application sécurisée s'adressant à des entreprises en B2B, permettant de remonter et suivre des problèmes technique (tracking system).


## Fonctionnalités :


- Inscription et connexion des utilisateurs.
- Création de projet (titre, description, type, auteur).
- Si il est contributeur ou auteur, chaque projet peut se voir associer des problèmes.
- Chaque problèmes peut faire objet de commentaire de la part des contributeurs.


## Installation :


Cloner ce dépôt de code à l'aide de la commande :
```$ git clone https://github.com/Christophe-Ringot/Projet_10_Creer_une_API_securisee_RESTful_en_utilisant_Django_REST.git```

Créer un environnement virtuel pour le projet :
```$ python -m venv env``` sous windows ou ```$ python3 -m venv env``` sous macos ou linux.

Activez l'environnement virtuel :
```$ env\Scripts\activate``` sous windows ou ```$ source env/bin/activate sous macos ou linux.```

Installez les dépendances de à l'aide de la commande :
```pip install -r requirements.txt```


## Exécution :

Se rendre sur le dossier avec la commande :
```$ cd SoftDesk```

Créer un nouveau compte administrateur :
```$ python3 manage.py createsuperuser```

Lancez le serveur avec la commande :
```$ python3 manage.py runserver```


## Lien Postman :


https://documenter.getpostman.com/view/17770612/UV5WFJpp
