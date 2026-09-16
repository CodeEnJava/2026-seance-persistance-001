# Gestionnaire de fichiers — `file_manager.py`

Ce dépôt contient l'implémentation de la fonction **`create_directory()`**, développée dans le cadre du module `file_manager.py` (Formation PQDI : **S-PYTH-3001-2**).

## 📌 Présentation

La fonction `create_directory()` permet de créer un nouveau répertoire sur le système de fichiers à partir d'une racine existante. Elle s'intègre de manière modulaire aux fonctionnalités de gestion de fichiers et réutilise la fonction `check_path()`.

---

## 🛠️ Structure du module

```text
file_manager.py
 ├── check_path()
 └── create_directory()
```

---

## ⚙️ Spécification de la fonction

### Signature
```python
def create_directory(root: str, directory_name: str) -> bool:
```

### Paramètres
* **`root`** (`str`) : Le chemin de la racine dans laquelle le répertoire doit être créé.
* **`directory_name`** (`str`) : Le nom du nouveau répertoire à créer.

### Valeur de retour
* **`True`** : Si le répertoire est créé avec succès ou s'il existait déjà.
* **`False`** : En cas d'échec (paramètres invalides ou racine inexistante).

---

## 🔄 Algorithme et Déroulement

1. **Validation des paramètres** :
   * Les arguments `root` et `directory_name` doivent impérativement être de type `str`.
   * Si l'un des paramètres est invalide, la fonction retourne immédiatement `False`.
2. **Vérification de la racine** :
   * La fonction vérifie l'existence de la racine en réutilisant `check_path(root)`.
   * Si la racine n'existe pas, la création échoue et la fonction retourne `False`.
3. **Construction du chemin** :
   * Le chemin complet est assemblé proprement à l'aide du module `os.path` (via `os.path.join`), sans concaténation manuelle avec des séparateurs de chemin (`\`).
4. **Création du répertoire** :
   * Le répertoire est créé via la fonctionnalité dédiée du module standard `os`.
   * *Cas particulier* : Si le répertoire existe déjà au chemin spécifié, l'opération est considérée comme réussie (`True`) car l'objectif (disposer du répertoire) est atteint.
5. **Absence d'affichage** :
   * La fonction ne réalise aucun affichage console (`print`), elle communique son résultat exclusivement via son booléen de retour.

---

## 💡 Exemples d'utilisation

### Situation 1 — Racine existante
```python
create_directory("C:\\Users\\stebar\\Python", "data")
# Résultat : True
# Le dossier "C:\Users\stebar\Python\data" est créé.
```

### Situation 2 — Racine inexistante
```python
create_directory("C:\\Users\\stebar\\Python\\inexistant", "data")
# Résultat : False
# Le dossier n'est pas créé car le dossier parent n'existe pas.
```

### Situation 3 — Paramètre invalide
```python
create_directory(123, "data")
# Résultat : False (type de 'root' invalide)
```

---

## ✅ Critères de réussite

* Nom de fonction : `create_directory()`
* Deux paramètres obligatoires de type `str` (`root`, `directory_name`).
* Validation stricte des types des arguments.
* Vérification préalable de la racine via réutilisation de `check_path()`.
* Construction robuste du chemin complet avec `os.path`.
* Création effective du dossier via le module `os`.
* Retour booléen unique (`True` / `False`) et aucun affichage console.
