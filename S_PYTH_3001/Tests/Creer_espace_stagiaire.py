import os

from S_PYTH_3001.file_manager import add_trainee


#-----------------------------------------
# préparer le dossier en fonction de l'OS
#-----------------------------------------
if os.name == "nt":
    root = r"C:\Users\STEPHANE.BAROIS\Python"
else:
    root = r"/Users/steph.barois.dev/Downloads/python/"

result = add_trainee(
    root,
    "TOTO_Otto"
)

