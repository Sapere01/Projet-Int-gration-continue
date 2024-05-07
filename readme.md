# Application de Gestion de Tâches Collaboratives

Cette application de gestion de tâches collaboratives a été développée dans le cadre du projet du cours de Tests Logiciels & Intégration Continue à l'Ecole Polytechnique de Ouagadougou (EPO). L'objectif principal était de mettre en pratique les connaissances acquises en tests logiciels et intégration continue, en utilisant le framework web Django.

## Enseignant
- KABORE Abdoul Kader

## Auteurs
- YAMEOGO Baowendsomme Armel
- SANGO Appolinaire


## Fonctionnalités

- **Gestion des Tâches :** Les utilisateurs peuvent créer de nouvelles tâches, les afficher et les marquer comme terminées à partir de la ligne de commande.
- **Statistiques sur les Tâches :** Les utilisateurs peuvent obtenir des statistiques sur leurs tâches, telles que le nombre total de tâches, le nombre de tâches terminées, etc.
- **Interface Utilisateur Conviviale :** Une interface utilisateur en ligne de commande simple et intuitive permet aux utilisateurs d'interagir facilement avec l'application pour gérer leurs tâches.


## Technologies Utilisées

- Framework Web: Django
- Base de Données: SQLite (par défaut avec Django)
- Outils d'Intégration Continue: GitLab CI/CD

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python et Django installés sur votre machine.
3. Naviguez vers le répertoire du projet dans votre terminal.
4. Installez les dépendances en exécutant la commande :
```
pip install -r requirements.txt
```
5. Appliquez les migrations avec la commande :
```
python manage.py migrate
```
6. Tester l'application avec la commande :
```
python manage.py todo
```
