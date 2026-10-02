import os

from S_PYTH_3001.file_manager import create_file, check_path
from S_PYTH_3001.file_reader import read_text
from S_PYTH_3001.file_writer import add_txt, get_file_size, pad_text

###############################################################
#    Préparation du test
###############################################################

# structure d'une note

"""

┌──────────┬────────────────┬──────────┬─────┬────────────────────────────────────┐
│ Date     │ Référence      │ Type     │Note │ Observation                        │
│ 10 oct.  │ 14 octets      │ 10 oct.  │5    │ 100 octets                         │
└──────────┴────────────────┴──────────┴─────┴────────────────────────────────────┘

                         Taille totale : 139 octets
                         
2026-01-03S-PYTH-3000-01EVALUATION10.50Travail correct, quelques notions restent à consolider.                                             
2026-01-03S-PYTH-3000-01EVALUATION10.50Travail correct, quelques notions restent à consolider.                                             


Structure
Champ       Format                 Taille      DEBUT       FIN
date        yyyy-mm-dd             10 octets   0           9
reference   S-PYTH-3000-00         14 octets   10          23
type        EVALUATION, TP, PROJET 10 octets   24          33
note        ##.##                  5 octets    34          38
observation texte                  100 octets  39          128
Total                              139 octets
"""


# Préparer les notes
note_1 = "2026-01-03S-PYTH-3000-01EVALUATION10.50Travail correct, quelques notions restent à consolider."
note_2 = "2026-01-05S-PYTH-3000-02PROJET    15.50Très bon travail sur la lecture des fichiers."
note_3 = "2026-01-08S-PYTH-3000-03TP        12.00Travail satisfaisant, les bases sont acquises."
note_4 = "2026-01-12S-PYTH-3000-04EVALUATION08.50Des difficultés persistent, les notions sont à revoir."
note_5 = "2026-01-15S-PYTH-3000-05TP        14.00Bon travail, les notions principales sont maîtrisées."
note_6 = "2026-01-20S-PYTH-3000-06PROJET    17.50Excellent travail, les objectifs sont très bien atteints."
note_7 = "2026-01-23S-PYTH-3000-07EVALUATION11.50Résultat satisfaisant, certains points restent à consolider."
note_8 = "2026-01-27S-PYTH-3000-08TP        09.00Les bases sont présentes, mais le travail doit être approfondi."
note_9 = "2026-01-30S-PYTH-3000-09PROJET    13.50Bon résultat, poursuivre les efforts pour progresser."
note_10 = "2026-02-03S-PYTH-3000-10EVALUATION16.00Très bon résultat, les compétences sont bien maîtrisées."

# injecter les notes dans une liste

list_notes = [
    note_1,
    note_2,
    note_3,
    note_4,
    note_5,
    note_6,
    note_7,
    note_8,
    note_9,
    note_10
]

# préparer le dossier en fonction de l'OS
if os.name == "nt":
    path_txt = "C:\\Users\\stebar\\Python\\Gestion_Notes\\2026_toto_otto\\S_PYTH"
else:
    path_txt = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes/2026_toto_otto/S_PYTH"

# préparer le fichier txt pour les notes du mois de janvier
file_jan = "jan_notes.txt"

# injecter les données dans le fichier "jan_notes.txt"
filename = os.path.join(path_txt,file_jan)

if not check_path(filename,"file"):
    create_file(path_txt,file_jan)

max_note_size = 139
# injection des datas dans le fichier si celui-ci est vide
if get_file_size(filename) == 0:
    for note in list_notes:
        success = add_txt(filename,pad_text(note,max_note_size)+"\n")
        if success == 1:
            print("Ajout de la note réussie")
        elif success == 0:
            print("Echec dans l'ajout de la note")
        else:
            print("Erreur: le fichier n'existe pas")
else:
    print("le fichier contient déjà des données pour le test")


# lire le contenu du fichier

data = read_text(filename)
if data:
    print(data)
else:
    print("Erreur dans le fichier")

