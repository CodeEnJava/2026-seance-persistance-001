"""
Tests du module `reader`.

Ce module permet de tester la lecture de fichiers texte et binaires
à l'aide des fonctions fournies par le module `reader`.

Les tests permettent notamment de vérifier :

- l'ouverture d'un fichier existant ;
- la lecture d'un fichier texte à partir d'une connexion ouverte ;
- la lecture d'un fichier texte directement avec `read_text()` ;
- la lecture d'un fichier binaire avec `read_binary()` ;
- le comportement du programme lorsqu'un fichier n'existe pas.
"""

# =============================================================
# Imports
# =============================================================

from file_connection import (
    open_connection,
    READ_ONLY_MODE
)
from reader import (
    read_text,
    read_text_aux,
    read_binary,
    DATA,
    ERROR
)





# =============================================================
# Test 1 : lecture d'un fichier texte à partir d'une connexion
# =============================================================

filename = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"

# Pour générer une erreur, activer la ligne suivante :
# filename = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple1.txt"

file_cnx = open_connection(filename, READ_ONLY_MODE)

if file_cnx is not None:

    read = read_text_aux(file_cnx)

    if read[DATA] is not None:
        print("OK")
        print(read[DATA])
    else:
        print("PAS OK")
        print(read[ERROR])

else:
    print(f"Le fichier {filename}\nn'existe pas...")


# =============================================================
# Test 2 : lecture directe d'un fichier texte
# =============================================================

texte = read_text(filename)

print(texte)


# =============================================================
# Test 3 : lecture d'un fichier binaire
# =============================================================

filename_image = "/Users/steph.barois.dev/Downloads/python/Gestions/image.png"

# Pour générer une erreur, activer la ligne suivante :
# filename_image = "/Users/steph.barois.dev/Downloads/python/Gestions/image.gnp"

binaire = read_binary(filename_image)

print(binaire)
