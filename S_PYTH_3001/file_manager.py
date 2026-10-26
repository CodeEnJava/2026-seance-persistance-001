"""
Gestion des chemins, répertoires et fichiers.

Référence du catalogue : 200.
Les erreurs de validation sont retournées sous forme de dictionnaires.
Les fonctions de ce module ne masquent pas les erreurs système inattendues.
"""

import os

from S_PYTH_3001.catalogue_messages import create_message
from S_PYTH_3001.constantes_gestionnaire_note import (
    MAIN_DIRECTORY,
    TRAINEE_PREFIX,
    TRAINING_SUBJECTS,
)
from S_PYTH_3001.params_connection import WRITE_ONLY_MODE


def _is_error(result):
    """Indique si un résultat standardisé correspond à une erreur."""
    return isinstance(result, dict) and result.get("status") == "ERREUR"


def check_path(path, path_type="dir"):
    """
    Vérifie l'existence et le type d'un chemin.

    Args:
        path (str): Chemin à vérifier.
        path_type (str): 'dir' pour un répertoire ou 'file' pour un fichier.

    Returns:
        dict: Résultat standardisé ; data vaut True ou False si les
        paramètres sont valides, ou None en cas d'erreur de validation.
    """
    if not isinstance(path, str):
        return create_message(201)

    if not isinstance(path_type, str) or path_type not in ("file", "dir"):
        return create_message(202)

    if path_type == "dir":
        exists = os.path.isdir(path)
        return create_message(220, data=exists, path=path)

    exists = os.path.isfile(path)
    return create_message(221, data=exists, path=path)


def create_directory(root, directory_name):
    """
    Crée un répertoire dans une racine existante.

    Returns:
        dict: data vaut -1 si la racine est absente, 0 si le répertoire
        existe déjà, 1 si le répertoire vient d'être créé.
        Une erreur de validation est renvoyée sous forme de dictionnaire.
    """
    if not isinstance(root, str):
        return create_message(203)

    if not isinstance(directory_name, str):
        return create_message(204)

    root_result = check_path(root)
    if _is_error(root_result):
        return root_result

    if not root_result["data"]:
        return create_message(223, root=root)

    new_path = os.path.join(root, directory_name)
    path_result = check_path(new_path)

    if _is_error(path_result):
        return path_result

    if path_result["data"]:
        return create_message(222, path=new_path)

    os.mkdir(new_path)
    return create_message(228, path=new_path)


def list_directory(root):
    """
    Liste les fichiers et les sous-répertoires d'une racine.

    Returns:
        dict: data contient les clés 'dir' et 'file'.
        Si la racine n'existe pas, data vaut None et le message l'indique.
    """
    if not isinstance(root, str):
        return create_message(205)

    root_result = check_path(root)
    if _is_error(root_result):
        return root_result

    if not root_result["data"]:
        return create_message(
            224,
            root=root,
            data=None,
        ) | {"status": "ECHEC", "message": f"Le répertoire n'existe pas : {root}"}

    elements = {"dir": [], "file": []}

    for element in os.listdir(root):
        element_path = os.path.join(root, element)
        if os.path.isdir(element_path):
            elements["dir"].append(element)
        elif os.path.isfile(element_path):
            elements["file"].append(element)

    return create_message(224, root=root, data=elements)


def create_main_directory(root):
    """Crée le répertoire principal de l'application."""
    return create_directory(root, MAIN_DIRECTORY)


def create_trainee_space(root, name):
    """Crée le répertoire personnel d'un stagiaire."""
    if not isinstance(name, str):
        return create_message(211)
    return create_directory(root, TRAINEE_PREFIX + name)


def create_subject_directories(root):
    """
    Crée les répertoires correspondant aux matières.

    Returns:
        dict: Associe chaque matière au résultat de create_directory().
    """
    if not isinstance(root, str):
        return create_message(206)

    results = {}
    for subject in TRAINING_SUBJECTS:
        results[subject] = create_directory(root, subject)
    return results


def add_trainee(root, nom_prenom):
    """
    Crée l'arborescence complète d'un stagiaire.

    data vaut 1 si tous les dossiers ont été créés, 0 si l'arborescence
    existait déjà, et -1 si la création est partielle ou échoue.
    """
    if not isinstance(root, str):
        return create_message(203)
    if not isinstance(nom_prenom, str):
        return create_message(211)

    result_main = create_main_directory(root)
    if _is_error(result_main):
        return result_main
    if result_main.get("data") == -1:
        return result_main

    path_gestion_notes = os.path.join(root, MAIN_DIRECTORY)
    result_trainee = create_trainee_space(path_gestion_notes, nom_prenom)
    if _is_error(result_trainee):
        return result_trainee
    if result_trainee.get("data") == -1:
        return result_trainee

    path_trainee = os.path.join(path_gestion_notes, TRAINEE_PREFIX + nom_prenom)
    result_subjects = create_subject_directories(path_trainee)

    if _is_error(result_subjects):
        return result_subjects

    # Si un résultat de matière n'est pas un dictionnaire ou indique un
    # échec, on conserve le détail des résultats dans le message global.
    if any(
        not isinstance(result, dict)
        or result.get("status") in ("ERREUR", "ECHEC")
        or result.get("data") == -1
        for result in result_subjects.values()
    ):
        return create_message(227, trainee=nom_prenom, data=-1)

    created_count = sum(
        result.get("data") == 1 for result in result_subjects.values()
    )

    if created_count == len(TRAINING_SUBJECTS):
        return create_message(225, trainee=nom_prenom, data=1)

    if created_count == 0:
        return create_message(226, trainee=nom_prenom, data=0)

    return create_message(227, trainee=nom_prenom, data=-1)



def create_file(root, filename, encoding=None):
    """
    Crée un fichier dans un répertoire existant.

    Args:
        root (str): Chemin du répertoire dans lequel créer le fichier.
        filename (str): Nom du fichier à créer.
        encoding (str, optional): Encodage utilisé pour créer le fichier.

    Returns:
        dict: Résultat standardisé issu du catalogue des messages.
              data=True  : le fichier a été créé.
              data=None  : le fichier existe déjà.
              data=False : une erreur système est survenue.
    """

    # Vérifie que le chemin du répertoire est une chaîne de caractères.
    if not isinstance(root, str):
        return create_message(207)

    # Vérifie que le nom du fichier est une chaîne de caractères.
    if not isinstance(filename, str):
        return create_message(208)

    # Vérifie que le chemin du répertoire n'est pas vide.
    if not root.strip():
        return create_message(209, root=root)

    # Vérifie que le nom du fichier n'est pas vide.
    if not filename.strip():
        return create_message(208)

    # Vérifie l'existence et la validité du répertoire racine.
    root_result = check_path(root)

    # Si la vérification du chemin a produit une erreur,
    # retourne directement le message correspondant du catalogue.
    if _is_error(root_result):
        return root_result

    # Si le répertoire n'existe pas, la création du fichier est impossible.
    if not root_result["data"]:
        return create_message(209, root=root)

    # Construit le chemin complet du fichier à créer.
    # os.path.join() adapte la construction du chemin au système utilisé.
    new_filename = os.path.join(root, filename)

    # Vérifie si le chemin obtenu correspond à un fichier existant.
    file_result = check_path(new_filename, "file")

    # Si la vérification du chemin a produit une erreur,
    # retourne le résultat obtenu sans le modifier.
    if _is_error(file_result):
        return file_result

    # Si le fichier existe déjà, retourne le message correspondant
    # sans tenter de créer ou de modifier ce fichier.
    if file_result["data"]:
        return create_message(231, path=new_filename)

    try:
        # Si un encodage UTF-8 est demandé, ouvre le fichier
        # avec cet encodage explicite.
        if encoding == "utf-8":
            with open(
                new_filename,
                WRITE_ONLY_MODE,
                encoding="utf-8"
            ):
                # Le fichier est créé à l'ouverture.
                # Le bloc with assure ensuite la fermeture du fichier.
                pass

        else:
            # Si aucun encodage UTF-8 n'est demandé,
            # utilise le mode d'ouverture défini dans la constante.
            with open(new_filename, WRITE_ONLY_MODE):
                # Le fichier est créé puis fermé automatiquement.
                pass

        # Retourne le message de succès défini dans le catalogue.
        return create_message(230, path=new_filename)

    except OSError as error:
        # Intercepte les erreurs système liées à la création du fichier :
        # droits insuffisants, chemin inaccessible, etc.
        # Transmet les informations utiles au catalogue des messages.
        return create_message(
            232,
            path=new_filename,
            error=str(error)
        )



def delete_file(filename):
    """
    Supprime un fichier existant.

    Args:
        filename (str): Chemin complet du fichier à supprimer.

    Returns:
        dict: Résultat standardisé issu du catalogue des messages.
              data=True  : le fichier a été supprimé.
              data=False : le fichier est absent ou la suppression a échoué.
    """

    # Vérifie que le paramètre filename est une chaîne de caractères.
    # Si le type est invalide, retourne le message correspondant au catalogue.
    if not isinstance(filename, str):
        return create_message(210)

    # Vérifie que le chemin fourni correspond à un fichier.
    # Le résultat est un dictionnaire contenant notamment la clé "data".
    file_result = check_path(filename, "file")

    # Si la vérification du chemin a détecté une erreur,
    # retourne directement le dictionnaire obtenu.
    if _is_error(file_result):
        return file_result

    # Si le fichier n'existe pas, retourne le message du catalogue
    # prévu pour signaler l'absence du fichier.
    if not file_result["data"]:
        return create_message(233, path=filename)

    try:
        # Supprime le fichier situé au chemin indiqué.
        os.remove(filename)

        # Retourne le message de succès défini dans le catalogue.
        return create_message(234, path=filename)

    except OSError as error:
        # Intercepte les erreurs système empêchant la suppression,
        # par exemple un accès refusé ou un fichier utilisé.
        # Retourne un message détaillé issu du catalogue.
        return create_message(
            235,
            path=filename,
            error=str(error)
        )
