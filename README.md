"# mixeur_images" 

# mixeur_images

Petite application Gradio pour mixer deux images via un simple blending.

## Présentation

`mixeur_images` est une application web légère construite avec [Gradio](https://gradio.app/) et [Pillow](https://python-pillow.org/) permettant de fusionner deux images en ajustant dynamiquement le ratio de mélange.

## Prérequis

- Python 3.7 ou supérieur
- pip

## Installation

1. Cloner le dépôt GitHub :
   ```bash
   git clone https://github.com/<ton-utilisateur>/mixeur_images.git
   ```
2. Se rendre dans le dossier du projet :
   ```bash
   cd mixeur_images
   ```
3. Installer les dépendances :
   ```bash
   pip install gradio pillow
   ```

## Usage

Lancer l'application :
```bash
python mixeur_images.py
```

Une fois lancée, ouvre ton navigateur à l'adresse indiquée (généralement `http://127.0.0.1:7860`).

1. Upload deux images.
2. Ajuste le slider **Mix Ratio (alpha)** pour définir le pourcentage de chaque image dans le résultat.
3. Visualise et télécharge le mélange final.

## Structure du projet

```
mixeur_images/
├── mixeur_images.py    # Script principal de l'application
├── README.md           # Documentation du projet
└── .gitignore          # Fichiers et dossiers exclus du dépôt
```

## Personnalisation

- Modifier la fonction `blend_images` dans `mixeur_images.py` pour changer la méthode de fusion.
- Ajouter d'autres widgets Gradio (boutons, dropdowns) selon tes besoins.

## Contribuer

Les contributions sont les bienvenues !

1. Fork le dépôt.
2. Crée une branche (`git checkout -b feature/nom-feature`).
3. Commit tes changements (`git commit -m "Ajout d'une nouvelle feature"`).
4. Push ta branche (`git push origin feature/nom-feature`).
5. Ouvre une Pull Request.

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

