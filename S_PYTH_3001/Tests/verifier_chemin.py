from S_PYTH_3001.file_manager import check_path
root = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes"
result = check_path(root, "dir")

if isinstance(result, dict):
    code = next(iter(result))
    print(f"Erreur {code} : {result[code]}")
elif result:
    print("Le répertoire existe.")
else:
    print("Le répertoire n'existe pas.")