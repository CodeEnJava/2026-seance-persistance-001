import os

from S_PYTH_3001.file_writer import count_carriage_return, modify_text_range
from S_PYTH_3001.note_constants import LINE_SIZE, OBSERVATION_START, OBSERVATION_SIZE
from S_PYTH_3001.updater_note import update_note_observation

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

# line = 0
# new_type = "td"
#
# print(update_note_type(filename_txt,line,new_type))
# #{10: "Ce type de note n'est pas valide."}



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
# grade = 1.75
#
# for line in range(10):
#     print(update_note_grade(filename_txt,line,grade*(line+1.15)))
#

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

# line = 0
# new_type = "td"
#
# print(update_note_type(filename_txt,line,new_type))
# #{10: "Ce type de note n'est pas valide."}
#
# new_type = "projet"
# # AVANT
# #2026-01-03S-ALGO-1285-01EVALUATION10.50Travail correct, quelques notions restent à consolider.
# print(update_note_type(filename_txt,line,new_type))
# #{1: 'Modification du type réussie.'}
# #2026-01-03S-ALGO-1285-01PROJET    10.50Travail correct, quelques notions restent à consolider.
#
# new_type = "tp"
#
# for line in range(10):
#     print(update_note_type(filename_txt, line, new_type))

#
# new_type = "projet"
# # AVANT
# #2026-01-03S-ALGO-1285-01EVALUATION10.50Travail correct, quelques notions restent à consolider.
# print(update_note_type(filename_txt,line,new_type))
# #{1: 'Modification du type réussie.'}
# #2026-01-03S-ALGO-1285-01PROJET    10.50Travail correct, quelques notions demeurent à consolider.
#
# new_type = "tp"
#
# for line in range(10):
#     print(update_note_type(filename_txt, line, new_type))

# # mettre la même date pour l'ensemble des notes
# str_date = "2026-10-02"
# for line in range(10):
#     print(update_note_date(filename_txt,line,str_date))
#
# # modifier la référence
# str_ref = "S-PYTH-2560-0"
# for line in range(10):
#     print(update_note_reference(filename_txt,line,str_ref + str(line)))
#
# # mettre le mettre type pour toutes les notes
# new_type = "projet"
# for line in range(10):
#     print(update_note_type(filename_txt,line,new_type))
#
# # mettre la même note à tous
# grade = 8.1
# for line in range(10):
#     print(update_note_grade(filename_txt,line,grade))
#


# dans le fichier, on utilise l'encodage utf-8.
def affichage_informations(str_info):
    print(f"message = {str_info}")
    print(f" size : {len(str_info)} caractères(s)")
    print(f" size : {len(str_info.encode('utf-8'))} octet(s)")
    print("-" * 25)

observation = "A"
affichage_informations(observation)

observation = "é"
affichage_informations(observation)

observation = ""
affichage_informations(observation)

observation = "😊"
affichage_informations(observation)

observation = "Travail correct, quelques notions restent à consolider."
affichage_informations(observation)

# occupation d'un caractère est dynamique entre 1 octet et 4 octets
    # exemple :
    # | Caractère | Nombre d'octets UTF-8 |
    # | --------- | --------------------: |
    # | `A`       |                     1 |
    # | `é`       |                     2 |
    # | `€`       |                     3 |
    # | `😊`      |                     4 |
    # | --------- | --------------------: |

#-----------------------------------------
# Tester la modification d'une observation
#-----------------------------------------

observation = (
    " Dans l'ensemble, un bon travail, "
    "les notions principales sont maîtrisées. "
)

print("Observation avant modification :")
affichage_informations(observation)

observation_normalisee = observation.lstrip()

print("Observation après normalisation :")
affichage_informations(observation_normalisee)
affichage_informations(observation)

observation_normalisee = observation.strip()

print("Observation après normalisation :")
affichage_informations(observation_normalisee)

# --------------------------------------------
# test de la fonction modify_text_range
# --------------------------------------------
text = "Bon travail, mais il faut persévérer."


# for line  in range(10):
#     cursor = LINE_SIZE * line
#     start = cursor + OBSERVATION_START
#
#     nb_cr = count_carriage_return(filename_txt,0, start)
#
#     if isinstance(nb_cr,dict):
#         print("Erreur ")
#     else:
#         start += nb_cr
#         end = start + OBSERVATION_SIZE
#         print(modify_text_range(filename_txt, start, end, text))

# --------------------------------------------
# test de la fonction update_note_observation
# --------------------------------------------
line = 9

text = " Ne lâcher rien, les efforts vont payer. "

print(update_note_observation(filename_txt, line, text))


