"""
Catalogue centralisé des messages du Gestionnaire de notes.

Convention :
    100 : référence du module file_connection.py
    101 à 109 : erreurs de file_connection.py
    110 à 119 : succès de file_connection.py
    200 : référence du module file_manager.py
    201 à 219 : erreurs de file_manager.py
    220 et suivants : résultats de file_manager.py
"""

CATALOGUE_MESSAGES = {
    # --------------------------------------------------
    # Module 100 : file_connection.py
    # --------------------------------------------------
    101: {
        "fonction": "open_connection",
        "message": "Vous n'avez pas l'autorisation d'accéder au fichier dans le mode suivant : '{mode}'.",
        "mode": None, "status": "ERREUR", "data": None
    },
    102: {
        "fonction": "open_connection",
        "message": "Le mode d'ouverture du fichier n'est pas valide : '{mode}'.",
        "mode": None, "status": "ERREUR", "data": None
    },
    103: {
        "fonction": "open_connection",
        "message": "Le nom du fichier doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    104: {
        "fonction": "open_connection",
        "message": "Le nom du fichier doit être une chaîne non vide.",
        "mode": None, "status": "ERREUR", "data": None
    },
    105: {
        "fonction": "open_connection",
        "message": "Le paramètre fourni n'est pas un fichier valide.",
        "mode": None, "status": "ERREUR", "data": None
    },
    106: {
        "fonction": "close_connection",
        "message": "Le paramètre fourni n'est pas une connexion valide.",
        "mode": None, "status": "ERREUR", "data": False
    },
    110: {
        "fonction": "open_connection",
        "message": "La connexion au fichier est ouverte : (mode : '{mode}').",
        "mode": None, "status": "SUCCES", "data": False
    },
    111: {
        "fonction": "open_connection",
        "message": "La connexion au fichier est ouverte : (mode : '{mode}', encodage UTF-8).",
        "mode": None, "status": "SUCCES", "data": False
    },
    112: {
        "fonction": "is_obj_connection",
        "message": "Vérifie si l'objet de connexion est valide.",
        "mode": None, "status": "SUCCES", "data": True
    },
    113: {
        "fonction": "is_valid_mode",
        "message": "Vérifie si le mode d'ouverture est autorisé.",
        "mode": None, "status": "SUCCES", "data": True
    },
    114: {
        "fonction": "is_binary_mode",
        "message": "Vérifie si le mode choisi est un mode binaire.",
        "mode": None, "status": "SUCCES", "data": True
    },

    # --------------------------------------------------
    # Module 200 : file_manager.py
    # --------------------------------------------------
    201: {
        "fonction": "check_path",
        "message": "Le chemin doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    202: {
        "fonction": "check_path",
        "message": "Le type de chemin doit être 'file' ou 'dir'.",
        "mode": None, "status": "ERREUR", "data": None
    },
    203: {
        "fonction": "create_directory",
        "message": "Le chemin racine doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    204: {
        "fonction": "create_directory",
        "message": "Le nom du répertoire doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    205: {
        "fonction": "list_directory",
        "message": "Le chemin racine doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    206: {
        "fonction": "create_subject_directories",
        "message": "Le chemin doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    207: {
        "fonction": "create_file",
        "message": "Le chemin racine doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    208: {
        "fonction": "create_file",
        "message": "Le nom du fichier doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    209: {
        "fonction": "create_file",
        "message": "Le répertoire racine n'existe pas ou n'est pas valide : {root}",
        "mode": None, "status": "ERREUR", "data": None
    },
    210: {
        "fonction": "delete_file",
        "message": "Le chemin du fichier doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },
    211: {
        "fonction": "create_trainee_space",
        "message": "Le nom du stagiaire doit être une chaîne de caractères.",
        "mode": None, "status": "ERREUR", "data": None
    },

    # Résultats de vérification des chemins
    220: {
        "fonction": "check_path",
        "message": "Vérification du répertoire : {path}",
        "mode": None, "status": "SUCCES", "data": False
    },
    221: {
        "fonction": "check_path",
        "message": "Vérification du fichier : {path}",
        "mode": None, "status": "SUCCES", "data": False
    },

    # Résultats de création de répertoire
    222: {
        "fonction": "create_directory",
        "message": "Le répertoire existe déjà : {path}",
        "mode": None, "status": "SUCCES", "data": 0
    },
    223: {
        "fonction": "create_directory",
        "message": "Le répertoire racine n'existe pas ou n'est pas un dossier : {root}",
        "mode": None, "status": "ECHEC", "data": -1
    },
    228: {
        "fonction": "create_directory",
        "message": "Le répertoire a été créé : {path}",
        "mode": None, "status": "SUCCES", "data": 1
    },

    # Autres résultats
    224: {
        "fonction": "list_directory",
        "message": "Liste des fichiers et répertoires de : {root}",
        "mode": None, "status": "SUCCES", "data": None
    },
    225: {
        "fonction": "add_trainee",
        "message": "L'arborescence du stagiaire '{trainee}' a été créée.",
        "mode": None, "status": "SUCCES", "data": 1
    },
    226: {
        "fonction": "add_trainee",
        "message": "L'arborescence du stagiaire '{trainee}' existe déjà.",
        "mode": None, "status": "SUCCES", "data": 0
    },
    227: {
        "fonction": "add_trainee",
        "message": "La création de l'arborescence du stagiaire '{trainee}' est partielle.",
        "mode": None, "status": "ECHEC", "data": -1
    },
    230: {
        "fonction": "create_file",
        "message": "Le fichier a été créé : {path}",
        "mode": None,
        "status": "SUCCES",
        "data": True
    },

    231: {
        "fonction": "create_file",
        "message": "Le fichier existe déjà : {path}",
        "mode": None,
        "status": "SUCCES",
        "data": None
    },

    232: {
        "fonction": "create_file",
        "message": "Erreur lors de la création du fichier : {path}. Détail : {error}",
        "mode": None,
        "status": "ECHEC",
        "data": False
    },
    # 233 : le fichier à supprimer est absent.
    233: {
        "fonction": "delete_file",
        "status": "ECHEC",
        "message": "Le fichier n'existe pas : {path}",
        "data": False
    },

    # 234 : la suppression du fichier a réussi.
    234: {
        "fonction": "delete_file",
        "status": "SUCCES",
        "message": "Le fichier a été supprimé : {path}",
        "data": True
    },

    # 235 : une erreur système empêche la suppression.
    235: {
        "fonction": "delete_file",
        "status": "ECHEC",
        "message": "Erreur lors de la suppression du fichier : {path}. Détail : {error}",
        "data": False
    },

    # ============================================================
    # CATALOGUE DES MESSAGES : LECTURE DE FICHIERS
    # Codes 300 à 350
    # ============================================================

    # --------------------------------------------------------
    # LECTURE D'UN FICHIER TEXTE
    # --------------------------------------------------------

    300: {
        "fonction": "read_text_aux",
        "status": "SUCCES",
        "message": "Lecture du fichier texte réussie."
    },

    301: {
        "fonction": "read_text_aux",
        "status": "ERREUR",
        "message": "Le paramètre doit être une connexion texte valide."
    },

    302: {
        "fonction": "read_text_aux",
        "status": "ERREUR",
        "message": "Une erreur est survenue pendant la lecture du fichier texte."
    },
    303: {
        "fonction": "read_text",
        "status": "ERREUR",
        "message": "Le paramètre doit être une connexion texte valide.",
        "data" : False
    },

    # --------------------------------------------------------
    # LECTURE D'UN FICHIER BINAIRE
    # --------------------------------------------------------

    310: {
        "fonction": "read_binary_aux",
        "status": "SUCCES",
        "message": "Lecture du fichier binaire réussie."
    },

    311: {
        "fonction": "read_binary_aux",
        "status": "ERREUR",
        "message": "Le paramètre doit être une connexion binaire valide."
    },

    312: {
        "fonction": "read_binary_aux",
        "status": "ERREUR",
        "message": "Une erreur est survenue pendant la lecture du fichier binaire."
    },

    # --------------------------------------------------------
    # LECTURE D'UN NOMBRE DE CARACTÈRES
    # --------------------------------------------------------

    320: {
        "fonction": "read_nb_char_aux",
        "status": "SUCCES",
        "message": "Lecture des caractères réussie."
    },

    321: {
        "fonction": "read_nb_char_aux",
        "status": "ERREUR",
        "message": "Le paramètre doit être une connexion texte valide."
    },

    322: {
        "fonction": "read_nb_char_aux",
        "status": "ERREUR",
        "message": "Le nombre de caractères doit être un entier."
    },

    323: {
        "fonction": "read_nb_char_aux",
        "status": "ERREUR",
        "message": "Le nombre de caractères doit être compris entre 1 et la taille du fichier."
    },

    324: {
        "fonction": "read_nb_char_aux",
        "status": "ERREUR",
        "message": "Une erreur est survenue pendant la lecture des caractères."
    },

    # --------------------------------------------------------
    # LECTURE D'UNE PORTION DE FICHIER TEXTE
    # --------------------------------------------------------

    330: {
        "fonction": "read_char_range",
        "status": "SUCCES",
        "message": "Lecture de la plage de caractères réussie."
    },

    331: {
        "fonction": "read_char_range",
        "status": "ERREUR",
        "message": "La position de début doit être un entier."
    },

    332: {
        "fonction": "read_char_range",
        "status": "ERREUR",
        "message": "La position de fin doit être un entier."
    },

    333: {
        "fonction": "read_char_range",
        "status": "ERREUR",
        "message": "La position de début doit être supérieure ou égale à zéro."
    },

    334: {
        "fonction": "read_char_range",
        "status": "ERREUR",
        "message": "La position de fin doit être supérieure à la position de début."
    },

    # --------------------------------------------------------
    # LECTURE D'UN NOMBRE D'OCTETS
    # --------------------------------------------------------

    340: {
        "fonction": "read_nb_byte_aux",
        "status": "SUCCES",
        "message": "Lecture des octets réussie."
    },

    341: {
        "fonction": "read_nb_byte_aux",
        "status": "ERREUR",
        "message": "Le paramètre doit être une connexion binaire valide."
    },

    342: {
        "fonction": "read_nb_byte_aux",
        "status": "ERREUR",
        "message": "Le nombre d'octets doit être un entier."
    },

    343: {
        "fonction": "read_nb_byte_aux",
        "status": "ERREUR",
        "message": "Le nombre d'octets doit être compris entre 1 et la taille du fichier."
    },

    344: {
        "fonction": "read_nb_byte_aux",
        "status": "ERREUR",
        "message": "Une erreur est survenue pendant la lecture des octets."
    },

    # --------------------------------------------------------
    # LECTURE D'UNE PORTION DE FICHIER BINAIRE
    # --------------------------------------------------------

    350: {
        "fonction": "read_byte_range",
        "status": "SUCCES",
        "message": "Lecture de la plage d'octets réussie."
    }
}



def create_message(code, **params):
    """
    Construit un dictionnaire de résultat à partir du catalogue.

    Args:
        code (int): Code du message.
        **params: Paramètres facultatifs de formatage et/ou de remplacement
            de la donnée de retour (data).

    Returns:
        dict | None: Résultat standardisé, ou None si le code est inconnu.
    """
    information = CATALOGUE_MESSAGES.get(code)
    if information is None:
        return None

    data = params.get("data", information.get("data"))
    mode = params.get("mode", information.get("mode", ""))

    # Tous les paramètres sont disponibles pour les modèles de message.
    format_params = dict(params)
    format_params.setdefault("mode", mode)
    format_params.setdefault("data", data)

    try:
        message = information["message"].format(**format_params)
    except (KeyError, IndexError, ValueError) as error:
        # Signale un défaut de configuration du catalogue au développeur.
        message = (
            f"Erreur de formatage du message {code} : "
            f"{information['message']} ({error})"
        )

    return {
        "code": code,
        "fonction": information["fonction"],
        "status": information["status"],
        "mode": mode,
        "message": message,
        "data": data,
    }
