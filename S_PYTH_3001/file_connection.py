import _io

from file_manager import check_path

"""
Gestion des connexions aux fichiers.

Ce module fournit des fonctions permettant d'ouvrir et de fermer des
connexions vers des fichiers.

Il centralise également les différents modes d'ouverture proposés par
Python avec la fonction `open()` afin de leur attribuer des noms explicites
et faciliter leur utilisation dans l'application.

Les fichiers texte sont ouverts avec l'encodage UTF-8. Les fichiers
binaires sont ouverts sans encodage afin de permettre la lecture et
l'écriture de données sous forme d'octets.

Modes d'ouverture disponibles :

    READ_ONLY_MODE            ("r")
        Lecture seule. Le fichier doit exister.

    WRITE_ONLY_MODE           ("w")
        Écriture seule. Le fichier est créé s'il n'existe pas.
        Le contenu existant est supprimé.

    APPEND_MODE               ("a")
        Écriture en ajout à la fin du fichier.
        Le fichier est créé s'il n'existe pas.

    APPEND_READ_MODE          ("a+")
        Lecture et ajout à la fin du fichier.
        Le fichier est créé s'il n'existe pas.

    BINARY_READ_MODE          ("rb")
        Lecture en mode binaire.

    BINARY_WRITE_MODE         ("wb")
        Écriture en mode binaire.
        Le contenu existant est supprimé.

    READ_WRITE_MODE           ("r+")
        Lecture et écriture.
        Le fichier doit exister.

    WRITE_READ_MODE           ("w+")
        Écriture et lecture.
        Le fichier est créé s'il n'existe pas et son contenu existant
        est supprimé.

    BINARY_READ_WRITE_MODE   ("rb+")
        Lecture et écriture en mode binaire.
        Le fichier doit exister.

    BINARY_WRITE_READ_MODE   ("wb+")
        Écriture et lecture en mode binaire.
        Le fichier est créé s'il n'existe pas et son contenu existant
        est supprimé.

La constante `VALID_MODES` regroupe l'ensemble des modes d'ouverture
autorisés par ce module.

Les fonctions principales sont :

    is_binary_mode(mode)
        Indique si un mode correspond à une ouverture en mode binaire.

    is_obj_connection(obj_cnx)
        Vérifie si un objet correspond à une connexion valide vers
        un fichier.

    is_valid_mode(mode)
        Vérifie si un mode d'ouverture est autorisé.

    open_connection(filename, mode)
        Vérifie le mode et l'existence du fichier, puis ouvre une
        connexion en mode texte ou binaire selon le mode demandé.

    close_connection(obj_connection)
        Vérifie la connexion puis ferme le fichier.

Dépendance :

    S_PYTH_3001.file_manager.check_path
        Fonction utilisée pour vérifier l'existence du fichier avant
        son ouverture.

Exemple :

    connection = open_connection("notes.txt", READ_ONLY_MODE)

    if connection:
        content = connection.read()
        close_connection(connection)
"""



#===============================================
# constantes
#===============================================
READ_ONLY_MODE = "r"
WRITE_ONLY_MODE = "w"

APPEND_MODE = "a"
APPEND_READ_MODE = "a+"

BINARY_READ_MODE = "rb"
BINARY_WRITE_MODE = "wb"

READ_WRITE_MODE = "r+"
WRITE_READ_MODE = "w+"

BINARY_READ_WRITE_MODE = "rb+"
BINARY_WRITE_READ_MODE = "wb+"

VALID_MODES = (
    READ_ONLY_MODE,
    WRITE_ONLY_MODE,
    APPEND_MODE,
    APPEND_READ_MODE,
    BINARY_READ_MODE,
    BINARY_WRITE_MODE,
    READ_WRITE_MODE,
    WRITE_READ_MODE,
    BINARY_READ_WRITE_MODE,
    BINARY_WRITE_READ_MODE
)

BUFFERED_READER = _io.BufferedReader
BUFFERED_WRITER = _io.BufferedWriter
BUFFERED_RANDOM = _io.BufferedRandom
TEXT_IO_WRAPPER = _io.TextIOWrapper


def is_valid_mode(mode):
    """
       Vérifie si le mode d'ouverture fourni est autorisé.

       Le mode est comparé à la liste des modes d'ouverture définis
       dans la constante `VALID_MODES`.

       Args:
           mode (str): Mode d'ouverture du fichier.

       Returns:
           bool: True si le mode est autorisé, sinon False.
    """
    return mode in VALID_MODES

def is_binary_mode(mode):
    """
        Vérifie si le mode d'ouverture correspond à un mode binaire.

        Cette fonction permet de distinguer les modes d'ouverture binaires
        des modes d'ouverture texte.

        Elle est notamment utilisée par `open_connection()` pour déterminer
        si le paramètre `encoding="utf-8"` doit être utilisé lors de
        l'ouverture du fichier.

        Args:
            mode (str): Mode d'ouverture du fichier.

        Returns:
            bool: True si le mode est binaire, sinon False.
    """
    return mode in (BINARY_WRITE_READ_MODE,
                    BINARY_WRITE_MODE,
                    BINARY_READ_MODE,
                    BINARY_READ_WRITE_MODE)

def is_obj_connection(obj_cnx):
    """
       Vérifie si un objet correspond à une connexion valide vers un fichier.

       La fonction vérifie si l'objet fourni est une instance d'un des
       types de connexion pris en charge par le module.

       Les types de connexion reconnus sont :

           - `_io.BufferedWriter`
           - `_io.BufferedReader`
           - `_io.BufferedRandom`
           - `_io.TextIOWrapper`

       Args:
           obj_cnx (_io.IOBase): Objet à vérifier.

       Returns:
           bool: True si l'objet correspond à une connexion valide,
               sinon False.
       """
    for obj in (BUFFERED_WRITER,BUFFERED_READER,BUFFERED_RANDOM,TEXT_IO_WRAPPER):
        if isinstance(obj_cnx,obj):
            return True
    return False

def open_connection(filename, mode=READ_ONLY_MODE):
    """
    Ouvre une connexion vers un fichier.

    Args:
        filename (str): Chemin du fichier à ouvrir.
        mode (str): Mode d'ouverture du fichier.
            Par défaut, READ_ONLY_MODE ("r").

    Returns:
        _io.IOBase | None: Objet représentant la connexion ouverte,
            ou None si le fichier n'existe pas.

    Raises:
        ValueError: Si le mode d'ouverture n'est pas autorisé.
    """
    # il faut valider le paramètre mode

    if not is_valid_mode(mode):
        raise ValueError(f"Le mode d'ouverture du fichier est pas valide: {mode}")

    if not isinstance(filename,str):
        raise ValueError("Le nom du fichier doit-être une chaine de caractères.")

    if len(filename)<=0:
        raise ValueError("Le nom du fichier doit-être une chaine de caractères non vide.")
    try:
        if check_path(filename,"file"):
            # deux types : texte ou binaire
            if not is_binary_mode(mode):
                return open(filename,mode,encoding="utf-8")
            else:
                return open(filename,mode)
        return None
    except PermissionError:
        # si le fichier est en MODE LECTURE UNIQUE, peut provoquer cette exception
        # dans le cas ou le mode est _WRITE_

        # Ou vous n'avez pas les droits à modifier le contenu
        raise ValueError(f"Vous n'avez pas l'autorisation d'accéder "
                         f"au fichier dans le mode suivant:{mode}")



def close_connection(obj_connection):
   """
    Ferme une connexion ouverte vers un fichier.

    Args:
        obj_connection : Objet représentant la connexion
                         à fermer.

    Returns:
        int: Retourne 1 lorsque la connexion est fermée.

    Raises:
        TypeError: Si l'objet fourni n'est pas une connexion valide.
    """
   if not is_obj_connection(obj_connection):
       raise TypeError("Erreur : Le paramètre n'est pas un objet de type valide.")

   obj_connection.close()

   return 1



