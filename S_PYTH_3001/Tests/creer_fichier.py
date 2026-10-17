

from S_PYTH_3001.file_manager import create_file
root = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes"
result = create_file(
    root,
    "notes.txt",
    "utf-8"
)

if isinstance(result, dict):
    code = next(iter(result))
    print(result[code])
elif result is True:
    print("Fichier créé.")
elif result is None:
    print("Le fichier existe déjà.")