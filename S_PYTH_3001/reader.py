from S_PYTH_3001.file_connection import (
    TEXT_IO_WRAPPER,
    BINARY_READ_MODE,
    BUFFERED_READER
)
from file_connection import (
    open_connection,
    close_connection,
    READ_ONLY_MODE
)

"""
Lecture de données depuis des fichiers texte et binaires.

Ce module fournit des fonctions permettant de lire le contenu de fichiers
texte et binaires à partir de connexions ouvertes.

Il s'appuie sur le module `file_connection` pour gérer l'ouverture et la
fermeture des connexions aux fichiers.

La lecture est organisée en deux niveaux :

- les fonctions `read_text()` et `read_binary()` constituent l'interface
  principale du module. Elles ouvrent le fichier, déclenchent sa lecture
  puis retournent les données lues ;
- les fonctions `read_text_aux()` et `read_binary_aux()` réalisent
  effectivement la lecture à partir d'une connexion déjà ouverte et
  assurent la fermeture de celle-ci après utilisation.

Les fonctions de lecture auxiliaires vérifient également que l'objet de
connexion fourni correspond au type attendu :

- `TEXT_IO_WRAPPER` pour les fichiers texte ;
- `BUFFERED_READER` pour les fichiers binaires.

Les résultats des fonctions auxiliaires sont retournés sous la forme
d'un dictionnaire contenant trois informations :

- `DATA` : les données lues ;
- `STATUS` : l'état de la connexion après la lecture ;
- `ERROR` : le message d'erreur éventuel.

Les fonctions publiques `read_text()` et `read_binary()` simplifient
l'utilisation de ces mécanismes en retournant directement les données
lues ou `None` en cas d'erreur.

La fermeture des connexions est prise en charge après la lecture afin
de libérer les ressources utilisées.
"""

# constantes
CLOSED = "closed"
DATA = "data"
STATUS = "status"
ERROR = "Error"

def read_text_aux(obj_connection):
    """
    Lit l'intégralité du contenu d'une connexion vers un fichier texte.

    Cette fonction travaille sur une connexion déjà ouverte. Elle vérifie
    que l'objet fourni est bien une connexion texte, lit son contenu.

    La fermeture des connexions est prise en charge après la lecture afin
    de libérer les ressources utilisées.

    Le résultat est retourné sous la forme d'un dictionnaire contenant
    les données lues, l'état de la connexion et une éventuelle erreur.

    :param obj_connection:  Objet représentant une connexion ouverte vers
                            un fichier texte.
    :type obj_connection: TEXT_IO_WRAPPER
    :return:    Dictionnaire contenant les données lues (`DATA`), l'état
                de la connexion (`STATUS`) et le message d'erreur éventuel
                (`ERROR`).
    :rtype:     dict
    :raises TypeError:  Si `obj_connection` n'est pas une connexion
                        de type `TEXT_IO_WRAPPER`.
    """
    if not isinstance(obj_connection, TEXT_IO_WRAPPER):
        raise TypeError(f"Le paramètre doit être un objet de type {TEXT_IO_WRAPPER}.")
    try:
        data_txt = obj_connection.read()
        # On libère la ressource
        close_connection(obj_connection)
        return {
            DATA: data_txt,
            STATUS: CLOSED,
            ERROR: "Pas d'erreur"
        }
    except ValueError as error:
        if obj_connection.closed:
            return {
                DATA: None,
                STATUS: CLOSED,
                ERROR: "Impossible de lire, la connexion est fermée."
            }
        return {
            DATA:None,
            STATUS:CLOSED,
            ERROR:error
        }

def read_text(filename):
    """
    Lit l'intégralité du contenu d'un fichier texte.

    Cette fonction ouvre le fichier en mode lecture, délègue la lecture
    du contenu à `read_text_aux()` puis retourne directement les données
    lues.

    Si le fichier ne peut pas être ouvert ou si une erreur survient
    pendant la lecture, la fonction affiche le message correspondant
    et retourne `None`.

    :param filename: Chemin du fichier texte à lire.
    :type filename: str
    :return: Contenu du fichier sous forme de chaîne de caractères,
        ou `None` en cas d'erreur.
    :rtype: str | None
    """
    obj_cnx = open_connection(filename, READ_ONLY_MODE)

    if obj_cnx is None:
        print(f"Le fichier :{filename} \nn'a pas été trouvé")
        return None

    data = read_text_aux(obj_cnx)

    if data[DATA] is not None:
        return data[DATA]

    print(data[ERROR])
    return None





def read_binary_aux(obj_connection):
    """
    Lit l'intégralité du contenu d'une connexion vers un fichier binaire.

    Cette fonction travaille sur une connexion déjà ouverte. Elle vérifie
    que l'objet fourni est bien une connexion binaire, lit son contenu.

    La fermeture des connexions est prise en charge après la lecture afin
    de libérer les ressources utilisées.

    Le résultat est retourné sous la forme d'un dictionnaire contenant
    les données lues, l'état de la connexion et une éventuelle erreur.

    :param obj_connection:  Objet représentant une connexion ouverte vers
                            un fichier binaire.
    :type obj_connection:   BUFFERED_READER
    :return:    Dictionnaire contenant les données lues (`DATA`), l'état
                de la connexion (`STATUS`) et le message d'erreur éventuel
                (`ERROR`).
    :rtype:     dict
    :raises TypeError:  Si `obj_connection` n'est pas une connexion
                        de type `BUFFERED_READER`.
    """

    if not isinstance(obj_connection, BUFFERED_READER):
        raise TypeError(f"Le paramètre doit être un objet de type {BUFFERED_READER}.")
    try:
        data_binary = obj_connection.read()
        # On libère la ressource
        close_connection(obj_connection)

        return {
            DATA:data_binary,
            STATUS:CLOSED,
            ERROR:"Pas d'erreur"
        }
    except ValueError as error:
        if obj_connection.closed:
            return {
                DATA: None,
                STATUS: CLOSED,
                ERROR: "Impossible de lire, la connexion est fermée."
            }
        return {
            DATA:None,
            STATUS:CLOSED,
            ERROR:error
        }




def read_binary(filename):
    """
    Lit l'intégralité du contenu d'un fichier binaire.

    Cette fonction ouvre le fichier en mode lecture binaire, délègue
    la lecture du contenu à `read_binary_aux()` puis retourne directement
    les données lues.

    Si le fichier ne peut pas être ouvert ou si une erreur survient
    pendant la lecture, la fonction affiche le message correspondant
    et retourne `None`.

    :param filename: Chemin du fichier binaire à lire.
    :type filename: str
    :return: Contenu du fichier sous forme d'une séquence d'octets,
        ou `None` en cas d'erreur.
    :rtype: bytes | None
    """

    obj_cnx = open_connection(filename, BINARY_READ_MODE)

    if obj_cnx is None:
        print(f"Le fichier :{filename} \nn'a pas été trouvé")
        return None

    data = read_binary_aux(obj_cnx)

    if data[DATA] is not None:
        return data[DATA]

    print(data[ERROR])
    return None
