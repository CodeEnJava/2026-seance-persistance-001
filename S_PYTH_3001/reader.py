

"""
Ce module a pour objectif de lire :
    * des fichiers texte
    * des fichiers binaire

    On va utiliser une connexion vers le fichier en mettant en oeuvre
    les modules file_connection et file_manager

    Pour réaliser la lecture, je propose de le faire en deux temps
    * read_text_aux(obj_cnx) --> va retourner un dictionnaire {data:str, status: closed, error : message}
    * read_text(filename). --> va retourner un str

    * read_binary_aux(obj_cnx) --> va retourner un dictionnaire {data:str, status: closed, error : message}
    * read_binary(filename) va retourner un str


    La fermeture des connexions est prise en charge après la lecture afin de libérer la ressource

"""
from S_PYTH_3001.file_connection import close_connection, open_connection, READ_ONLY_MODE, BUFFERED_READER, \
    BINARY_READ_MODE
from file_connection import TEXT_IO_WRAPPER

# définition des constantes pour le dictionnaire
CLOSED = "closed"
DATA = "data"
STATUS = "status"
ERROR = "error"

def read_text_aux(obj_connection):
    """
    Lit l'intégralité du contenu d'une connexion vers un fichier texte.

    La docString, sera réalisée hors vidéo et sera disponible sur le GitHUB

    """

    if not isinstance(obj_connection,TEXT_IO_WRAPPER):
        raise TypeError(f"Le paramètre doit être un objet de type {TEXT_IO_WRAPPER}.")

    try:
        data_txt = obj_connection.read()

        #On libère la ressource
        close_connection(obj_connection)
        return {
            DATA:data_txt,
            STATUS:CLOSED,
            ERROR:"Pas d'erreur"
        }
    except ValueError as error:
        if obj_connection.closed:
            return {
                DATA:None,
                STATUS:CLOSED,
                ERROR:"Impossible de lire le fichier, la connexion était fermée."
            }
        return {
            DATA:None,
            STATUS:CLOSED,
            ERROR:error
        }

def read_text(filename):
    """
        List l'intégralité du contenu d'un fichier texte.
        La docString, sera réalisée hors vidéo et sera disponible sur le GitHUB

    """
    # par défaut :READ_ONLY_MODE
    obj_cnx = open_connection(filename)

    if obj_cnx is None:
        print(f"Le fichier {filename}\nn'a pas été trouvé.")
        return None

    data = read_text_aux(obj_cnx)

    if data[DATA] is not None:
        return data[DATA]

    print(data[ERROR])
    return None

def read_binary_aux(obj_connection):
    """
    Lit l'intégralité du contenu d'une connexion vers un fichier binaire (image, vidéo, audio).

    La docString, sera réalisée hors vidéo et sera disponible sur le GitHUB

    """

    if not isinstance(obj_connection,BUFFERED_READER):
        raise TypeError(f"Le paramètre doit être un objet de type {BUFFERED_READER}.")

    try:
        data_binary = obj_connection.read()

        #On libère la ressource
        close_connection(obj_connection)
        return {
            DATA:data_binary,
            STATUS:CLOSED,
            ERROR:"Pas d'erreur"
        }
    except ValueError as error:
        if obj_connection.closed:
            return {
                DATA:None,
                STATUS:CLOSED,
                ERROR:"Impossible de lire le fichier, la connexion était fermée."
            }
        return {
            DATA:None,
            STATUS:CLOSED,
            ERROR:error
        }

def read_binary(filename):
    """
        List l'intégralité du contenu d'un fichier binaire.
        La docString, sera réalisée hors vidéo et sera disponible sur le GitHUB

    """

    obj_cnx = open_connection(filename,BINARY_READ_MODE)

    if obj_cnx is None:
        print(f"Le fichier {filename}\nn'a pas été trouvé.")
        return None

    data = read_binary_aux(obj_cnx)

    if data[DATA] is not None:
        return data[DATA]

    print(data[ERROR])
    return None