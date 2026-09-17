from file_connection import open_connection, BINARY_READ_MODE
# importq
from reader import read_text_aux, read_text, read_binary_aux, read_binary

# Test N°1
# Utilisation de la fonction read_text_aux

# Il faut réaliser une connexion vers le fichier
path = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.rtf"
obj_cnx = open_connection(path) # mode READ_ONLY_MODE par défaut

datas = read_text_aux(obj_cnx)

print(datas)

path = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple1.rtf"
obj_cnx = open_connection(path) # mode READ_ONLY_MODE par défaut
if obj_cnx is not None:
    datas = read_text_aux(obj_cnx)
    print(datas)
else:
    print("La connexion vers le fichier a échoué.")

# test N°2
# utilisation de la fonction read_test(filename)
print("*"*100)
print("Test N°2 : la fonction read_txt")
path_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"
# Pour générer une erreur, activer la ligne suivante :
# path_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/image10.png"
# path_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple10.txt"
data_txt = read_text(path_txt)

print(data_txt)


# test N°3
# Utilisation de la fonction read_binary_aux
print("*"*100)
print("Test N°3 : la fonction read_binary_aux")

# Il faut réaliser une connexion vers le fichier
path = "/Users/steph.barois.dev/Downloads/python/Gestions/image.png"
# Pour générer une erreur, activer la ligne suivante :
# path = "/Users/steph.barois.dev/Downloads/python/Gestions/image10.png"
obj_cnx = open_connection(path,BINARY_READ_MODE)
if obj_cnx is not None:
    data_png = read_binary_aux(obj_cnx)
    print(data_png)
else:
    print("La connexion entre API et le fichier n'a pas été réalisée.")


# test N°4
# utilisation de la fonction read_binary(filename)
print("*"*100)
print("Test N°4 : la fonction read_binary")
path_image = "/Users/steph.barois.dev/Downloads/python/Gestions/image.png"
# Pour générer une erreur, activer la ligne suivante :
# path_image = "/Users/steph.barois.dev/Downloads/python/Gestions/image10.png"
data_image = read_binary(path_image)

print(data_image)
