import os
import stat
import subprocess



def check_path(path, path_type="dir"):
    """
    Vérifie si un chemin donné correspond à un répertoire ou à un fichier.

    Args:
        path (str): Le chemin du fichier ou du répertoire à vérifier.
        path_type (str, optional): Le type d'élément attendu ('dir' ou 'file').
            Défaut à 'dir'.

    Returns:
        bool: True si le chemin existe et correspond au type demandé,
        False sinon.

    Raises:
        TypeError: Si 'path' ou 'path_type' ne sont pas des chaînes de caractères.
        ValueError: Si 'path_type' n'est ni 'file' ni 'dir'.
    """

    if not isinstance(path, str):
        raise TypeError(
            "Le premier paramètre doit être une "
            "chaine de caractères, contenant un chemin."
        )

    # le second paramètre est un paramètre optionnel, par défaut à dir
    if not isinstance(path_type, str):
        raise TypeError(
            "Le second paramètre doit être une "
            "chaine de caractères, devra contenir 'dir' ou 'file'."
        )

    if path_type != "file" and path_type != "dir":
        raise ValueError(
            "La valeur du paramètre 'path_type' doit être 'file' ou 'dir'."
        )

    if path_type == "dir":
        return os.path.isdir(path)
    return os.path.isfile(path)

def create_directory_old(root, directory_name):
    """

    :param root:
    :param directory_name:
    :return:
    """
    if not isinstance(root, str):
        raise TypeError("Le premier paramètre doit être une "
                        "chaine de caractères, contenant la racine "
                        "ou on va placer le nouveau dossier.")

    # le second paramètre est un paramètre optionnel, par défaut à dir
    if not isinstance(directory_name, str):
        raise TypeError("Le second paramètre doit être une "
                        "chaine de caractères, quii contient le nom du dossier à créer.")

    if not check_path(root):
        return False

    # on peut réaliser la création du nouveau dossier, si et seulement si
    # celui-ci n'existe pas
    new_path = os.path.join(root,directory_name )
    if not check_path(new_path):
        os.mkdir(new_path)
    return True


def create_directory(root, directory_name):
    """
        Crée un nouveau dossier dans un répertoire existant.

        Le chemin du nouveau dossier est construit à partir du répertoire racine
        et du nom du dossier à créer. Si le dossier existe déjà, aucune création
        n'est effectuée.

        :param root: Chemin du répertoire dans lequel créer le nouveau dossier.
        :type root: str
        :param directory_name: Nom du dossier à créer.
        :type directory_name: str
        :return: True si le dossier existe ou a été créé, False si le répertoire
                 racine n'existe pas.
        :rtype: bool
        :raises TypeError: Si root ou directory_name n'est pas une chaîne de caractères.
    """
    if not isinstance(root, str):
        raise TypeError("Le premier paramètre doit être une "
                        "chaine de caractères, contenant la racine "
                        "ou on va placer le nouveau dossier.")

    # le second paramètre est un paramètre optionnel, par défaut à dir
    if not isinstance(directory_name, str):
        raise TypeError("Le second paramètre doit être une "
                        "chaine de caractères, qui contient le nom du dossier à créer.")

    if not check_path(root):
        return -1

    # on peut réaliser la création du nouveau dossier, si et seulement si
    # celui-ci n'existe pas
    new_path = os.path.join(root, directory_name)
    if not check_path(new_path):
        os.mkdir(new_path)
        return 1
    return 0

def list_directory(root):
    """
        Liste les fichiers et les dossiers contenus dans un répertoire.

        Le contenu du répertoire indiqué par `root` est analysé et classé
        dans un dictionnaire contenant deux listes :

        - `dir` : noms des sous-répertoires ;
        - `file` : noms des fichiers.

        :param root: Chemin du répertoire à analyser.
        :type root: str
        :return: Dictionnaire contenant les listes des dossiers et des fichiers.
        :rtype: dict
        :raises TypeError: Si `root` n'est pas une chaîne de caractères.
        :raises FileNotFoundError: Si le chemin indiqué n'existe pas.
        :raises NotADirectoryError: Si `root` ne désigne pas un répertoire.
    """
    if not isinstance(root, str):
        raise TypeError("Le premier paramètre doit être une "
                        "chaine de caractères, contenant une racine ")
    print(root)

    if not check_path(root):
        return None

    ls = {
           "dir":[],
           "file":[]
         }
    list_folders_files = os.listdir(root)

    for element in list_folders_files:
        if check_path(os.path.join(root,element)):
            ls["dir"].append(element)
        else:
            ls["file"].append(element)

    return ls

# constantes
MAIN_DIRECTORY = "Gestion_Notes"
TRAINEE_PREFIX = "2026_"
TRAINING_SUBJECTS = [
                        "S_MATH",
                        "S_ALGO",
                        "S_PYTH",
                        "S_TPTD",
                        "S_PROJ"
]

def create_main_directory(root):
    """
       Crée le répertoire principal de l'application.

       :param root: Chemin dans lequel créer le répertoire.
       :type root: str
       :return: Code indiquant le résultat de la création.
       :rtype: int
    """
    return create_directory(root,MAIN_DIRECTORY)


def create_trainee_space(root, name) :
    """
        Crée le répertoire personnel d'un stagiaire.

        :param root: Chemin du répertoire principal.
        :type root: str
        :param nom_prenom: Nom et prénom du stagiaire.
        :type nom_prenom: str
        :return: Code indiquant le résultat de la création.
        :rtype: int
    """
    return create_directory(root,TRAINEE_PREFIX+name)

def create_subject_directories(root):
    """
    Crée les répertoires correspondant aux matières de formation.

    :param root: Chemin du répertoire du stagiaire.
    :type root: str
    :return: Dictionnaire associant chaque matière au résultat de sa création.
    :rtype: dict
    :raises TypeError: Si ``root`` n'est pas une chaîne de caractères.
    """
    if not isinstance(root, str):
        raise TypeError(
            "Le paramètre doit être une chaine de caractères contenant un chemin."
        )

    results = {}

    for subject in TRAINING_SUBJECTS:
        results[subject] = create_directory(root, subject)

    return results


def add_trainee(root, nom_prenom):
    """
        Crée l'ensemble des répertoires nécessaires à un stagiaire.

        :param root: Chemin racine de stockage.
        :type root: str
        :param nom_prenom: Nom et prénom du stagiaire.
        :type nom_prenom: str
        :return: Résultats des opérations de création.
        :rtype: dict
    """
    result_main = create_main_directory(root)

    if result_main < 0:
        return {"main":result_main}

    path_gestion_notes = os.path.join(root,MAIN_DIRECTORY)

    result_trainee = create_trainee_space(path_gestion_notes,nom_prenom)

    if result_trainee < 0:
        return {"main":result_main,
                "trainee":result_trainee}

    path_trainee = os.path.join(path_gestion_notes,TRAINEE_PREFIX+nom_prenom)

    result_subjects = create_subject_directories(path_trainee)

    return {
        "main": result_main,
        "trainee":result_trainee,
        "subjects": result_subjects
    }


