import os

from S_PYTH_3001.updater_note import update_note_grade, update_note_reference

#-----------------------------------------
# test de la fonction update_note_date
#-----------------------------------------

#-----------------------------------------
# préparer le dossier en fonction de l'OS
#-----------------------------------------
if os.name == "nt":
    filename_txt = "C:\\Users\\stebar\\Python\\Gestion_Notes\\2026_toto_otto\\S_PYTH\\jan_notes.txt"
else:
    filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes/2026_toto_otto/S_PYTH/jan_notes.txt"


# grade = 25.0
# line = 0
# print(update_note_grade(filename_txt,line,grade))
# #{5: 'La note se trouve en dehors du domaine [0,20].'}
#
# grade = 25
# line = 0
# print(update_note_grade(filename_txt,line,grade))
# #{6: "Le paramètre 'grade' n'est pas un type float."}
#
# grade = -2.35
# line = 0
# print(update_note_grade(filename_txt,line,grade))
# #{5: 'La note se trouve en dehors du domaine [0,20].'}
#
# grade = "2,35"
# line = 0
# print(update_note_grade(filename_txt,line,grade))
# #{6: "Le paramètre 'grade' n'est pas un type float."}
#
# grade = 2.75
#
# for line in range(10):
#     print(update_note_grade(filename_txt,line,grade*(line+1.15)))


# ref = "S-100-pyth"
# line = 0
#
# # avant modification de la ligne 0
# #2026-01-03S-PYTH-3000-01EVALUATION10.50Travail correct, quelques notions restent à consolider.
# # --> S-PYTH-3000-01
#
#
# print(update_note_reference(filename_txt,line,ref))
# #{8: "Le nombre de caractères pour définir la référence n'est pas valide (il faut 14 caractères)."}
#
# ref = "s-ALGo-1285-01"
# print(update_note_reference(filename_txt,line,ref))
# #AVANT
# #2026-01-03S-PYTH-3000-01EVALUATION10.50Travail correct, quelques notions restent à consolider.
# #APRES
# #2026-01-03S-ALGO-1285-01EVALUATION10.50Travail correct, quelques notions restent à consolider.

