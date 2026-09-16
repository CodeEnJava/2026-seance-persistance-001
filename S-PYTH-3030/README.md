# 2026-seance-file-connection-part-001
# S-PYTH-3030 — Gestion des connexions aux fichiers

## 🐍 Gestionnaire de notes — Persistance des données et échanges de fichiers

Ce dépôt correspond à la séance **S-PYTH-3030** du module :

> **S-PYTH-3000 — Persistance des données et échanges de fichiers**

Cette séance s'inscrit dans la réalisation progressive d'un projet pédagogique :

> **Gestionnaire de notes**

L'objectif du projet est de construire progressivement une application Python permettant de gérer et de sauvegarder les notes de stagiaires.

---

## 🎯 Objectif de la séance

Dans la séance précédente **S-PYTH-3001**, nous avons commencé à gérer le système de fichiers avec le module :

```text
file_manager.py
```

Ce module permet notamment de vérifier l'existence d'un fichier ou d'un répertoire.

Dans cette nouvelle séance, nous allons créer :

```text
file_connection.py
```

Son rôle est de centraliser la **gestion des connexions aux fichiers**.

L'objectif est de ne pas disperser les appels à `open()` et `close()` dans les différentes fonctionnalités de l'application.

![Architecture du module](./images/gestion_file_connection.png)

Nous commençons ainsi à mettre en place une séparation des responsabilités dans notre projet.

---

# 📂 Organisation des modules

L'architecture commence progressivement à prendre la forme suivante :

```text
Gestionnaire de notes
│
├── file_manager.py
│   └── Gestion des chemins
│
└── file_connection.py
    └── Gestion des connexions aux fichiers
```

Le module `file_connection.py` utilise notamment la fonction :

```python
check_path()
```

provenant du module :

```text
S_PYTH_3001.file_manager
```

---

# 🔌 Qu'est-ce qu'une connexion à un fichier ?

Lorsque Python exécute :

```python
connection = open("notes.txt", "r", encoding="utf-8")
```

la fonction `open()` ne retourne pas directement le contenu du fichier.

Elle retourne un **objet représentant une connexion ouverte vers le fichier**.

Cette connexion peut ensuite être utilisée pour effectuer différentes opérations :

```python
content = connection.read()
```

ou :

```python
connection.write("Nouvelle note")
```

Lorsque le travail est terminé, la connexion doit être fermée :

```python
connection.close()
```

Dans cette séance, nous allons donc encapsuler ces opérations dans notre propre module.

---

# ⚙️ Les modes d'ouverture

Le module `file_connection.py` centralise les principaux modes d'ouverture utilisés dans le projet.

| Constante                | Mode  | Utilisation              |
| ------------------------ | ----- | ------------------------ |
| `READ_ONLY_MODE`         | `r`   | Lecture seule            |
| `WRITE_ONLY_MODE`        | `w`   | Écriture                 |
| `APPEND_MODE`            | `a`   | Ajout en fin de fichier  |
| `APPEND_READ_MODE`       | `a+`  | Lecture et ajout         |
| `READ_WRITE_MODE`        | `r+`  | Lecture et écriture      |
| `WRITE_READ_MODE`        | `w+`  | Écriture et lecture      |
| `BINARY_READ_MODE`       | `rb`  | Lecture binaire          |
| `BINARY_WRITE_MODE`      | `wb`  | Écriture binaire         |
| `BINARY_READ_WRITE_MODE` | `rb+` | Lecture/écriture binaire |
| `BINARY_WRITE_READ_MODE` | `wb+` | Écriture/lecture binaire |

Les différents modes sont regroupés dans :

```python
VALID_MODES
```

Cette constante permet de contrôler les modes acceptés par notre module.

---

# 🧩 Fonctions du module

## `is_binary_mode()`

Détermine si le mode demandé correspond à une ouverture en mode binaire.

Exemple :

```python
is_binary_mode("r")
```

retourne :

```text
False
```

Alors que :

```python
is_binary_mode("rb")
```

retourne :

```text
True
```

---

## `is_valid_mode()`

Vérifie que le mode demandé fait partie des modes autorisés.

Exemple :

```python
is_valid_mode("r")
```

retourne :

```text
True
```

Alors que :

```python
is_valid_mode("xyz")
```

retourne :

```text
False
```

---

## `is_obj_connection()`

Vérifie qu'un objet correspond à une connexion fichier prise en charge par le module.

Cette fonction utilise notamment `isinstance()` et les différents types proposés par le module `_io`.

Elle permet notamment de contrôler l'objet avant de demander sa fermeture.

---

## `open_connection()`

La fonction `open_connection()` centralise l'ouverture d'un fichier.

Elle effectue plusieurs contrôles :

```text
                open_connection()
                       │
                       ▼
              Mode valide ?
                 │       │
                NON     OUI
                 │       │
                 ▼       ▼
             ValueError  Fichier existant ?
                            │       │
                           NON     OUI
                            │       │
                            ▼       ▼
                          None   Texte / binaire
                                      │
                                      ▼
                                    open()
```

Exemple :

```python
connection = open_connection(
    "notes.txt",
    READ_ONLY_MODE
)
```

Pour un fichier texte, le module utilise :

```python
encoding="utf-8"
```

Pour un fichier binaire, aucun encodage n'est utilisé.

---

## `close_connection()`

La fonction `close_connection()` permet de fermer une connexion.

Avant de fermer le fichier, elle vérifie que l'objet fourni correspond bien à une connexion valide.

Exemple :

```python
connection = open_connection(
    "notes.txt",
    READ_ONLY_MODE
)

if connection:
    content = connection.read()

    close_connection(connection)
```

Si l'objet fourni n'est pas une connexion valide, une `TypeError` est déclenchée.

---

# 🧪 Exemple complet

Un exemple simple d'utilisation du module :

```python
from file_connection import (
    open_connection,
    close_connection,
    READ_ONLY_MODE
)

connection = open_connection(
    "notes.txt",
    READ_ONLY_MODE
)

if connection:
    content = connection.read()

    print(content)

    close_connection(connection)
```

L'application n'a donc plus besoin de gérer directement la logique de contrôle du mode et de vérification du fichier.

---

# 🏗️ Séparation des responsabilités

Cette séance permet de commencer à organiser le projet selon différentes responsabilités.

```text
┌───────────────────────────────┐
│       Gestionnaire de notes   │
└───────────────┬───────────────┘
                │
                ▼
       ┌─────────────────┐
       │ file_connection │
       └────────┬────────┘
                │
        open() / close()
                │
                ▼
       ┌─────────────────┐
       │      Fichier    │
       └─────────────────┘
                ▲
                │
       check_path()
                │
       ┌────────┴────────┐
       │  file_manager   │
       └─────────────────┘
```

L'objectif n'est pas seulement de faire fonctionner le programme.

Nous cherchons progressivement à construire une application dans laquelle chaque module possède une **responsabilité clairement identifiée**.

---

# 📚 Notions Python abordées

Cette séance permet de travailler ou de consolider les notions suivantes :

* fonctions ;
* paramètres par défaut ;
* valeurs de retour ;
* constantes ;
* tuples ;
* imports ;
* modules ;
* `open()` ;
* `close()` ;
* encodage UTF-8 ;
* fichiers texte ;
* fichiers binaires ;
* `isinstance()` ;
* `raise` ;
* `ValueError` ;
* `TypeError` ;
* objets de connexion ;
* module `_io` ;
* séparation des responsabilités.

---

# 🎓 Objectifs pédagogiques

À l'issue de cette séance, le stagiaire doit être capable de :

* expliquer le rôle de `open()` ;
* expliquer ce qu'est une connexion à un fichier ;
* distinguer les principaux modes d'ouverture ;
* distinguer une ouverture texte d'une ouverture binaire ;
* utiliser une constante représentant un mode ;
* vérifier qu'un mode est autorisé ;
* ouvrir un fichier avec une fonction dédiée ;
* fermer une connexion ;
* utiliser `isinstance()` pour contrôler un objet ;
* utiliser `ValueError` et `TypeError` pour signaler des erreurs ;
* réutiliser une fonction provenant d'un autre module ;
* comprendre l'intérêt de séparer les responsabilités entre plusieurs modules.

---

# 🔗 Dépendance

Le module dépend du module réalisé dans la séance **S-PYTH-3001** :

```python
from S_PYTH_3001.file_manager import check_path
```

La fonction `check_path()` est utilisée pour vérifier que le fichier existe avant de tenter de l'ouvrir.

---

# 🚀 Évolution du projet

Le projet **Gestionnaire de notes** va continuer à évoluer progressivement.

Les prochaines étapes permettront notamment de mettre en œuvre :

```text
Gestionnaire de notes
        │
        ├── Gestion des chemins
        │
        ├── Connexion aux fichiers
        │
        ├── Lecture
        │
        ├── Écriture
        │
        ├── Modification
        │
        ├── Suppression
        │
        └── Persistance au format JSON
```

L'objectif final est de construire progressivement une application Python structurée en séparant les différentes responsabilités.

---

## 🎬 Vidéo de la séance

Cette séance est accompagnée d'une vidéo de programmation présentant la construction progressive du module `file_connection.py`.

La vidéo montre notamment :

* la création des constantes ;
* la gestion des modes d'ouverture ;
* la détection des modes binaires ;
* la validation des modes ;
* l'ouverture des fichiers ;
* la gestion des connexions ;
* la fermeture des fichiers ;
* la structuration progressive du projet.

---

## 📌 Série S-PYTH-3000

**S-PYTH-3000 — Persistance des données et échanges de fichiers**

Projet support :

**Gestionnaire de notes**

Séance :

**S-PYTH-3030 — Gestion des connexions aux fichiers**

---

## 👨‍💻 Projet pédagogique

Projet réalisé dans le cadre de la formation aux **métiers de développeur informatique**.

L'objectif est de privilégier une progression concrète :

```text
Comprendre
    ↓
Expérimenter
    ↓
Coder
    ↓
Tester
    ↓
Structurer
    ↓
Faire évoluer
```

**Concevoir, sécuriser, faire évoluer.**
