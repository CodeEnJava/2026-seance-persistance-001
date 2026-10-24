
"""
Gestion des chemins, répertoires et fichiers.

Référence du catalogue : 200

Les erreurs de validation sont retournées sous forme de dictionnaires
via le catalogue centralisé catalogue_messages.py.

Codes d'erreur :
    201 : chemin invalide dans check_path
    202 : type de chemin invalide
    203 : racine invalide dans create_directory
    204 : nom de répertoire invalide
    205 : racine invalide dans list_directory
    206 : racine invalide dans create_subject_directories
    207 : racine invalide dans create_file
    208 : nom de fichier invalide
    209 : répertoire racine invalide
    210 : chemin invalide dans delete_file
    211 : nom de stagiaire invalide

Retours historiques :
    create_directory : -1 si la racine n'existe pas,
                       0 si le répertoire existe déjà,
                       1 si le répertoire est créé.
"""

import os

from S_PYTH_3001.catalogue_messages import create_message
from S_PYTH_3001.constantes_gestionnaire_note import MAIN_DIRECTORY, TRAINEE_PREFIX, TRAINING_SUBJECTS
from S_PYTH_3001.params_connection import WRITE_ONLY_MODE


# --------------------------------------------------
# Vérification des chemins
# --------------------------------------------------

def check_path(path, path_type="dir"):
    """
    Vérifie l'existence d'un fichier ou d'un répertoire.

    Args:
        path (str): Chemin à vérifier.
        path_type (str): 'dir' pour un répertoire ou 'file'
            pour un fichier. Par défaut : 'dir'.

    Returns:
        bool | dict:
            True si le chemin existe et correspond au type demandé.
            False si le chemin n'existe pas ou ne correspond pas au type.
            Dictionnaire d'erreur 201 ou 202 si les paramètres
            sont invalides.
    """
    if not isinstance(path, str):
        return create_message(201)

    if not isinstance(path_type, str):
        return create_message(202)

    if path_type not in ("file", "dir"):
        return create_message(202)

    if path_type == "dir":
        flag = os.path.isdir(path)
        return create_message(220,data = flag)

    flag = os.path.isfile(path)
    return create_message(221,data = flag)


# --------------------------------------------------
# Création des répertoires
# --------------------------------------------------

def create_directory_old(root, directory_name):
    """
    Ancienne version conservée pour compatibilité.

    Args:
        root (str): Répertoire racine.
        directory_name (str): Nom du répertoire à créer.

    Returns:
        bool | dict:
            True si l'opération est possible ou déjà réalisée.
            False si la racine n'existe pas.
            Dictionnaire d'erreur en cas de paramètres invalides.
    """
    if not isinstance(root, str):
        return create_message(203)

    if not isinstance(directory_name, str):
        return create_message(204)

    result = check_path(root)

    print("ligne 99 : ",result)

    if isinstance(result, dict) and result.get("data") is None:
        return result

    if not result.get("data"):
        return False

    new_path = os.path.join(root, directory_name)
    result = check_path(new_path)

    if isinstance(result, dict):
        return result

    if not result:
        os.mkdir(new_path)

    return True


def create_directory(root, directory_name):
    """
    Crée un répertoire dans une racine existante.

    Args:
        root (str): Chemin du répertoire racine.
        directory_name (str): Nom du répertoire à créer.

    Returns:
        int | dict:
            -1 si la racine n'existe pas ;
             0 si le répertoire existe déjà ;
             1 si le répertoire a été créé ;
            dictionnaire si un paramètre est invalide.
    """
    if not isinstance(root, str):
        return create_message(203)

    if not isinstance(directory_name, str):
        return create_message(204)

    result = check_path(root)

    if result.get("data") is None:
        return result

    if not result.get("data"):
        return create_message(224, data = -1)

    new_path = os.path.join(root, directory_name)
    result = check_path(new_path)

    if result.get("data") is None:
        return result

    if not result.get("data"):
        os.mkdir(new_path)
        return create_message(221, data = 1)

    return create_message(222, data = 0)


# --------------------------------------------------
# Liste des fichiers et des répertoires
# --------------------------------------------------

def list_directory(root):
    """
    Liste les fichiers et les sous-répertoires d'une racine.

    Args:
        root (str): Chemin du répertoire à analyser.

    Returns:
        dict | None:
            Dictionnaire contenant les listes 'dir' et 'file'.
            None si le répertoire n'existe pas.
            Dictionnaire d'erreur 205 si root est invalide.

    Note:
        Les erreurs système de os.listdir ne sont pas interceptées.
    """
    if not isinstance(root, str):
        return create_message(205)

    result = check_path(root)

    if result.get("data") is None:
        return result

    if not result.get("data"):
        return result

    elements = {
        "dir": [],
        "file": []
    }

    for element in os.listdir(root):
        element_path = os.path.join(root, element)
        result = check_path(element_path)

        if isinstance(result, dict):
            return result

        if result:
            elements["dir"].append(element)
        else:
            elements["file"].append(element)

    return create_message(224, mode=root, data=elements)



def create_main_directory(root):
    """
    Crée le répertoire principal de l'application.

    Args:
        root (str): Chemin racine de stockage.

    Returns:
        int | dict: Code de create_directory ou dictionnaire d'erreur.
    """
    return create_directory(root, MAIN_DIRECTORY)


def create_trainee_space(root, name):
    """
    Crée le répertoire personnel d'un stagiaire.

    Args:
        root (str): Répertoire principal.
        name (str): Nom et prénom du stagiaire.

    Returns:
        int | dict: Code de création ou dictionnaire d'erreur.
    """
    if not isinstance(name, str):
        return create_message(211)

    return create_directory(root, TRAINEE_PREFIX + name)


def create_subject_directories(root):
    """
    Crée les répertoires correspondant aux matières.

    Args:
        root (str): Répertoire personnel du stagiaire.

    Returns:
        dict: Dictionnaire associant chaque matière à son résultat,
              ou dictionnaire d'erreur 206 si root est invalide.
    """
    if not isinstance(root, str):
        return create_message(206)

    results = {}

    for subject in TRAINING_SUBJECTS:
        result = create_directory(root, subject)
        results[subject] = result

    print(f"results: {results}")
    return results


def add_trainee(root, nom_prenom):
    """
    Crée l'arborescence complète d'un stagiaire.

    Args:
        root (str): Racine de stockage.
        nom_prenom (str): Nom et prénom du stagiaire.

    Returns:
        dict: Résultats des créations ou dictionnaire d'erreur.
    """
    result_main = create_main_directory(root)

    if result_main.get("data") < 0:
        return result_main

    path_gestion_notes = os.path.join(root, MAIN_DIRECTORY)
    result_trainee = create_trainee_space(
        path_gestion_notes, nom_prenom
    )

    if result_trainee.get("data") < 0:
        return result_trainee

    path_trainee = os.path.join(
        path_gestion_notes, TRAINEE_PREFIX + nom_prenom
    )

    result_subjects = create_subject_directories(path_trainee)
    exists = 0
    for subject in result_subjects:
        # si tous les sujets sont à 1 construction réussie
        # si tous les sujets sont à 0 arborescence existe
        if result_subjects.get(subject).get("data")<0:
            # si un sujet est à -1 echec
            return create_message(227, data=0, mode=subject)
        elif result_subjects.get(subject).get("data") == 1:
           exists += 1

    if exists == 0:
            return create_message(226,data=1,mode=nom_prenom)

    return create_message(22,data=1,mode=nom_prenom)


# --------------------------------------------------
# Création d'un fichier
# --------------------------------------------------

def create_file(root, filename, encoding=None):
    """
    Crée un fichier dans un répertoire existant.

    Args:
        root (str): Répertoire dans lequel créer le fichier.
        filename (str): Nom du fichier.
        encoding (str | None): Encodage demandé.
            'utf-8' pour un fichier texte UTF-8.

    Returns:
        bool | None | dict:
            True si le fichier est créé.
            None si le fichier existe déjà.
            Dictionnaire d'erreur 207, 208 ou 209 si les
            paramètres ou la racine sont invalides.

    Note:
        Les erreurs système d'ouverture ou d'écriture ne sont pas
        interceptées.
    """
    if not isinstance(root, str):
        return create_message(207)

    if not isinstance(filename, str):
        return create_message(208)

    result = check_path(root)

    if isinstance(result, dict):
        return result

    if not result:
        return create_message(209, root=root)

    new_filename = os.path.join(root, filename)
    result = check_path(new_filename, "file")

    if isinstance(result, dict):
        return result

    if result:
        return None

    if encoding == "utf-8":
        with open(
            new_filename, WRITE_ONLY_MODE, encoding="utf-8"
        ):
            pass
    else:
        with open(new_filename, WRITE_ONLY_MODE):
            pass

    return True


# --------------------------------------------------
# Suppression d'un fichier
# --------------------------------------------------

def delete_file(filename):
    """
    Supprime un fichier existant.

    Args:
        filename (str): Chemin complet du fichier à supprimer.

    Returns:
        bool | dict:
            True si le fichier est supprimé.
            False si le fichier n'existe pas.
            Dictionnaire d'erreur 210 si filename est invalide.

    Note:
        Les erreurs système de os.remove ne sont pas interceptées.
    """
    if not isinstance(filename, str):
        return create_message(210)

    result = check_path(filename, "file")

    if isinstance(result, dict):
        return result

    if not result:
        return False

    os.remove(filename)

    return True
