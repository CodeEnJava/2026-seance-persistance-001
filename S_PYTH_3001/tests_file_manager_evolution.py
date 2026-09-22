import os.path

from S_PYTH_3001.file_manager import (
    create_file,
    delete_file
)

# tests pour ajouter un nouveau fichier

path = "C:\\Users\\stebar\\Python\\Gestions"

exemple_1 = "exemple_3.txt"
exemple_binaire = "binaire_3.bin"

success = create_file(path,exemple_1,"utf-8")
if success:
    print(f"Le fichier {exemple_1} a été créé.")
else:
    print(f"Le fichier {exemple_1} n'a pas été créé.")

# neutraliser le bloc suivant pour tester la fonction delete_file
#success = create_file(path, exemple_binaire)
#if success:
#    print(f"Le fichier {exemple_binaire} a été créé.")
#else:
#    print(f"Le fichier {exemple_binaire} n'a pas été créé.")

# test de la fonction delete_file
filename_3 = os.path.join(path,exemple_binaire)
delete = delete_file(filename_3)

if delete:
    print(f"Le fichier {filename_3} a été supprimé.")
else:
    print(f"le fichier {filename_3} n'a pas pu être supprimé.")

