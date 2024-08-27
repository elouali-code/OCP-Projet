
# OCP Group - Prédiction des Performances des Compresseurs

## Description
Cette application permet de prédire les performances des compresseurs en se basant sur plusieurs paramètres. L'application est conçue pour être simple à utiliser, même pour une personne sans connaissances techniques.

## Prérequis
- **Python 3.x** doit être installé sur votre machine. Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).

## Étapes d'installation et d'exécution

### 1. Téléchargement du projet
- Téléchargez ou clonez le projet sur votre ordinateur.

### 2. Installation des dépendances
- Ouvrez un terminal (ou l'invite de commandes sur Windows).
- Naviguez jusqu'au dossier où se trouve le projet.
- Exécutez la commande suivante pour installer les bibliothèques nécessaires :

```bash
pip install flask pandas scikit-learn
```

### 3. Lancer l'application
Toujours dans le terminal, exécutez la commande suivante pour lancer l'application :

```bash
python main.py
```

### 4. Accéder à l'application
Une fois l'application lancée, ouvrez votre navigateur web préféré et accédez à l'adresse suivante :

```arduino
http://127.0.0.1:5000
```

### 5. Utilisation de l'application
Sur la page d'accueil de l'application, vous verrez une interface avec deux boutons :

- **Sélectionner un fichier Excel** : Cliquez sur ce bouton pour sélectionner le fichier Excel contenant les données des compresseurs que vous souhaitez analyser.
- **Uploader et Prédire** : Après avoir sélectionné votre fichier Excel, cliquez sur ce bouton pour uploader le fichier et recevoir la prédiction de la performance du compresseur.

Les résultats de la prédiction seront affichés directement sur la page avec un pourcentage de performance.

### 6. Personnalisation et ajustements
Si vous souhaitez modifier les paramètres ou les calculs utilisés par le modèle, vous pouvez le faire en modifiant le fichier `main.py` ou en ajustant les fichiers Excel que vous utilisez.

### 7. Arrêter l'application
Pour arrêter l'application, retournez au terminal où elle est en cours d'exécution et appuyez sur **CTRL+C**. Cela arrêtera le serveur Flask.

## Support
En cas de problème, veuillez contacter le développeur de l'application.

© 2024 OCP Group. Tous droits réservés. | Data Engineer & Developer: El Ouail Abderrahman
