

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

filename_text = "C:\\Users\\stebar\\Python\\Gestions\\exemple.txt"





"""
voici le résultat des différents tests réalisés

Le projet : Gestionnaire de notes

Bonjour et bienvenue sur la chaine Youtube Python 

Première ligne Bonjour
Seconde ligne  tu vas bien
Troisième ligne A bientôt.

Pour la suite des histoires pour fichiers.
"""

# le dernier test:
old_text = "disque"
new_text = "disque dur"

result = replace_text(filename_text,old_text,new_text)
print(result)