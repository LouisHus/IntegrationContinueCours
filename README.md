# Structure du projet
`loadFiles()` : Charge tous les fichiers Markdown et CSV du répertoire source et les traite individuellement.

`loadMD(file)` : Convertit un fichier Markdown en HTML et associe une image (si disponible).

`loadCSV(file)` : Convertit un fichier CSV en une page HTML avec les détails des membres.

`loadIndex()` : Crée une page d'accueil avec les événements et les informations des membres de l'association.

## Prérequis

- Python 3.x

- Bibliothèque markdown (installation via pip)

Installation
```python
pip install markdown
```

## Structure des fichiers

``` 
/project
│
├── /source
│   ├── event-1.md
│   ├── event-2.md
│   ├── membre.csv
│   └── image-1.webp
│   └──/result
│       │── (les fichiers HTML générés seront placés ici)
└──     └── script.py
 
```

