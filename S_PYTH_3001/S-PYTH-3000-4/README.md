# Gestion_Notes — Construction de l'arborescence du projet

Ce projet en Python (module `file_manager.py`) permet de construire et de gérer l'arborescence de dossiers pour l'application **Gestion_Notes**.

---

## 📌 Objectif du projet

L'objectif est d'automatiser la création d'une structure de répertoires modulaire pour organiser les espaces de stockage des stagiaires et leurs dossiers de matières.

---

## 📁 Arborescence générée

L'application génère la structure de dossiers suivante :

```
Gestion_Notes/
└── 2026_nom_prenom/
    ├── S_MATH/
    ├── S_ALGO/
    ├── S_PYTH/
    ├── S_TPTD/
    └── S_PROJ/
```

---

## 🛠️ Architecture du module (`file_manager.py`)

Le projet est structuré selon une approche modulaire séparant les responsabilités en trois niveaux :

### 1. Fonctions élémentaires
- **`check_path()`** : Vérification des chemins dans le système de fichiers.
- **`create_directory()`** : Création d'un dossier. Retourne un code d'état (`1` : création réalisée, `0` : dossier déjà existant, `-1` : création impossible).
- **`list_directory()`** : Listage du contenu des répertoires.

### 2. Fonctions spécialisées
- **`create_main_directory(root)`** : Crée le dossier principal `Gestion_Notes` à partir du chemin racine fourni.
- **`create_trainee_space(root, name)`** : Crée l'espace d'un stagiaire en respectant la convention de nommage `2026_nom_prenom`.
- **`create_subject_directories(trainee_path)`** : Crée les 5 sous-dossiers de matières (`S_MATH`, `S_ALGO`, `S_PYTH`, `S_TPTD`, `S_PROJ`).
- **`get_absolute_path(path)`** : Convertit un chemin relatif en chemin absolu via le module `os.path`.

### 3. Fonction d'orchestration
- **`add_trainee(root, name)`** : Orchestre les fonctions précédentes pour créer automatiquement l'arborescence complète d'un nouveau stagiaire (dossier principal, espace stagiaire et sous-dossiers de matières).

---

## 🚀 Exemple d'utilisation

```python
from file_manager import add_trainee, get_absolute_path

# Conversion d'un chemin relatif en chemin absolu
abs_path = get_absolute_path("Gestion_Notes")

# Ajout d'un nouveau stagiaire
add_trainee("C:\\Users\\stebar\\Python", "toto_otto")
```
