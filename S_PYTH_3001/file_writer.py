from S_PYTH_3001.file_connection import open_connection, close_connection
from S_PYTH_3001.file_manager import check_path
from S_PYTH_3001.file_reader import read_text
from S_PYTH_3001.params_connection import APPEND_MODE, WRITE_READ_MODE


# une fonction pour ajouter du texte à la fin d'un fichier
# une fonction pour ajouter du texte au début du fichier
# une fonction qui permet de choisir à la fin ou au debut

def append_txt(filename, txt):
    """
        Ajoute un texte à la fin d'un fichier existant.
        La fonction vérifie le type des paramètres ainsi que l'existence
        du fichier avant d'ouvrir celui-ci en mode ajout.

        Le contenu fourni est alors ajouté à la fin du fichier sans modifier son contenu existant.

        Args:
            filename (str): Chemin complet du fichier dans lequel le texte doit être ajouté.
            txt (str): Texte à ajouter à la fin du fichier.

        Returns: int:   - 1 si le texte a été ajouté avec succès.
                        - 0 si l'ouverture du fichier a échoué.
                        - -1 si le fichier n'existe pas.

        Raises: TypeError: Si `filename` ou `txt` n'est pas une chaîne de caractères.
    """
    if not isinstance(filename,str):
        raise TypeError(
            "Le premier paramètre doit-être une chaine de caractères, contenant le nom du fichier"
            "complet."
        )

    if not isinstance(filename,str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant "
            "le texte à ajouter à la fin du fichier."
        )

    if not check_path(filename,"file"):
        print(f" le fichier {filename} n'existe pas.")
        return -1

    obj_cnx = open_connection(filename,APPEND_MODE)

    if obj_cnx:
        obj_cnx.write(txt)
        close_connection(obj_cnx)
        return 1
    else:
        print("Un problème lors de la réalisation de l'objet de connexion.")
        return 0


def prepend(filename,txt):
    """
        Ajoute un texte au début d'un fichier existant.
        La fonction lit d'abord le contenu actuel du fichier, puis réécrit
        le fichier avec le nouveau texte placé au début. Le contenu initial
        du fichier est ensuite ajouté à la suite du nouveau texte.

        Cette méthode est adaptée aux fichiers de petite taille,
        car l'intégralité du contenu du fichier est temporairement chargée en mémoire.

        Args:
            filename (str): Chemin complet du fichier dans lequel le texte doit être ajouté.
            txt (str): Texte à ajouter au début du fichier.

        Returns:
            int:    - 1 si le texte a été ajouté avec succès.
                    - 0 si l'ouverture du fichier a échoué.
                    - -1 si le fichier n'existe pas.

        Raises:
            TypeError: Si `filename` ou `txt` n'est pas une chaîne de caractères.

        """
    if not isinstance(filename,str):
        raise TypeError(
            "Le premier paramètre doit-être une chaine de caractères, contenant le nom du fichier"
            "complet."
        )

    if not isinstance(filename,str):
        raise TypeError(
            "Le second paramètre doit-être une chaine de caractères, contenant "
            "le texte à ajouter à la fin du fichier."
        )

    if not check_path(filename,"file"):
        print(f" le fichier {filename} n'existe pas.")
        return -1

    # faire une sauvegarde du fichier, cette fonction sera utile pour le projet
    # Car nous manipulons des fichiers de faibles tailles (moins de 100 ko)
    # prévoir dans le futur, un message si la taille du fichier est sup à 100ko

    content = read_text(filename)

    # le contenu du fichier a été supprimé, après avoir créé l'objet obj_cnx
    obj_cnx = open_connection(filename,WRITE_READ_MODE)

    if obj_cnx:
        # il faut injecter le texte dans le fichier
        # pour rappel le fichier est vide, donc le texte sera ajouté au début
        obj_cnx.write(txt)
        close_connection(obj_cnx)
        append_txt(filename,content)
        return 1
    else:
        print("Un problème lors de la réalisation de l'objet de connexion.")
        return 0

def write_txt(filename,txt,append=True):
    """
        Ajoute un texte au début ou à la fin d'un fichier.
        Cette fonction constitue une interface permettant de choisir l'emplacement
        où le texte doit être ajouté.

        Le paramètre `append` détermine le comportement :
            - True : ajout du texte à la fin du fichier.
            - False : ajout du texte au début du fichier.

        Args:
            filename (str): Chemin complet du fichier à modifier.
            txt (str): Texte à ajouter au fichier.
            append (bool, optional):    Indique la position d'ajout du texte.
                                        La valeur `True` ajoute le texte à la fin du fichier.
                                        La valeur `False` ajoute le texte au début du fichier.
                                        Par défaut : True.

        Returns:
            int:    - 1 si le texte a été ajouté avec succès.
                    - 0 si l'ouverture ou la modification du fichier a échoué.
                    - -1 si le fichier n'existe pas.

        Raises:
            TypeError:  Si `filename` ou `txt` n'est pas une chaîne de caractères,
                        ou si `append` n'est pas un booléen.

    """

    if not isinstance(append,bool):
        raise TypeError(
            "Le troisième paramètre doit être un type boolean."
        )

    if append:
        return append_txt(filename,txt)
    return prepend(filename,txt)

