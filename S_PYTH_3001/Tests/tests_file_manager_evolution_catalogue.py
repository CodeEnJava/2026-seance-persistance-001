
"""
Module de tests du module file_manager.

Objectif :
    Vérifier le fonctionnement des fonctions de gestion
    des fichiers et contrôler les résultats retournés.

Les tests utilisent un répertoire temporaire afin de
ne pas modifier les fichiers de travail de l'utilisateur.
"""

import os
import shutil
import tempfile

from S_PYTH_3001.file_manager import (
    create_file,
    delete_file, check_path
)
from S_PYTH_3001.file_reader import read_text
from S_PYTH_3001.file_writer import add_txt

#-----------------------------------------
# préparer la racine en fonction de l'OS
#-----------------------------------------
if os.name == "nt":
    root = r"C:\Users\STEPHANE.BAROIS\Python"
else:
    root = r"/Users/steph.barois.dev/Downloads/python/"

# ============================================================
# INITIALISATION DES TESTS
# ============================================================

# Création d'un répertoire temporaire pour les tests.
TEST_DIRECTORY = os.path.join(root, "test_file_manager")

# Supprimer le répertoire s'il existe déjà.
if check_path(TEST_DIRECTORY).get("data"):
    shutil.rmtree(TEST_DIRECTORY)

# Créer le répertoire de tests.
os.makedirs(TEST_DIRECTORY)


# Définition  des fichiers de test.
FILE_TEST_1 = "test_1.txt"
FILE_TEST_2 = "test_2.txt"

# Définition des chemins complets des fichiers de test
PATH_FILE_TEST_1 = os.path.join(TEST_DIRECTORY, FILE_TEST_1)
PATH_FILE_TEST_2 = os.path.join(TEST_DIRECTORY, FILE_TEST_2)


# Texte utilisé pour les tests de lecture et d'écriture.
TEST_CONTENT = "Test du module file_manager."


# ============================================================
# TEST 1 : CRÉATION D'UN FICHIER
# ============================================================

print("\nTEST 1 : CRÉATION D'UN FICHIER")
print("-" * 50)

result = create_file(TEST_DIRECTORY,FILE_TEST_1)

print("Fonction testée : create_file")
print(f"Fichier : {FILE_TEST_1}")
print(f"Résultat : {result}")


# ============================================================
# TEST 2 : ÉCRITURE DANS UN FICHIER
# ============================================================

print("\nTEST 2 : ÉCRITURE DANS UN FICHIER")
print("-" * 50)

result = add_txt(PATH_FILE_TEST_1, TEST_CONTENT)

print("Fonction testée : write_file")
print(f"Contenu écrit : {TEST_CONTENT}")
print(f"Résultat : {result}")


# ============================================================
# TEST 3 : LECTURE D'UN FICHIER
# ============================================================

print("\nTEST 3 : LECTURE D'UN FICHIER")
print("-" * 50)

result = read_text(PATH_FILE_TEST_1)

print("Fonction testée : read_file")
print(f"Contenu lu : {result}")


# ============================================================
# TEST 4 : LECTURE D'UN FICHIER INEXISTANT
# ============================================================

print("\nTEST 4 : LECTURE D'UN FICHIER INEXISTANT")
print("-" * 50)

result = read_text(
    os.path.join(TEST_DIRECTORY, "inexistant.txt")
)

print("Fonction testée : read_file")
print(f"Résultat : {result}")


# ============================================================
# TEST 5 : SUPPRESSION D'UN FICHIER
# ============================================================

print("\nTEST 5 : SUPPRESSION D'UN FICHIER")
print("-" * 50)

result = delete_file(PATH_FILE_TEST_1)

print("Fonction testée : delete_file")
print(f"Résultat : {result}")


# ============================================================
# TEST 6 : SUPPRESSION D'UN FICHIER INEXISTANT
# ============================================================

print("\nTEST 6 : SUPPRESSION D'UN FICHIER INEXISTANT")
print("-" * 50)

result = delete_file(PATH_FILE_TEST_1)

print("Fonction testée : delete_file")
print(f"Résultat : {result}")


# ============================================================
# NETTOYAGE
# ============================================================

print("\nNETTOYAGE DES TESTS")
print("-" * 50)

# Suppression des éventuels fichiers restants.
for filename in os.listdir(TEST_DIRECTORY):
    filepath = os.path.join(TEST_DIRECTORY, filename)

    if os.path.isfile(filepath):
        os.remove(filepath)

# Suppression du répertoire temporaire.
os.rmdir(TEST_DIRECTORY)

print("Répertoire temporaire supprimé.")
print("Fin des tests.")
