# Module S-PYTH-3001-1 : Vérification d'un chemin (`check_path`)

Ce projet constitue la première brique du module réutilisable de gestion des fichiers et dossiers pour l'application **Gestionnaire de notes** (Formation PQDI) [1, 2].

## 📋 Présentation

Dans le cadre du projet *Gestionnaire de notes*, l'application doit vérifier qu'un chemin existe avant d'effectuer des opérations sur le système de fichiers [2]. La fonction `check_path()` permet de contrôler l'existence et le type d'un chemin (répertoire ou fichier) et de réutiliser cette logique à travers différentes fonctionnalités du système (ex. vérification du dossier *Gestion_Notes*, des fichiers JSON, etc.) [1, 2].

## ⚙️ Spécifications de la fonction

- **Nom de la fonction :** `check_path(path, path_type="dir")` [3]
- **Paramètres :**
  - `path` *(str)* : Le chemin vers le fichier ou le répertoire à vérifier [3].
  - `path_type` *(str, optionnel)* : Le type attendu. Valeurs acceptées : `"dir"` (répertoire) ou `"file"` (fichier) [3]. Valeur par défaut : `"dir"` [3].
- **Valeur de retour :** `bool` (`True` si le chemin existe et correspond au type demandé, `False` sinon) [2, 3, 4].
- **Aide / Affichage :** La fonction ne réalise aucun affichage (`print()`) [5, 10].

## 🛠️ Contraintes techniques

- Utilisation du module standard Python `os` et plus particulièrement `os.path` [5].
- Prise en compte de la `docstring` documentant le rôle, les paramètres et le type de retour [9, 10].
- Gestion des types inconnus de `path_type` (retourne `False`) [8, 10].

## 🧪 Cas de test

1. **Répertoire existant (type par défaut) :** `check_path("chemin/dossier")` $\rightarrow$ `True` [4, 6]
2. **Répertoire inexistant :** `check_path("chemin/inexistant")` $\rightarrow$ `True` / `False` [4, 6]
3. **Fichier existant :** `check_path("chemin/fichier.txt", "file")` $\rightarrow$ `True` [4, 7]
4. **Fichier inexistant :** `check_path("chemin/inexistant.txt", "file")` $\rightarrow$ `False` [4, 7]
5. **Fichier recherché comme répertoire :** `check_path("chemin/fichier.txt", "dir")` $\rightarrow$ `False` [7]
6. **Répertoire recherché comme fichier :** `check_path("chemin/dossier", "file")` $\rightarrow$ `False` [7]
