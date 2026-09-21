# 2026-seance-persistance-001
# S-PYTH-3000 — Persistance des données et échanges de fichiers

## 📚 Présentation

Jusqu'à présent, les programmes Python développés manipulent principalement des données stockées en mémoire.

Lorsque le programme s'arrête, ces données disparaissent.

Cette séquence introduit la **persistance des données** : l'objectif est d'apprendre à enregistrer durablement des informations sur le disque afin de pouvoir les retrouver et les exploiter lors d'une prochaine exécution du programme.

Au cours de cette séquence, vous apprendrez progressivement à :

* manipuler des dossiers et des fichiers ;
* construire et parcourir une arborescence ;
* lire des données depuis un fichier ;
* écrire des données dans un fichier ;
* modifier et supprimer des données ;
* comprendre les limites du stockage sous forme de fichiers texte ;
* découvrir le format **JSON** ;
* lire des données structurées au format JSON ;
* modifier et sauvegarder des données JSON.

---

# 🎯 Projet fil rouge — Gestionnaire de notes

Tout au long de la séquence, vous allez développer progressivement une application permettant de **gérer les notes de plusieurs stagiaires**.

Chaque stagiaire possède plusieurs ensembles de notes correspondant aux matières suivantes :

* [Mathématiques](https://ladapt95.lilicampus.com/mod/quiz/view.php?id=1884) ;
* [Algorithmique](https://ladapt95.lilicampus.com/mod/quiz/view.php?id=1882) ;
* Python ;
* TP / TD ;
* Projets.

Le projet sera d'abord construit à partir de **fichiers texte**.

La structure des données évoluera ensuite progressivement vers une solution utilisant le format **JSON**.

L'objectif est de comprendre la transformation :

```text
Données temporaires en mémoire
             ↓
       Fichiers texte
             ↓
      Données structurées
             ↓
             JSON
```

---

# 📝 Cahier des charges

L'application doit permettre de créer et gérer un espace de stockage pour chaque stagiaire.

Chaque stagiaire possède un dossier dont le nom respecte la convention :

```text
2026_nom_prenom
```

Exemple :

```text
2026_toto_otto
```

Tous les stagiaires sont regroupés dans un dossier principal :

```text
Gestion_Notes
```

---

## 📁 Organisation des dossiers

Chaque stagiaire possède cinq dossiers correspondant aux différentes matières :

```text
S_MATH
S_ALGO
S_PYTH
S_TPTD
S_PROJ
```

L'organisation générale est la suivante :

```text
Gestion_Notes/
│
└── 2026_nom_prenom/
    │
    ├── S_MATH/
    ├── S_ALGO/
    ├── S_PYTH/
    ├── S_TPTD/
    └── S_PROJ/
```

---

## 📄 Organisation des fichiers de notes

Chaque matière contient un fichier de notes pour chaque mois de l'année :

```text
jan_notes.txt
feb_notes.txt
mar_notes.txt
apr_notes.txt
may_notes.txt
jun_notes.txt
jul_notes.txt
aug_notes.txt
sep_notes.txt
oct_notes.txt
nov_notes.txt
dec_notes.txt
```

L'organisation complète peut être représentée ainsi :

```text
Gestion_Notes/
│
└── 2026_nom_prenom/
    │
    ├── S_MATH/
    │   ├── jan_notes.txt
    │   ├── feb_notes.txt
    │   └── ...
    │
    ├── S_ALGO/
    │   ├── jan_notes.txt
    │   └── ...
    │
    ├── S_PYTH/
    │   ├── jan_notes.txt
    │   └── ...
    │
    ├── S_TPTD/
    │   ├── jan_notes.txt
    │   └── ...
    │
    └── S_PROJ/
        ├── jan_notes.txt
        └── ...
```

---

# 🎯 Fonctionnalités attendues

À terme, l'application devra permettre de gérer l'environnement de stockage et les notes.

## Gestion de l'environnement

* créer le dossier principal ;
* vérifier l'existence d'un dossier ;
* créer un dossier ;
* créer l'arborescence complète d'un stagiaire ;
* lister les dossiers ;
* lister les fichiers.

## Gestion des notes

* ajouter une note ;
* lire les notes enregistrées ;
* afficher les notes d'une matière ;
* modifier une note ;
* supprimer une note.

## Persistance des données

Les données seront d'abord enregistrées dans des **fichiers texte**.

Elles évolueront ensuite vers une structure de données utilisant le **format JSON**.

---

# 🧩 S-PYTH-3001 — Les fichiers et les dossiers

## Objectifs

Cette séance permet de découvrir comment Python peut interagir avec le système de fichiers.

Vous apprendrez à :

* manipuler des chemins ;
* vérifier l'existence d'un dossier ;
* créer un dossier ;
* créer plusieurs dossiers ;
* parcourir une arborescence ;
* lister le contenu d'un dossier.

## Projet

Vous allez créer un module dédié à la manipulation des fichiers et des dossiers :

```text
file_manager.py
```

Ce module permettra progressivement de :

```text
vérifier un dossier
créer un dossier
lister un dossier
créer le dossier principal
créer l'espace d'un stagiaire
créer les dossiers des matières
```

## Application au projet

À la fin de la séance, l'application doit être capable de créer automatiquement une structure telle que :

```text
Gestion_Notes/
│
└── 2026_nom_prenom/
    ├── S_MATH/
    ├── S_ALGO/
    ├── S_PYTH/
    ├── S_TPTD/
    └── S_PROJ/
```

---

# 📖 S-PYTH-3002 — Lire des données dans un fichier

## Objectifs

Cette séance est consacrée à la lecture de données depuis un fichier texte.

Vous découvrirez comment :

* ouvrir un fichier ;
* lire son contenu ;
* lire une ligne ;
* lire plusieurs lignes ;
* parcourir les données d'un fichier ;
* récupérer une information précise.

## Projet

Vous allez créer un module dédié à la lecture des fichiers :

```text
file_reader.py
```

Responsabilité du module :

> Lire et retourner les données enregistrées dans un fichier.

## Application au projet

# Structure des fichiers de notes

## Format d'un enregistrement

Dans le cadre du projet **Gestionnaire de notes**, les notes sont stockées dans des fichiers texte encodés en **UTF-8**.

Afin de faciliter la lecture, la recherche et l'accès direct aux données, chaque enregistrement possède une **structure à longueur fixe**.

Un enregistrement correspond à une note attribuée à un stagiaire.

### Structure

| Champ         | Format                       |         Taille |
| ------------- | ---------------------------- | -------------: |
| `date`        | `yyyy-mm-dd`                 |      10 octets |
| `reference`   | `S-PYTH-3000-00`             |      14 octets |
| `type`        | `EVALUATION`, `TP`, `PROJET` |      10 octets |
| `note`        | `##.##`                      |       5 octets |
| `observation` | texte                        |     100 octets |
| **Total**     |                              | **139 octets** |

### Exemple

Un enregistrement peut être représenté ainsi :

```text
2026-09-19S-PYTH-3000-00EVALUATION15.50Très bon travail sur la lecture des fichiers
```

La structure logique est :

```text
┌──────────┬────────────────┬──────────┬─────┬───────────────────────────────────────────────────────────────┐
│ Date     │ Référence      │ Type     │Note │ Observation                                                    │
│ 10 oct.  │ 14 octets      │ 10 oct.  │5    │ 100 octets                                                     │
└──────────┴────────────────┴──────────┴─────┴───────────────────────────────────────────────────────────────┘

                         Taille totale : 139 octets
```

## Champ `type`

Trois types de notes sont prévus :

```text
EVALUATION
TP
PROJET
```

Le champ possède une largeur fixe de **10 octets**.

Les valeurs plus courtes sont complétées par des espaces :

```text
EVALUATION
TP        
PROJET    
```

Ainsi, quelle que soit la valeur utilisée, le champ occupe toujours **10 octets**.

## Encodage UTF-8

Les fichiers sont enregistrés en **UTF-8**.

La taille d'une donnée doit donc être considérée en **octets** et non uniquement en nombre de caractères.

Par exemple :

```python
texte = "EVALUATION"

print(len(texte))
print(len(texte.encode("utf-8")))
```

Résultat :

```text
10
10
```

Pour garantir la longueur fixe des champs, il est recommandé de contrôler la taille avec :

```python
len(texte.encode("utf-8"))
```

## Accès à un enregistrement

La longueur fixe de **139 octets** permet de déterminer directement la position d'un enregistrement dans le fichier.

Par exemple, pour accéder au troisième enregistrement :

```python
position = 2 * 139
```

Puis :

```python
file.seek(position)
```

Le programme peut alors lire les **139 octets** correspondant à cet enregistrement.

Cette organisation permettra au module `reader.py` de proposer progressivement des fonctions permettant :

* de connaître la taille d'un fichier ;
* de positionner le curseur de lecture ;
* de lire un nombre précis d'octets ;
* de lire un segment de données ;
* d'accéder directement à un enregistrement.

## Remarque

La taille de **139 octets** correspond à la structure définie actuellement :

```text
10 + 14 + 10 + 5 + 100 = 139 octets
```

Cette structure constitue le format de référence utilisé par le projet **Gestionnaire de notes**.

```

Le programme devra être capable de lire ces données afin de pouvoir ensuite les exploiter.

---

# ✍️ S-PYTH-3003 — Écrire, modifier et supprimer des données

## Objectifs

Cette séance permet d'apprendre à modifier le contenu d'un fichier texte.

Vous découvrirez comment :

* créer un fichier ;
* écrire une donnée ;
* ajouter une donnée ;
* modifier une donnée ;
* supprimer une donnée ;
* réécrire le contenu d'un fichier.

## Projet

Vous allez créer un module dédié à l'écriture des données :

```text
file_writer.py
```

Ce module permettra progressivement de :

```text
écrire une donnée
ajouter une donnée
modifier une donnée
supprimer une donnée
réécrire le contenu d'un fichier
```

## 💡 Point important

Modifier ou supprimer une donnée dans un fichier texte nécessite généralement de suivre cette démarche :

```text
Lire le fichier
      ↓
Modifier les données en mémoire
      ↓
Réécrire le fichier
```

Cette approche permet de comprendre les limites et les contraintes du stockage sous forme de fichiers texte.

---

# 🗂️ S-PYTH-3010 — Découvrir la structure JSON

## Objectifs

Les fichiers texte sont adaptés au stockage de données simples.

Cependant, lorsque les données deviennent plus nombreuses et plus structurées, il devient nécessaire d'utiliser un format permettant de représenter cette organisation.

Cette séance introduit le format **JSON**.

Vous apprendrez notamment à faire le lien entre les structures Python et les structures JSON.

| Python               | JSON    |
| -------------------- | ------- |
| dictionnaire         | objet   |
| liste                | tableau |
| chaîne de caractères | string  |
| nombre               | number  |
| booléen              | boolean |
| `None`               | `null`  |

## Exemple

Une structure JSON peut représenter les informations d'un stagiaire :

```json
{
    "nom": "Dupont",
    "prenom": "Jean",
    "annee": 2026,
    "notes": {
        "python": [12, 15, 18]
    }
}
```

---

# 📖 S-PYTH-3011 — Lire un fichier JSON

## Objectifs

Cette séance permet d'apprendre à lire un fichier JSON et à convertir son contenu en structures Python.

Vous découvrirez comment :

* ouvrir un fichier JSON ;
* lire son contenu ;
* convertir le JSON en dictionnaires et listes Python ;
* parcourir les données ;
* récupérer une information précise.

## Projet

Vous allez créer un module dédié à la lecture des données JSON :

```text
json_reader.py
```

Responsabilité du module :

> Lire un fichier JSON et retourner les données sous forme de structures Python.

---

# ✍️ S-PYTH-3012 — Modifier des données JSON

## Objectifs

Cette dernière séance permet d'apprendre à modifier une structure JSON et à sauvegarder les changements.

Vous découvrirez comment :

* ajouter une information ;
* modifier une information ;
* supprimer une information ;
* enregistrer les nouvelles données dans le fichier JSON.

## Projet

Vous allez mettre en œuvre un module permettant de gérer l'évolution des données JSON.

Par exemple :

```text
json_manager.py
```

ou :

```text
json_writer.py
```

## 🔄 Démarche

La modification d'un fichier JSON suit généralement le processus suivant :

```text
Fichier JSON
     ↓
Lecture
     ↓
Structure Python
     ↓
Modification
     ↓
Écriture
     ↓
Fichier JSON mis à jour
```

---

# 🚀 Progression de la séquence

```text
Structures de données Python
            │
            ▼
     S-PYTH-3001
  Fichiers et dossiers
            │
            ▼
     S-PYTH-3002
    Lecture de fichiers
            │
            ▼
     S-PYTH-3003
 Écriture et modification
            │
            ▼
 Persistance avec fichiers texte
            │
            ▼
     S-PYTH-3010
    Découverte de JSON
            │
            ▼
     S-PYTH-3011
 Lecture d'un fichier JSON
            │
            ▼
     S-PYTH-3012
 Modification des données JSON
```

---

# 🏆 Compétence visée

À l'issue de cette séquence, vous serez capable de :

> **Concevoir une application Python capable de conserver, retrouver et modifier durablement des données stockées sur le disque.**

Vous aurez appris à faire évoluer une application depuis une solution simple basée sur des fichiers texte vers une solution utilisant des **données structurées au format JSON**.

---

# 💡 Pourquoi cette séquence est importante ?

La persistance des données constitue une étape essentielle dans l'apprentissage du développement informatique.

Les notions étudiées dans cette séquence préparent directement à d'autres technologies utilisées dans les applications professionnelles :

* fichiers CSV ;
* fichiers JSON ;
* bases de données ;
* API ;
* services Web ;
* échanges de données entre applications.

Jusqu'à présent, vos programmes manipulaient principalement des **données temporaires en mémoire**.

Avec cette séquence, ils commencent à **conserver durablement leurs informations**.

```text
Mémoire
   ↓
Fichier texte
   ↓
JSON
   ↓
Base de données
   ↓
Application professionnelle
```

---

## 📌 Séquence

**Référence :** `S-PYTH-3000`
**Intitulé :** Persistance des données et échanges de fichiers
**Technologie principale :** Python
**Formats étudiés :** TXT, JSON
**Projet fil rouge :** Gestionnaire de notes
