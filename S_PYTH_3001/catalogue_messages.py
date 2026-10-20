
"""
Catalogue centralisé des messages du Gestionnaire de notes.

Chaque message est identifié par un code numérique stable.

Convention :
    100 : référence du module file_connection.py
    101 à 109 : erreurs du module file_connection.py
    110 à 119 : succès du module file_connection.py

Les autres modules disposeront de leurs propres plages de codes.
"""

CATALOGUE_MESSAGES = {
    # --------------------------------------------------
    # Module 100 : file_connection.py
    # --------------------------------------------------

    101: {
        "fonction": "open_connection",
        "message": (
            "Vous n'avez pas l'autorisation d'accéder "
            "au fichier dans le mode suivant : \'{mode}\'"
        ),
        "mode":None,
        "status": "ERREUR",
        "data":None

    },

    102: {
        "fonction": "open_connection",
        "message": (
            "Le mode d'ouverture du fichier n'est pas valide : \'{mode}\'{"
        ),
        "mode":None,
        "status": "ERREUR",
        "data":None
    },

    103: {
        "fonction": "open_connection",
        "message": (
            "Le nom du fichier doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    104: {
        "fonction": "open_connection",
        "message": (
            "Le nom du fichier doit être une chaîne non vide."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    105: {
        "fonction": "open_connection",
        "message": (
            "Le paramètre fourni n'est pas un fichier valide."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },
    106: {
            "fonction": "close_connection",
            "message": (
                "Le paramètre fourni n'est pas une connexion valide."
            ),
            "mode": None,
            "status": "ERREUR",
            "data":False
        },

    110: {
        "fonction": "close_connection",
        "message": "La connexion au fichier est ouverte dans le mode :\'{mode}\'.",
        "mode": None,
        "status": "SUCCES",
        "data": False
    },
    111: {
        "fonction": "close_connection",
        "message": "La connexion au fichier est ouverte dans le mode:\' {mode} \'pour l'encodage utf-8.",
        "mode": None,
        "status": "SUCCES",
        "data": False
        },
    112: {
        "fonction": "is_obj_connection",
        "message": "Vérifie si l'objet de connexion est valide.",
        "mode": None,
        "status": "SUCCES",
        "data": True
        },
    113: {
        "fonction": "is_valid_mode",
        "message": "Vérifie si le mode d'ouverture est autorisé.",
        "mode": None,
        "status": "SUCCES",
        "data": True
        },
    114:{
        "fonction": "is_binary_mode",
        "message": "Vérifie si on a choisi un mode binaire",
        "mode":None,
        "status": "SUCCES",
        "data": True
    },

    # --------------------------------------------------
    # Module 200 : file_manager.py
    # --------------------------------------------------

    201: {
        "fonction": "check_path",
        "message": "Le chemin doit être une chaîne de caractères.",
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    202: {
        "fonction": "check_path",
        "message": (
            "Le status de chemin doit être 'file' ou 'dir'."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    203: {
        "fonction": "create_directory",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    204: {
        "fonction": "create_directory",
        "message": (
            "Le nom du répertoire doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    205: {
        "fonction": "list_directory",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    206: {
        "fonction": "create_subject_directories",
        "message": (
            "Le chemin doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    207: {
        "fonction": "create_file",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    208: {
        "fonction": "create_file",
        "message": (
            "Le nom du fichier doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    209: {
        "fonction": "create_file",
        "message": (
            "Le répertoire racine n'existe pas ou n'est pas valide : {root}"
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    210: {
        "fonction": "delete_file",
        "message": (
            "Le chemin du fichier doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    },

    211: {
        "fonction": "create_trainee_space",
        "message": (
            "Le nom du stagiaire doit être une chaîne de caractères."
        ),
        "mode": None,
        "status": "ERREUR",
        "data":None
    }

}


def create_message(code,**params):
    """
        Construit un résultat standardisé à partir du catalogue des messages.

        Recherche le message correspondant au code fourni, récupère les
        informations associées et construit un dictionnaire contenant
        le code, la fonction concernée, le statut, le mode, le message
        formaté et les données de retour.

        Args:
            code (int): Code numérique identifiant le message dans le
                catalogue CATALOGUE_MESSAGES.
            **params: Paramètres nommés complémentaires. Les paramètres
                pris en charge sont :
                    data : donnée ou valeur de retour associée au résultat ;
                    mode : mode de traitement utilisé pour formater
                        le message.

        Returns:
            dict | None: Dictionnaire contenant les informations du résultat
                si le code existe dans le catalogue, None sinon.

        Note:
            Les paramètres non utilisés par la fonction sont ignorés.
            Le message est actuellement formaté avec le paramètre mode.
    """
    information = CATALOGUE_MESSAGES.get(code)

    if information is None:
        return None

    _data = None
    _mode = ""

    key = "data"
    if key in params:
        _data = params.get("data")

    key ="mode"
    if key in params:
        _mode = params.get("mode")

    message = information["message"].format(mode=_mode)

    return {
            "code":code,
            "fonction": information["fonction"],
            "status": information["status"],
            "mode":_mode,
            "message": message,
            "data": _data
    }
