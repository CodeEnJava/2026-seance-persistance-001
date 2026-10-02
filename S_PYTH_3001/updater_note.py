

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




