

"""
Date                update_note_date()
Référence.          update_note_reference()
Type                update_note_type()
Notes               update_note_grade()
Observation         update_note_observation()
"""
from datetime import datetime

from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.file_reader import read_text
from S_PYTH_3001.file_writer import replace_text_range
from S_PYTH_3001.note_constants import (
    DATE_SIZE,
    LINE_SIZE,
    DATE_START,
    DATE_END,
    REFERENCE_SIZE,
    REFERENCE_START,
    REFERENCE_END, TYPE_START, TYPE_END, GRADE_SIZE, GRADE_START, GRADE_END
)

dict_type = {"EVALUATION":"EVALUATION",
             "TP":"TP",
             "PROJET":"PROJET"}

# prévoir de placer dans le futur cette fonction dans un module utils.py
def is_valid_date(str_date):
    """
        Vérifie qu'une chaîne de caractères représente une date valide.

        La date doit respecter le format ISO suivant : YYYY-MM-DD.
        La validation est réalisée à l'aide de la méthode `strptime()`
        du module `datetime`.

        Args:
            str_date (str): Date à vérifier au format YYYY-MM-DD.

        Returns:
            bool: True si la date est valide et respecte le format attendu,
                sinon False.

        Examples:
            is_valid_date("2026-10-02")
            True
            is_valid_date("2026-02-30")
            False
            is_valid_date("02-10-2026")
            False
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
        Valide les paramètres nécessaires à la modification d'un
        enregistrement dans un fichier de notes.

        La fonction vérifie successivement le type du nom de fichier,
        le type du numéro de ligne, le type de la donnée à modifier
        ainsi que l'existence du fichier.

        Args:
            filename (str): Chemin complet ou relatif du fichier à modifier.
            line (int): Numéro de la ligne contenant l'enregistrement à modifier.
            str_data (str): Nouvelle donnée à utiliser lors de la modification.

        Returns:
            None | dict: Retourne un dictionnaire contenant un code d'erreur
                et un message si le fichier n'existe pas. Si les validations
                sont correctes, la fonction ne retourne aucune valeur.

        Raises:
            TypeError: Si `filename` n'est pas une chaîne de caractères.
            TypeError: Si `line` n'est pas un entier.
            TypeError: Si `str_data` n'est pas une chaîne de caractères.

        Examples:
            validat_update("notes.txt", 0, "2026-10-02")
            None
        """

    if not isinstance(filename, str):
        raise TypeError(
            "Le paramètre 'filename' doit-être une chaine de caractères"
        )

    if not isinstance(line,int):
        raise TypeError(
            "Le paramètre 'line' doit-être un entier."
        )

    if not isinstance(str_data, str):
        raise TypeError(
            "Le dernier paramètre doit-être une chaine de caractères"
        )

    if not check_path(filename, "file"):
        return {-1: "Le fichier n'existe pas"}

def update_note_date(filename, line, new_date ):
    """
        Modifie la date d'un enregistrement dans un fichier de notes.

        La fonction vérifie les paramètres nécessaires à la modification,
        contrôle la longueur de la nouvelle date ainsi que son format,
        puis remplace la date existante dans l'enregistrement indiqué.

        La date doit respecter le format YYYY-MM-DD et contenir exactement
        10 caractères.

        Args:
            filename (str): Chemin complet ou relatif du fichier contenant
                les notes.
            line (int): Numéro de la ligne contenant la note à modifier.
            new_date (str): Nouvelle date au format YYYY-MM-DD.

        Returns:
            dict: Dictionnaire contenant un code et un message indiquant
                le résultat de la modification.

                Codes de retour :
                    1 : Modification de la date réussie.
                   -1 : Le fichier n'existe pas.
                   -2 : La date ne contient pas 10 caractères.
                   -3 : Le format de la date est incorrect.
                   -4 : La modification de la date a échoué.

        Raises:
            TypeError: Si l'un des paramètres ne respecte pas le type attendu.

        Examples:
            update_note_date("jan_notes.txt", 0, "2026-10-02")
            {1: 'Modification de la date réussie.'}

            update_note_date("jan_notes.txt", 0, "2026-02-30")
            {-3: 'Erreur dans le format. Le format attendu est yyyy-MM-dd.'}
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


#----------------------------------------------
# Modification d'une note que l'on nomme GRADE
#----------------------------------------------

def is_float(grade):
    """

    Args:
        grade:

    Returns:

    """
    return isinstance(grade,float)

# il faut vérifier que la note [0,20]

def validate_grade(grade):
    """

    Args:
        grade:

    Returns:

    """
    if is_float(grade):
        if 0 <= grade <= 20:
            return {1:"La note est valide."}
        else:
            return {5:"La note se trouve en dehors du domaine [0,20]."}
    return {6: "Le paramètre 'grade' n'est pas un type float."}


def normalise_grade(grade):
    """

    Args:
        grade:

    Returns:

    """

    status_grade = validate_grade(grade)

    if 1 not in status_grade:
        return status_grade

    # arrondir avec deux chiffres après la virgule
    grade_normalised = round(grade, 2)
    str_grade = str(grade_normalised)

    pos_dec_point = str_grade.find('.')

    if pos_dec_point == -1:
        return {7:"Erreur dans la fonction normalise_grade."}

    print(f"str_grade = {str_grade}")

    left = str_grade[:pos_dec_point]
    right = str_grade[pos_dec_point+1:]

    if len(left) == 1:
        left = "0" + left
    if len(right) == 1:
        right = right + "0"

    return left + "." + right

def update_note_grade(filename,line,grade):

    str_grade_normalised = normalise_grade(grade)

    if isinstance(str_grade_normalised, dict):
        return str_grade_normalised

    # on peut modifier la note 'grade'

    cursor = LINE_SIZE * line
    start = cursor + GRADE_START
    end = cursor + GRADE_END

    success = replace_text_range(filename, start, end + 1, str_grade_normalised)

    if success:
        return {1: "Modification de la note réussie."}

    return {-4: "La modification de la note a échoué."}

#-------------------------------------------------
# Modifier une référence associée à une note
#-------------------------------------------------

def is_validat_size_data(data, size):
    """

    Args:
        data:
        size:

    Returns:

    """
    return len(data) ==  size

def is_exist_ref(filename, ref):
    """

    Args:
        filename:
        ref:

    Returns:

    """
    data_notes = read_text(filename)
    return data_notes.find(ref) != -1

def update_note_reference(filename, line, ref):
    """

    Args:
        filename:
        line:
        ref:

    Returns:

    """
    status_update = validat_update(filename,line,ref)

    if isinstance(status_update, dict):
        return status_update

    is_validat_size = is_validat_size_data(ref, REFERENCE_SIZE)

    if not is_validat_size:
        return {
            8: f"Le nombre de caractères pour définir la référence n'est pas valide"
               f" (il faut {REFERENCE_SIZE} caractères)."
        }

    if is_exist_ref(filename,ref):
        return {
            9: "Impossible, cette référence est déjà attribuée dans ce fichier."
        }
    cursor = LINE_SIZE * line
    start = cursor + REFERENCE_START
    end = cursor + REFERENCE_END

    success = replace_text_range(filename,start,end + 1, str(ref).upper())

    if success:
        return {1: "Modification de la référence réussie."}

    return {-4: "La modification de la référence a échoué."}

#-------------------------------------------
# Modifier le type d'une note en utilisant
# un type prédéfini {EVALUATION, PROJET, TP}
#-------------------------------------------

set_type ={
    "EVALUATION",
    "PROJET",
    "TP"
}

def is_validat_type(new_type):
    """

    Args:
        new_type:

    Returns:

    """
    upper_type = str(new_type).upper()
    if upper_type in set_type:
        return True
    else:
        return False

def update_note_type(filename,line,new_type):

    status_validate = validat_update(filename,line,new_type)

    if isinstance(status_validate, dict):
        return status_validate

    if not is_validat_type(new_type):
        return {
            10 : "Ce type de note n'est pas valide."
        }
    # normalisation du type
    new_type = str(new_type).upper()

    cursor = LINE_SIZE * line
    start = cursor + TYPE_START
    end = cursor + TYPE_END

    success = replace_text_range(filename, start, end + 1, new_type)

    if success:
        return {1: "Modification du type réussie."}

    return {-4: "La modification du type a échoué."}