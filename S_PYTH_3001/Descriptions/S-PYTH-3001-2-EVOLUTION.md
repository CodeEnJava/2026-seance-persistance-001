# Évolution de la fonction `create_directory()`

Ce projet s'inscrit dans le cadre de la **Formation PQDI (Prépa Développeur - LADAPT)**. Il documente l'évolution de la fonction Python `create_directory()`, qui passe d'un retour booléen (`True`/`False`) à un **code de retour entier** (`1`, `0`, `-1`) afin de fournir une information plus riche au programme appelant.

---

## 📌 Contexte et Objectif

Jusqu'à présent, la fonction `create_directory()` indiquait uniquement si l'opération avait réussi ou échoué via une valeur booléenne. Cette information était insuffisante pour distinguer un répertoire déjà existant d'un échec de création.

La nouvelle version permet de qualifier précisément le résultat de l'opération :
* **Distinguer** un répertoire qui vient d'être créé d'un répertoire déjà existant.
* **Permettre au programme appelant d'adapter son comportement** selon la situation.
* **Introduire progressivement la notion de code de retour** pour les futures fonctions de gestion de fichiers et de données.

---

## ⚙️ Signature et Contrat de Retour

### Signature
```python
create_directory(root, directory_name)
```

### Codes de Retour

| Code de retour | Situation | Signification |
| :---: | :--- | :--- |
| **`1`** | **Création réussie** | Le répertoire n'existait pas et sa création a été réalisée avec succès. |
| **`0`** | **Répertoire déjà existant** | Le répertoire demandé existe déjà. Aucune création n'est nécessaire. |
| **`-1`** | **Échec de la création** | Opération impossible (paramètres invalides, racine inexistante ou non-répertoire, refus système ou erreur). |

---

## 🔀 Logique de Fonctionnement

Le déroulement général de la fonction suit l'arbre de décision suivant :

1. **Validation des paramètres** :
   * Si les paramètres sont invalides (ex: type non-chaîne) $\rightarrow$ **Retour : `-1`**
2. **Vérification de la racine (`root`)** :
   * Si la racine n'existe pas ou n'est pas un répertoire $\rightarrow$ **Retour : `-1`**
3. **Vérification du répertoire cible (`directory_name`)** :
   * Si le répertoire existe déjà $\rightarrow$ **Retour : `0`**
   * S'il n'existe pas, tentative de création :
     * En cas de succès $\rightarrow$ **Retour : `1`**
     * En cas d'échec (erreur système ou droits) $\rightarrow$ **Retour : `-1`**

---

## 🧪 Tests à Réaliser

Les tests suivants permettent de valider le respect du nouveau contrat de retour :

### Test 1 — Création d'un nouveau répertoire
* **Prérequis** : Supprimer au préalable le répertoire de test.
* **Appel** : `create_directory("C:\\Users\\stebar\\Python", "data")`
* **Résultat attendu** : `1`

### Test 2 — Répertoire déjà existant
* **Appel** : `create_directory("C:\\Users\\stebar\\Python", "data")` (exécuté une seconde fois)
* **Résultat attendu** : `0`

### Test 3 — Racine inexistante
* **Appel** : `create_directory("C:\\Users\\stebar\\Python\\inexistant", "data")`
* **Résultat attendu** : `-1`

### Test 4 — Paramètres invalides
* **Appels** : 
  * `create_directory(123, "data")` (premier paramètre non-chaîne)
  * `create_directory("C:\\Users\\stebar\\Python", 456)` (second paramètre non-chaîne)
* **Résultats attendus** : `-1`
