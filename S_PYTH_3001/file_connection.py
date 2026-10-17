
"""
Gestion des connexions aux fichiers.

Ce module centralise l'ouverture et la fermeture des fichiers
texte et binaires.

Référence du catalogue : 100

Les erreurs prévues sont retournées sous la forme d'un dictionnaire
dont la clé est un code numérique et la valeur un message explicatif.

Codes :
    101 : autorisation d'accès refusée
    102 : mode d'ouverture invalide
    103 : type de nom de fichier invalide
    104 : nom de fichier vide
    105 : connexion invalide

Dépendances :
    S_PYTH_3001.file_manager.check_path
    S_PYTH_3001.params_connection
    S_PYTH_3001.catalogue_messages.create_message
"""

import _io

from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.params_connection import *
from S_PYTH_3001.catalogue_messages import create_message


def is_valid_mode(mode):
    """
    Vérifie si le mode d'ouverture est autorisé.

    Args:
        mode (str): Mode d'ouverture du fichier.

    Returns:
        bool: True si le mode est autorisé, sinon False.
    """
    return mode in VALID_MODES


def is_binary_mode(mode):
    """
    Vérifie si le mode d'ouverture correspond à un mode binaire.

    Args:
        mode (str): Mode d'ouverture du fichier.

    Returns:
        bool: True si le mode est binaire, sinon False.
    """
    return mode in (
        BINARY_WRITE_READ_MODE,
        BINARY_WRITE_MODE,
        BINARY_READ_MODE,
        BINARY_READ_WRITE_MODE
    )


def is_obj_connection(obj_cnx):
    """
    Vérifie si un objet correspond à une connexion fichier reconnue.

    Args:
        obj_cnx: Objet à vérifier.

    Returns:
        bool: True si l'objet est d'un type reconnu, sinon False.
    """
    for obj in (
        BUFFERED_WRITER,
        BUFFERED_READER,
        BUFFERED_RANDOM,
        TEXT_IO_WRAPPER
    ):
        if isinstance(obj_cnx, obj):
            return True

    return False


def open_connection(filename, mode=READ_ONLY_MODE):
    """
    Ouvre une connexion vers un fichier.

    Args:
        filename (str): Chemin du fichier à ouvrir.
        mode (str): Mode d'ouverture autorisé.
            Par défaut, READ_ONLY_MODE.

    Returns:
        _io.IOBase | None | dict:
            - Objet fichier si l'ouverture réussit.
            - None si check_path indique que le fichier n'existe pas.
            - Dictionnaire codifié en cas d'erreur prévue :
                101 : autorisation refusée.
                102 : mode invalide.
                103 : nom de fichier de type invalide.
                104 : nom de fichier vide.

    Note:
        Les erreurs système autres que PermissionError ne sont pas
        transformées par cette fonction et peuvent remonter à l'appelant.
    """
    if not is_valid_mode(mode):
        return create_message(102, mode=mode)

    if not isinstance(filename, str):
        return create_message(103)

    if len(filename) == 0:
        return create_message(104)

    try:
        if check_path(filename, "file"):
            if is_binary_mode(mode):
                return open(filename, mode)

            return open(filename, mode, encoding="utf-8")

        return None

    except PermissionError:
        return create_message(101, mode=mode)


def close_connection(obj_connection):
    """
    Ferme une connexion fichier ouverte.

    Args:
        obj_connection: Objet représentant la connexion à fermer.

    Returns:
        int | dict:
            - 1 si la connexion est fermée.
            - Dictionnaire de code 105 si l'objet n'est pas reconnu.

    Raises:
        Les erreurs système imprévues liées à la fermeture ne sont pas
        interceptées par cette fonction.
    """
    if not is_obj_connection(obj_connection):
        return create_message(105)

    obj_connection.close()

    return 1
