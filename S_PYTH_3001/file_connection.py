"""
Gestion des connexions aux fichiers.

Ce module centralise les opérations d'ouverture et de fermeture des
fichiers texte et binaires. Il fournit également des fonctions de
vérification des modes d'ouverture et de validation des objets de
connexion.

Les résultats des opérations sont construits à partir du catalogue
centralisé des messages, au moyen de la fonction create_message().
Ils sont retournés sous la forme de dictionnaires contenant notamment
un code numérique, le nom de la fonction concernée, un statut, un
message explicatif et une donnée associée au résultat.

Référence du catalogue :
    100 : module file_connection.py

Codes des messages :
    101 : autorisation d'accès au fichier refusée ;
    102 : mode d'ouverture invalide ;
    103 : type du nom de fichier invalide ;
    104 : nom de fichier vide ;
    105 : paramètre fichier invalide ;
    106 : objet de connexion invalide ;
    110 : ouverture d'une connexion fichier ;
    111 : ouverture d'une connexion fichier texte en UTF-8 ;
    112 : vérification d'un objet de connexion ;
    113 : vérification du mode d'ouverture ;
    114 : vérification du mode binaire.

Dépendances internes :
    S_PYTH_3001.file_manager.check_path :
        Vérifie le chemin et la nature du fichier.

    S_PYTH_3001.params_connection :
        Fournit les constantes définissant les modes d'ouverture
        et les types d'objets de connexion reconnus.

    S_PYTH_3001.catalogue_messages.create_message :
        Construit les dictionnaires de résultat à partir des codes
        et des informations du catalogue centralisé.

Comportement :
    - Les modes d'ouverture sont contrôlés avant toute tentative
      d'ouverture du fichier.
    - Les fichiers binaires sont ouverts sans paramètre d'encodage.
    - Les fichiers texte sont ouverts avec l'encodage UTF-8.
    - Les erreurs d'autorisation sont interceptées et converties
      en résultats codifiés.
    - Les autres erreurs système ne sont pas systématiquement
      interceptées et peuvent être propagées à l'appelant.

Note :
    Les fonctions de vérification retournent également des
    dictionnaires de résultat. La valeur booléenne associée à ces
    vérifications est accessible via la clé "data".

    La fermeture d'une connexion nécessite de fournir un objet
    de connexion reconnu par le module.
"""
import _io
from enum import Flag

from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.params_connection import *
from S_PYTH_3001.catalogue_messages import create_message


def is_valid_mode(mode):
    """
    Vérifie si le mode d'ouverture d'un fichier est autorisé.

    Compare le mode fourni à la liste des modes autorisés définis
    dans le module params_connection.

    Args:
        mode (str): Mode d'ouverture à vérifier.

    Returns:
        dict: Résultat construit à partir du code catalogue 113.
            La clé "data" contient True si le mode est autorisé,
            False dans le cas contraire.
            La clé "status" indique le résultat de la vérification.

    Note:
        Le dictionnaire retourné est construit par create_message().
    """

    _flag = mode in VALID_MODES
    _status = "ERREUR"
    if _flag:
        _status = "SUCCES"

    return create_message(113,data=_flag,status=_status)

def is_binary_mode(_mode):
    """
        Vérifie si le mode d'ouverture correspond à un mode binaire.

        Compare le mode fourni aux constantes définissant les modes
        d'ouverture binaires autorisés.

        Args:
            _mode (str): Mode d'ouverture du fichier à vérifier.

        Returns:
            dict: Dictionnaire de résultat construit à partir du code
                catalogue 114, contenant :
                    - code : code numérique du message ;
                    - fonction : nom de la fonction concernée ;
                    - status : "SUCCES" si le mode est binaire,
                      "ERREUR" dans le cas contraire ;
                    - mode : mode d'ouverture fourni ;
                    - message : message explicatif ;
                    - data : booléen indiquant si le mode est binaire.

        Note:
            Les modes binaires reconnus sont :
                BINARY_WRITE_READ_MODE ;
                BINARY_WRITE_MODE ;
                BINARY_READ_MODE ;
                BINARY_READ_WRITE_MODE.

            Le dictionnaire de résultat est généré par create_message().
    """

    _flag = False
    if _mode in (
        BINARY_WRITE_READ_MODE,
        BINARY_WRITE_MODE,
        BINARY_READ_MODE,
        BINARY_READ_WRITE_MODE
    ):
        _flag = True

    _status = "ERREUR"
    if _flag:
        _status = "SUCCES"

    return create_message(114,data=_flag,mode=_mode,status=_status)

def is_obj_connection(obj_cnx):
    """
        Vérifie si un objet appartient aux types de connexion reconnus.

        Contrôle si l'objet fourni est une instance de l'un des types
        de connexion définis dans le module params_connection :
        flux binaires en écriture, en lecture ou à accès aléatoire,
        ou flux texte.

        Args:
            obj_cnx: Objet dont le type doit être vérifié.

        Returns:
            dict: Résultat construit à partir du code catalogue 112.
                La clé "data" contient True si l'objet appartient à
                un type reconnu, False dans le cas contraire.
                La clé "status" indique le résultat de la vérification.

        Note:
            Cette fonction vérifie le type de l'objet, mais ne garantit
            pas que la connexion soit encore ouverte ou utilisable.
    """

    _flag = False
    _status ="ERREUR"
    for obj in (
        BUFFERED_WRITER,
        BUFFERED_READER,
        BUFFERED_RANDOM,
        TEXT_IO_WRAPPER
    ):

        if isinstance(obj_cnx, obj):
            _flag =  True

    if _flag:
        _status = "SUCCES"

    return create_message(112,data=_flag,status=_status)

def open_connection(filename, _mode=READ_ONLY_MODE):
    """
        Ouvre un fichier texte ou binaire selon le mode spécifié.

        Vérifie le mode d'ouverture, le type du nom de fichier et
        sa validité avant de procéder à l'ouverture. Le chemin est
        contrôlé à l'aide de la fonction check_path().

        Les fichiers binaires sont ouverts sans paramètre d'encodage.
        Les fichiers texte sont ouverts avec l'encodage UTF-8.

        Args:
            filename (str): Chemin du fichier à ouvrir.
            _mode (str, optional): Mode d'ouverture du fichier.
                Par défaut, READ_ONLY_MODE.

        Returns:
            dict: Résultat de l'opération, construit à partir du
                catalogue centralisé des messages.
                La clé "code" identifie le résultat.
                La clé "status" indique le statut de l'opération.
                La clé "message" contient le message explicatif.
                La clé "data" contient l'objet fichier ouvert
                en cas de succès.

        Raises:
            PermissionError: Cette exception est interceptée et
                convertie en résultat codifié.
            OSError: Les autres erreurs système liées à l'ouverture
                ne sont pas interceptées par cette fonction.

        Note:
            Les codes catalogue utilisés sont :
                101 : autorisation d'accès refusée ;
                102 : mode d'ouverture invalide ;
                103 : type du nom de fichier invalide ;
                104 : nom de fichier vide ;
                106 : fichier absent ou chemin non valide selon
                      le résultat de check_path() ;
                110 : ouverture en mode binaire ;
                111 : ouverture en mode texte UTF-8.
    """


    if not is_valid_mode(_mode).get("data"):
        return create_message(102, mode=_mode)

    if not isinstance(filename, str):
        return create_message(103)

    if len(filename) == 0:
        return create_message(104)

    try:
        if check_path(filename, "file").get("data"):
            if is_binary_mode(_mode).get("data"):
                # fichier en mode lecture binaire
                return create_message(110,mode=_mode,data=open(filename, mode=_mode))
            # fichier texte encodage utf-8
            return create_message(111,mode=_mode,data=open(filename, mode=_mode,encoding="utf-8"))
        # le fichier n'existe pas
        return create_message(106)

    except PermissionError:
        return create_message(101, mode=_mode)

def close_connection(obj_connection):
    """
        Ferme une connexion à un fichier.

        Vérifie le type de l'objet fourni, récupère les informations
        associées à la connexion, puis ferme le fichier à l'aide de
        la méthode close().

        Args:
            obj_connection (dict): Dictionnaire contenant les
                informations de la connexion, notamment le mode
                d'ouverture et l'objet fichier associé dans la clé
                "data".

        Returns:
            dict: Résultat construit à partir du catalogue centralisé
                des messages.
                La clé "code" identifie le résultat.
                La clé "status" indique le statut de l'opération.
                La clé "message" contient le message explicatif.
                La clé "data" contient la valeur associée au résultat.

        Raises:
            AttributeError: Peut survenir si l'objet fourni ne possède
                pas les méthodes ou attributs attendus.
            OSError: Peut survenir si une erreur système se produit
                lors de la fermeture du fichier.

        Note:
            L'objet fourni doit respecter la structure attendue par
            la fonction. Les erreurs liées à la fermeture ne sont
            pas interceptées par cette fonction.
    """

    if is_obj_connection(obj_connection).get("data"):
        return create_message(106)

    _mode = obj_connection.get("mode")
    obj_connection.get("data").close()

    return create_message(110,mode =_mode,data = True)
