

"""
Date                update_note_date()
Référence.          update_note_reference()
Type                update_note_type()
Notes               update_note_grade()
Observation         update_note_observation()
"""
from datetime import datetime

from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.file_writer import replace_text_range
from S_PYTH_3001.note_constants import DATE_SIZE, LINE_SIZE, DATE_START, DATE_END


# prévoir de placer dans le futur cette fonction dans un module utils.py
def is_valid_date(str_date):
    """
    la docstring sera réalisée hors caméra et déposée dans le GitHub
    Args:
        str_date:

    Returns:

    """
    # le format utilisé sera yyyy-MM-DD
    # utiliser un objet de type datetime
    try:
        datetime.strptime(str_date,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def validat_update(filename, line, str_data):
    """
    la docstring sera réalisée hors caméra et déposée dans le GitHub
    Args:
        filename:
        line:
        str_data:

    Returns:

    """

    if not isinstance(filename, str):
        raise TypeError(
            print("Le paramètre 'filename' doit-être une chaine de caractères")
        )

    if not isinstance(line,int):
        raise TypeError(
            print("Le paramètre 'line' doit-être un entier.")
        )

    if not isinstance(str_data, str):
        raise TypeError(
            print("Le dernier paramètre doit-être une chaine de caractères")
        )

    if not check_path(filename, "file"):
        return {-1: "Le fichier n'existe pas"}

def update_note_date(filename, line, new_date ):
    """
    la docstring sera réalisée hors caméra et déposée dans le GitHub
    Args:
        filename:
        line:
        new_date:

    Returns:

    """

    validat_update(filename,line,new_date)

    if len(new_date) != DATE_SIZE:
        return {-2:"Le nombre de caractères pour définir la date n'est pas valide. (Il faut 10 caractères)."}

    if not is_valid_date(new_date):
        return {-3:"Erreur dans le format. Le format attendu est yyyy-MM-DD."}

    cursor = LINE_SIZE * line
    start = cursor + DATE_START
    end = cursor + DATE_END

    success = replace_text_range(filename, start, end + 1, new_date)

    if success:
        return {1:"Modification de la date réussie."}

    return {-4:"La modification de la date a échoué."}




