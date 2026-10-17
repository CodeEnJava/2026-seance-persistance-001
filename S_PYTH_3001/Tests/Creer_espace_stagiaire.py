from S_PYTH_3001.file_manager import add_trainee
root = "/Users/steph.barois.dev/Downloads/python/Gestion_Notes"
result = add_trainee(
    root,
    "MARTIN_Sophie"
)

if isinstance(result, dict) and len(result) == 1:
    code = next(iter(result))

    if isinstance(code, int):
        # Un dictionnaire d'erreur du catalogue
        print(result[code])
    else:
        # Résultats détaillés de création
        print(result)
else:
    print(result)