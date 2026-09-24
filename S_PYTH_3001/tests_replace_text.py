

"""
contenu du fichier texte pour les tests

Mini projet : Gestionnaire de notes

Bonjour et bienvenue chaine CodeEnJava

Première ligne Bonjour
Seconde ligne  tu vas bien
Troisième ligne A bientôt.

Pour la suite des aventures avec les fichiers.
"""
from S_PYTH_3001.file_writer import replace_text

# filename_text = "C:\\Users\\stebar\\Python\\Gestions\\exemple.txt"
filename_text ="/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"

"""
voici le résultat des différents tests réalisés

Mini projet : gestionnaire de notes

bonjour et bienvenue sur la chaine youtube python 

première ligne bonjour
seconde ligne  tu vas bien
troisième ligne à bientôt
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

old_text = "3"
new_text = "0"

result = replace_text(filename_text,old_text,new_text,True)
print(result)
