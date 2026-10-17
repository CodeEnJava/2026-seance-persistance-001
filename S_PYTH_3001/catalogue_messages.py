
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
            "au fichier dans le mode suivant : {mode}"
        ),
        "type": "ERREUR"
    },

    102: {
        "fonction": "open_connection",
        "message": (
            "Le mode d'ouverture du fichier n'est pas valide : {mode}"
        ),
        "type": "ERREUR"
    },

    103: {
        "fonction": "open_connection",
        "message": (
            "Le nom du fichier doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    104: {
        "fonction": "open_connection",
        "message": (
            "Le nom du fichier doit être une chaîne non vide."
        ),
        "type": "ERREUR"
    },

    105: {
        "fonction": "close_connection",
        "message": (
            "Le paramètre fourni n'est pas une connexion valide."
        ),
        "type": "ERREUR"
    },

    110: {
        "fonction": "close_connection",
        "message": "La connexion au fichier a été fermée.",
        "type": "SUCCES"
    },

    # --------------------------------------------------
    # Module 200 : file_manager.py
    # --------------------------------------------------

    201: {
        "fonction": "check_path",
        "message": "Le chemin doit être une chaîne de caractères.",
        "type": "ERREUR"
    },

    202: {
        "fonction": "check_path",
        "message": (
            "Le type de chemin doit être 'file' ou 'dir'."
        ),
        "type": "ERREUR"
    },

    203: {
        "fonction": "create_directory",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    204: {
        "fonction": "create_directory",
        "message": (
            "Le nom du répertoire doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    205: {
        "fonction": "list_directory",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    206: {
        "fonction": "create_subject_directories",
        "message": (
            "Le chemin doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    207: {
        "fonction": "create_file",
        "message": (
            "Le chemin racine doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    208: {
        "fonction": "create_file",
        "message": (
            "Le nom du fichier doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    209: {
        "fonction": "create_file",
        "message": (
            "Le répertoire racine n'existe pas ou n'est pas valide : {root}"
        ),
        "type": "ERREUR"
    },

    210: {
        "fonction": "delete_file",
        "message": (
            "Le chemin du fichier doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    },

    211: {
        "fonction": "create_trainee_space",
        "message": (
            "Le nom du stagiaire doit être une chaîne de caractères."
        ),
        "type": "ERREUR"
    }

}


def create_message(code, **params):
    """
    Construit un dictionnaire contenant un message du catalogue.

    Args:
        code (int): Code du message à récupérer.
        **params: Paramètres nécessaires au formatage du message.

    Returns:
        dict: Dictionnaire contenant le code et le message,
              ou None si le code est inconnu.
    """
    information = CATALOGUE_MESSAGES.get(code)

    if information is None:
        return None

    message = information["message"].format(**params)

    return {
        code: (
            f"fn : {information['fonction']}\n"
            f"{message}"
        )
    }
