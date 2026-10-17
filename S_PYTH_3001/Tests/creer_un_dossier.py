from S_PYTH_3001.file_manager import create_directory
root = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes"
result = create_directory(root, "2026_MARTIN_Sophie")

if isinstance(result, dict):
    code = next(iter(result))
    print(result[code])
elif result == 1:
    print("Répertoire créé.")
elif result == 0:
    print("Le répertoire existe déjà.")
elif result == -1:
    print("La racine n'existe pas.")