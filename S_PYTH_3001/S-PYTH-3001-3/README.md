# Module File Manager — `list_directory`

Ce projet fait partie de la formation **PQDI** pour l'application **Gestionnaire de notes**. Il implémente la fonction `list_directory()`, intégrée au module `file_manager.py`, permettant d'explorer le système de fichiers et d'organiser le contenu d'un répertoire.

---

## 📌 Présentation

La fonction `list_directory()` a pour rôle de parcourir un répertoire donné et de séparer son contenu en deux catégories distinctes :
- La liste des **répertoires**
- La liste des **fichiers**

Cette fonction réutilise la fonction `check_path()` développée précédemment pour valider le chemin avant d'effectuer le parcours.

---

## 🛠️ Structure du Module `file_manager.py`

Le module regroupe les fonctions de gestion du système de fichiers :
```text
file_manager.py
├── check_path()
├── create_directory()
└── list_directory()
```

---

## ⚙️ Spécifications de la Fonction `list_directory()`

### Signature
```python
def list_directory(root: str) -> dict:
```

### Paramètre
- **`root`** (`str`) : Le chemin du répertoire à explorer (ex: `"C:\\Users\\stebar\\Python"`).

### Validation des Entrées
1. **Type du paramètre** : `root` doit obligatoirement être une chaîne de caractères (`str`). Si le type est incorrect (ex: `123`, `None`, listes), la fonction doit gérer ce cas de manière appropriée.
2. **Existence du répertoire** : La fonction réutilise `check_path(root)` pour vérifier que le chemin correspond bien à un répertoire existant. Si la racine n'est pas valide ou désigne un fichier, aucun parcours n'est effectué.

### Type et Format de Retour
La fonction retourne un dictionnaire contant deux clés obligatoires `"dir"` et `"file"` :
```python
{
    "dir": [],  # Liste contenant uniquement les noms des sous-répertoires
    "file": []  # Liste contenant uniquement les noms des fichiers
}
```

*Note : Seuls les noms des éléments sont conservés dans le résultat final, et non leurs chemins complets.*

---

## 💡 Exemple d'Utilisation

Si le répertoire `Python/` contient l'arborescence suivante :
```text
Python/
├── data/
├── mastermind/
├── notes/
├── main.py
├── test.py
└── README.md
```

L'appel à `list_directory("C:\\Users\\stebar\\Python")` renvoie :
```python
{
    "dir": ["data", "mastermind", "notes"],
    "file": ["main.py", "test.py", "README.md"]
}
```

---

## 📑 Algorithme & Logique

1. Recevoir le paramètre `root`.
2. Vérifier que `root` est une chaîne de caractères (`str`).
3. Valider avec `check_path()` que `root` est un répertoire existant.
4. Initialiser le dictionnaire de résultat : `{"dir": [], "file": []}`.
5. Récupérer les éléments du répertoire via le module `os`.
6. Pour chaque élément :
   - Construire le chemin complet (`os.path.join`).
   - Si l'élément est un répertoire (`os.path.isdir`), ajouter son nom dans `"dir"`.
   - Si l'élément est un fichier (`os.path.isfile`), ajouter son nom dans `"file"`.
7. Retourner le dictionnaire résultat.

---

## 🧪 Cas de Test

Les cas de test suivants doivent être validés :
1. **Répertoire mixte** : Contenant à la fois des fichiers et des dossiers.
2. **Répertoire vide** : Doit retourner `{"dir": [], "file": []}`.
3. **Répertoire avec fichiers uniquement** : `{"dir": [], "file": [...]}`.
4. **Répertoire avec dossiers uniquement** : `{"dir": [...], "file": []}`.
5. **Racine inexistante** : Gestion des erreurs sans tenter d'explorer le chemin.
6. **Chemin pointant vers un fichier** : Détection comme cas invalide.
7. **Type de paramètre incorrect** (ex: `list_directory(123)`).

---

## 📋 Critères de Réussite

- Nom de fonction `list_directory(root)`.
- Validation stricte du type `str` et du répertoire via `check_path()`.
- Utilisation adaptée des fonctions des modules `os` et `os.path`.
- Retour d'un dictionnaire avec les clés `"dir"` et `"file"`.
- Présence d'une docstring descriptive.
