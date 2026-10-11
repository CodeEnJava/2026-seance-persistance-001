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
                         

Structure
Champ       Format                 Taille      DEBUT       FIN
date        yyyy-mm-dd             10 octets   0           9
reference   S-PYTH-3000-00         14 octets   10          23
type        EVALUATION, TP, PROJET 10 octets   24          33
note        ##.##                  5 octets    34          38
observation texte                  100 octets  39          138
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

MAX_NOTE_SIZE = 139
# injection des datas dans le fichier si celui-ci est vide
if get_file_size(filename) == 0:
    for note in list_notes:
        success = add_txt(filename,pad_text(note,MAX_NOTE_SIZE)+"\n")
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

"""
000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028
  2   0   2   6   -   0   1   -   0   3   S   -   P   Y   T   H   -   3   0   0   0  -    0   1   E   V   A   L   U
029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 053 054 055 056 057  
  A   T   I   O   N   1   0   .   5   0   T   r   a   v   a   i   l       c   o   r   r   e   c   t   ,   q   u   e   
058 059 060 061 062 063 064 065 066 067 068 069 070 071 072 073 074 075 076 077 078 079 080 081 082 083 084 085 086  
  l   q   u   e   s       n   o   t   i   o   n   s       r   e   s   t   e   n   t       à       c   o   n   s   o   
087 088 089 090 091 092 093 094 095 096 097 098 099 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115  
  l   i   d   e   r   .                                                                                                                     
116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144
                                                                                                 \n   2   0   2   6
145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173                                                                                                
  -   0   1   -   0   5   S   -   P   Y   T   H   -   3   0   0   0   -   0   2   P   R   O   J   E   T           1
174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 495 196 197 198 199 200 201 202
      5   .   5.  0   T   r   è   s       b   o   n       t   r   a   v   a   i   l       s   u   r       l   a 
203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231
  l   e   c   t   u   r   e       d   e   s       f   i   c   h   i   e   r   s   .

                                                        
2026-01-08S-PYTH-3000-03TP        12.00Travail satisfaisant, les bases sont acquises.                                                      
2026-01-12S-PYTH-3000-04EVALUATION08.50Des difficultés persistent, les notions sont à revoir.                                              
2026-01-15S-PYTH-3000-05TP        14.00Bon travail, les notions principales sont maîtrisées.                                               
2026-01-20S-PYTH-3000-06PROJET    17.50Excellent travail, les objectifs sont très bien atteints.                                           
2026-01-23S-PYTH-3000-07EVALUATION11.50Résultat satisfaisant, certains points restent à consolider.                                        
2026-01-27S-PYTH-3000-08TP        09.00Les bases sont présentes, mais le travail doit être approfondi.                                     
2026-01-30S-PYTH-3000-09PROJET    13.50Bon résultat, poursuivre les efforts pour progresser.                                               
2026-02-03S-PYTH-3000-10EVALUATION16.00Très bon résultat, les compétences sont bien maîtrisées.                                            

"""