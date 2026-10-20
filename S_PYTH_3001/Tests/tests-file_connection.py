
"""
Module de test des connexions aux fichiers.

Vérifie l'ouverture et la fermeture de fichiers en mode binaire
et en mode texte, à l'aide des fonctions du module file_connection.

Les résultats des opérations sont affichés à partir des messages
retournés par le catalogue centralisé.
"""

from S_PYTH_3001.file_connection import (
    open_connection,
    close_connection,
    BINARY_WRITE_READ_MODE,
    READ_ONLY_MODE
)


# --------------------------------------------------
# 1. Définition des chemins des fichiers à tester
# --------------------------------------------------

path_binary = r"C:\Users\STEPHANE.BAROIS\Python\exemple_1.txt"
path_text = r"C:\Users\STEPHANE.BAROIS\Python\exemple.txt"


# --------------------------------------------------
# 2. Ouverture des connexions
# --------------------------------------------------

connection_binary = open_connection(
    path_binary,
    BINARY_WRITE_READ_MODE
)

connection_text = open_connection(
    path_text,
    READ_ONLY_MODE
)


# --------------------------------------------------
# 3. Affichage des résultats d'ouverture
# --------------------------------------------------

print("=== Résultat de l'ouverture en mode binaire ===")
print(connection_binary.get("message"))

print("\n=== Résultat de l'ouverture en mode texte ===")
print(connection_text.get("message"))
print()

# --------------------------------------------------
# 4. Fermeture des connexions ouvertes
# --------------------------------------------------

if connection_binary.get("data") is not None:
    result_close_binary = close_connection(connection_binary)
    print(result_close_binary.get("message"))

if connection_text.get("data") is not None:
    result_close_text = close_connection(connection_text)
    print(result_close_text.get("message"))
