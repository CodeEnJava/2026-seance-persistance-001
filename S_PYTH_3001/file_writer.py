from S_PYTH_3001.file_connection import open_connection, close_connection
from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.file_reader import read_text, read_char_range, size
from S_PYTH_3001.params_connection import APPEND_MODE, WRITE_READ_MODE, READ_WRITE_MODE, WRITE_ONLY_MODE, READ_ONLY_MODE



# une fonction pour ajouter du texte à la fin d'un fichier
# une fonction pour ajouter du texte au début du fichier
# une fonction qui permet de choisir à la fin ou au debut

def append_txt(filename, txt):
    """
        Ajoute un texte à la fin d'un fichier existant.
        La fonction vérifie le type des paramètres ainsi que l'existence
        du fichier avant d'ouvrir celui-ci en mode ajout.

        Le contenu fourni est alors ajouté à la fin du fichier sans modifier son contenu existant.

        Args:
            filename (str): Chemin complet du fichier dans lequel le texte doit être ajouté.
            txt (str): Texte à ajouter à la fin du fichier.

        Returns: int:   - 1 si le texte a été ajouté avec succès.
                        - 0 si l'ouverture du fichier a échoué.
                        - -1 si le fichier n'existe pas.

        Raises: TypeError: Si `filename` ou `txt` n'est pas une chaîne de caractères.
    """
    if not isinstance(filename,str):
        raise TypeError(
            "Le premier paramètre doit-être une chaine de caractères, contenant le nom du fichier"
            "complet."
        )

    if not isinstance(filename,str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant "
            "le texte à ajouter à la fin du fichier."
        )

    if not check_path(filename,"file"):
        print(f" le fichier {filename} n'existe pas.")
        return -1

    obj_cnx = open_connection(filename,APPEND_MODE)

    if obj_cnx:
        obj_cnx.write(txt)
        close_connection(obj_cnx)
        return 1
    else:
        print("Un problème lors de la réalisation de l'objet de connexion.")
        return 0


def prepend(filename,txt):
    """
        Ajoute un texte au début d'un fichier existant.
        La fonction lit d'abord le contenu actuel du fichier, puis réécrit
        le fichier avec le nouveau texte placé au début. Le contenu initial
        du fichier est ensuite ajouté à la suite du nouveau texte.

        Cette méthode est adaptée aux fichiers de petite taille,
        car l'intégralité du contenu du fichier est temporairement chargée en mémoire.

        Args:
            filename (str): Chemin complet du fichier dans lequel le texte doit être ajouté.
            txt (str): Texte à ajouter au début du fichier.

        Returns:
            int:    - 1 si le texte a été ajouté avec succès.
                    - 0 si l'ouverture du fichier a échoué.
                    - -1 si le fichier n'existe pas.

        Raises:
            TypeError: Si `filename` ou `txt` n'est pas une chaîne de caractères.

        """
    if not isinstance(filename,str):
        raise TypeError(
            "Le premier paramètre doit-être une chaine de caractères, contenant le nom du fichier"
            "complet."
        )

    if not isinstance(filename,str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant "
            "le texte à ajouter à la fin du fichier."
        )

    if not check_path(filename,"file"):
        print(f" le fichier {filename} n'existe pas.")
        return -1

    # faire une sauvegarde du fichier, cette fonction sera utile pour le projet
    # Car nous manipulons des fichiers de faibles tailles (moins de 100 ko)
    # prévoir dans le futur, un message si la taille du fichier est sup à 100ko

    content = read_text(filename)

    # le contenu du fichier a été supprimé, après avoir créé l'objet obj_cnx
    obj_cnx = open_connection(filename,WRITE_READ_MODE)

    if obj_cnx:
        # il faut injecter le texte dans le fichier
        # pour rappel le fichier est vide, donc le texte sera ajouté au début
        obj_cnx.write(txt)
        close_connection(obj_cnx)
        append_txt(filename,content)
        return 1
    else:
        print("Un problème lors de la réalisation de l'objet de connexion.")
        return 0

def add_txt(filename,txt,append=True):
    """
        Ajoute un texte au début ou à la fin d'un fichier.
        Cette fonction constitue une interface permettant de choisir l'emplacement
        où le texte doit être ajouté.

        Le paramètre `append` détermine le comportement :
            - True : ajout du texte à la fin du fichier.
            - False : ajout du texte au début du fichier.

        Args:
            filename (str): Chemin complet du fichier à modifier.
            txt (str): Texte à ajouter au fichier.
            append (bool, optional):    Indique la position d'ajout du texte.
                                        La valeur `True` ajoute le texte à la fin du fichier.
                                        La valeur `False` ajoute le texte au début du fichier.
                                        Par défaut : True.

        Returns:
            int:    - 1 si le texte a été ajouté avec succès.
                    - 0 si l'ouverture ou la modification du fichier a échoué.
                    - -1 si le fichier n'existe pas.

        Raises:
            TypeError:  Si `filename` ou `txt` n'est pas une chaîne de caractères,
                        ou si `append` n'est pas un booléen.

    """

    if not isinstance(append,bool):
        raise TypeError(
            "Le troisième paramètre doit être un type boolean."
        )

    if append:
        return append_txt(filename,txt)
    return prepend(filename,txt)


def insert_text(filename, text, cursor):
    """Insère une chaîne de caractères dans un fichier à une position donnée.

    Args:
        filename (str): Chemin complet du fichier à modifier.
        text (str): Texte à insérer dans le fichier.
        cursor (int): Position du curseur (index de caractère) où insérer le texte.

    Returns:
        dict or None:   - Un dictionnaire d'erreur avec code négatif si la longueur du texte
                          est invalide (-1) ou si le fichier est trop court (-2).
                        - None si l'opération s'est déroulée sans erreur.

    Raises:
        TypeError:  Si `text` n'est pas une chaîne de caractères,
                    ou si `cursor` n'est pas un entier.
    """
    if not isinstance(text, str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant le texte à insérer."
        )

    if not isinstance(cursor, int):
        raise TypeError(
            "Le dernier paramètre doit-être un entier."
        )

    if len(text) < 1:
        return {-1: "La longueur de la séquence n'est pas valide car < 1."}

    obj_cnx = open_connection(filename, READ_ONLY_MODE)

    # taille du fichier
    size_file = size(obj_cnx)

    if size_file < len(text):
        return {-2: f"le fichier ne contient pas la séquence :{text}."}

    left = read_char_range(filename, 0, cursor) + text
    right = read_char_range(filename, cursor + 1, size_file)

    obj_cnx = open_connection(filename, WRITE_ONLY_MODE)
    obj_cnx.write(left + right)

    close_connection(obj_cnx)


def get_cursor_position(filename, sequence):
    """Recherche la première occurrence d'une séquence dans le texte d'un fichier.

    Args:
        filename (str): Chemin complet du fichier à analyser.
        sequence (str): Séquence de texte à rechercher.

    Returns:
        tuple or dict:  - Un tuple (int, int) contenant la position de début et de fin si la séquence est trouvée.
                        - Un dictionnaire avec le code d'erreur -1 si la séquence fait < 1 caractère,
                          -2 si la séquence est plus longue que le texte du fichier,
                          ou -3 si la séquence n'a pas été trouvée.

    Raises:
        TypeError: Si `sequence` n'est pas une chaîne de caractères.
    """
    if not isinstance(sequence, str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant la séquence à rechercher."
        )

    size_sequence = len(sequence)

    if size_sequence < 1:
        return {-1: "La longueur de la séquence n'est pas valide car < 1."}

    text = read_text(filename)

    size_text = len(text)

    if size_text < size_sequence:
        return {-2: f"Cette séquence n'existe pas dans le texte du fichier."}

    for pointer in range(size_text):
        if text[pointer:pointer + size_sequence] == sequence:
            return pointer, pointer + size_sequence

    return {-3: f"Cette séquence n'a pas été trouvée dans le texte du fichier."}


def get_cursor_start_position(filename, sequence):
    """Retourne la position de début de la première occurrence d'une séquence.

    Args:
        filename (str): Chemin complet du fichier à analyser.
        sequence (str): Séquence de texte dont on cherche l'index de début.

    Returns:
        int or dict:    - La position de début (int) sous forme d'index si la séquence est trouvée.
                        - Un dictionnaire avec la clé -1 si la séquence n'est pas trouvée.
    """
    position = get_cursor_position(filename, sequence)

    # si le dictionnaire existe alors, il y a une erreur.
    if isinstance(position, dict):
        # prévoir en retour le code d'erreur
        return {-1: "La séquence non trouvée."}
    return position[0]


def get_cursor_end_position(filename, sequence):
    """Retourne la position de fin de la première occurrence d'une séquence.

    Args:
        filename (str): Chemin complet du fichier à analyser.
        sequence (str): Séquence de texte dont on cherche l'index de fin.

    Returns:
        int or dict:    - La position de fin (int) sous forme d'index si la séquence est trouvée.
                        - Un dictionnaire avec la clé -1 si la séquence n'est pas trouvée.
    """
    position = get_cursor_position(filename, sequence)

    # si le dictionnaire existe alors, il y a une erreur.
    if isinstance(position, dict):
        # prévoir en retour le code d'erreur
        return {-1: "La séquence non trouvée."}
    return position[1]


def insert_text_after_first_occurrence(filename, text, sequence):
    """Insère un texte juste après la première occurrence d'une séquence repère dans un fichier.

    Args:
        filename (str): Chemin complet du fichier à modifier.
        text (str): Texte à insérer dans le fichier.
        sequence (str): Séquence repère après laquelle placer le texte.

    Returns:
        dict:   - {1: "Insertion réalisée avec succès."} si l'insertion réussit.
                - {-1: "..."} si la séquence n'a pas été trouvée.
    """
    position = get_cursor_position(filename, sequence)

    if isinstance(position, dict):
        # prévoir en retour le code d'erreur
        return {-1: "La séquence non trouvée, aucune modification a été effectuée dans le fichier."}

    cursor = position[1]

    insert_text(filename, text, cursor)

    return {1: "Insertion réalisée avec succès."}


def insert_text_before_first_occurrence(filename, text, sequence):
    """Insère un texte juste avant la première occurrence d'une séquence repère dans un fichier.

    Args:
        filename (str): Chemin complet du fichier à modifier.
        text (str): Texte à insérer dans le fichier.
        sequence (str): Séquence repère avant laquelle placer le texte.

    Returns:
        dict:   - {1: "Insertion réalisée avec succès."} si l'insertion réussit.
                - {-1: "..."} si la séquence n'est pas trouvée.
                - {-2: "..."} si le fichier est plus court que le texte à insérer.
    """
    position = get_cursor_position(filename, sequence)

    if isinstance(position, dict):
        # prévoir en retour le code d'erreur
        return {-1: "La séquence non trouvée, aucune modification a été effectuée dans le fichier."}

    cursor = position[0]

    obj_cnx = open_connection(filename, READ_ONLY_MODE)

    # taille du fichier
    size_file = size(obj_cnx)

    if size_file < len(text):
        return {-2: f"le fichier ne contient pas la séquence :{text}."}

    left = read_char_range(filename, 0, cursor)

    right = text + read_char_range(filename, cursor + 1, size_file)

    obj_cnx = open_connection(filename, WRITE_ONLY_MODE)

    obj_cnx.write(left + right)

    close_connection(obj_cnx)

    return {1: "Insertion réalisée avec succès."}