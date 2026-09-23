from S_PYTH_3001.file_writer import (
    insert_text,
    get_cursor_position,
    get_cursor_end_position,
    get_cursor_start_position,
    insert_text_after_first_occurrence,
    insert_text_before_first_occurrence
)

"""
Mini projet : Gestionnaire de notes

Bonjour et bienvenue sur ma chaine CodeEnJava
Première ligne Bonjour
Seconde ligne  Tout va bien
Troisième ligne A bientôt.

Pour la suite des aventures avec les fichiers.
"""


# il faut ajouter le texte suivant ' Toto' après le curseur (105)

# left <-  Mini projet : Gestionnaire de notes
#
# Bonjour et bienvenue sur ma chaine CodeEnJava
# Première ligne Bonjour

# right <-
#Seconde ligne  Tout va bien
#roisième ligne A bientôt.
#
#Pour la suite des aventures avec les fichiers.

# nouveau text = left + ' Toto' + right

#filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"
filename_txt = "C:\\Users\\stebar\\Python\\Gestions\\exemple.txt"
cursor = 105

sequence = " Toto"

insert_text(filename_txt,sequence,cursor)



