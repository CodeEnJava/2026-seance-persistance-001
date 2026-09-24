
from S_PYTH_3001.file_writer import replace_text

# filename_text = "C:\\Users\\stebar\\Python\\Gestions\\exemple.txt"
filename_text ="/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"

#################################################
# Tests du correctif de la fonction replace_text
#################################################
"""
voici le résultat des différents tests réalisés

Mini projet : gestionnaire de notes

bonjour et bienvenue sur la chaine youtube python 

première ligne bonjour
seconde ligne  tu vas bien
troisième ligne à bientôt
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

old_text = "ligne"
new_text = "plage"

result = replace_text(filename_text,old_text,new_text,True)
print(result)
