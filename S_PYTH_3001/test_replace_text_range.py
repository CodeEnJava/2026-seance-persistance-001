import os

from S_PYTH_3001.file_reader import read_text
from S_PYTH_3001.file_writer import replace_text_range

# préparer le dossier en fonction de l'OS
if os.name == "nt":
    filename_txt = "C:\\Users\\stebar\\Python\\Gestion_Notes\\2026_toto_otto\\S_PYTH\\jan_notes.txt"
else:
    filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes/2026_toto_otto/S_PYTH/jan_notes.txt"


# print(read_text(filename_txt))
# type        EVALUATION, TP, PROJET 10 octets   24          33
LINE_SIZE = 140
line = 7
cursor = LINE_SIZE * line

# pour la modification des dates
#start = cursor + 0
#end = cursor + 9

start = cursor + 24
end = cursor + 33

# mise en place de la modification pour la date
# new_date = "YYYY-MM-DD"
new_type = "PROJET"


print(replace_text_range(filename_txt,start,end + 1,new_type))

print(read_text(filename_txt))





