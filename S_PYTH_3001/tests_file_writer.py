from S_PYTH_3001.file_writer import (
    append_txt,
    prepend,
    add_txt,
    insert_text, get_cursor_position,
    get_cursor_start_position,
    get_cursor_end_position,
    insert_text_after_first_occurrence,
    insert_text_before_first_occurrence
)

filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"

# txt_end = "\nPour la suite des aventures avec les fichiers."

success = 0 #append_txt(filename_txt,txt_end)

if success == 1:
    print("Ajout du texte à la fin réussi.")
elif success == 0:
    print("Problème, ajout n'a pas pu être réalisé.")
else:
    print("Impossible le fichier n'existe pas.")

# test N°1
#le fichier /Users/steph.barois.dev/Downloads/python/exemple.txt n'existe pas.
#Impossible le fichier n'existe pas.
#/Users/steph.barois.dev/Downloads/python/Gestions

# test N°2
# Ajout du texte à la fin réussi.


# test pour ajouter au début du fichier

# text_begin = "Bonjour et bienvenue sur ma chaine CodeEnJava\n"

success = 0 #prepend(filename_txt,text_begin)

if success == 1:
    print("Ajout du texte au début.")
elif success == 0:
    print("Problème, ajout n'a pas pu être réalisé.")
else:
    print("Impossible le fichier n'existe pas.")

# test N°3

text_begin =" Mini projet : Gestionnaire de notes\n\n"
text_end = "\nA bientôt pour la suite des aventures avec CodeEnJava"

success = 0 #add_txt(filename_txt,text_begin,False)
if success == 1:
    print("Ajout du texte au début.")
elif success == 0:
    print("Problème, ajout n'a pas pu être réalisé.")
else:
    print("Impossible le fichier n'existe pas.")

success = 0 #add_txt(filename_txt,text_end)

if success == 1:
    print("Ajout du texte à la fin.")
elif success == 0:
    print("Problème, ajout n'a pas pu être réalisé.")
else:
    print("Impossible le fichier n'existe pas.")

