import os

from S_PYTH_3001.updater_note import update_note_date

# préparer le dossier en fonction de l'OS
if os.name == "nt":
    filename_txt = "C:\\Users\\stebar\\Python\\Gestion_Notes\\2026_toto_otto\\S_PYTH\\jan_notes.txt"
else:
    filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes/2026_toto_otto/S_PYTH/jan_notes.txt"

# test de la fonction update_note_date

line = 0
new_date = "2025-05-25"
print(update_note_date(filename_txt,line ,new_date))

new_date = "20/05/2000"
print(update_note_date(filename_txt,line ,new_date))

new_date = "200/05/2000"
print(update_note_date(filename_txt,line ,new_date))

new_date = "2025-15-25"
print(update_note_date(filename_txt,line ,new_date))

line = 9
new_date = "2000-12-23"
print(update_note_date(filename_txt,line ,new_date))

line = 8
new_date = "2010-10-10"
print(update_note_date(filename_txt,line ,new_date))