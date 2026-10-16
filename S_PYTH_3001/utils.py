import os


def get_os_type():
    """
    Déterminer le type de système d'exploitation
    Returns:
        int : 1 si le système est Windows (nt)
            : 0 si système est Linux

    """
    if os.name == "nt":
        return 1
    return 0
