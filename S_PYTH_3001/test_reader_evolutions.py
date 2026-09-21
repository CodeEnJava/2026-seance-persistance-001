import os

from S_PYTH_3001.reader import read_binary, read_nb_byte_aux, read_nb_byte, read_byte_range
from reader import (
    size,
    read_nb_char_aux,
    read_text,
    read_nb_char, read_char_range
)

from file_connection import (
    open_connection,
    BINARY_READ_MODE
)
#------------------------------------------
# Configurations
#------------------------------------------
if os.name == "nt":
    filename_txt = "C:\\Users\\stebar\\Python\\Gestions\\exemple.txt"
    filename_picture = "C:\\Users\\stebar\\Python\\Gestions\\image.png"
else:
    filename_txt = "/Users/steph.barois.dev/Downloads/python/Gestions/exemple.txt"
    filename_picture = "/Users/steph.barois.dev/Downloads/python/Gestions/image.png"

#------------------------------------------
# Objets de connexions
#------------------------------------------
obj_cnx_txt = open_connection(filename_txt)

obj_cnx_picture = open_connection(filename_picture,BINARY_READ_MODE)

#------------------------------------------
# Connaitre la taille des fichiers
#------------------------------------------


size_txt = size(obj_cnx_txt)

size_picture = size(obj_cnx_picture)

print(f"La taille du fichier texte est de {size_txt} octets")

print(f"La taille du fichier image est de {size_picture} octets")

#------------------------------------------
# Utiliser la fonction read_nb_char_aux
# Pour lire un bloc de données depuis le
# debut du fichier
#------------------------------------------
data_all =  read_text(filename_txt)
segment_txt = read_nb_char_aux(obj_cnx_txt,1)

print(f"Le text au complet :\n{data_all}")

print(f"Un segment de données : \n{segment_txt}")

#------------------------------------------
# Utiliser la fonction read_nb_char
# Pour lire un bloc de données depuis le
# debut du fichier
#------------------------------------------
print("la suite")
segment_txt = read_nb_char(filename_txt,32)
print("Utilisation de  la fonction 'read_nb_char' :")
print(f"Un segment de données : \n{segment_txt}")

#Fichier pour le test de lecture
#Fichier
#Fichier pour
#Fichier pour le test
#Fichier pour le test de lecture
#Fichier pour le test de lecture

#------------------------------------------
# Utiliser la fonction read_char_range
# Pour lire un bloc de données depuis une
# position du curseur défini dans un fichier
#------------------------------------------

segment_txt = read_char_range(filename_txt, 32, 64)

print("Utilisation de  la fonction 'read_char_range' :")
print(f"Un segment de données : \n{segment_txt}")
#avec la fonction reader_text(fil


#------------------------------------------
# Utiliser la fonction read_nb_byte_aux
# Pour lire un bloc de données depuis le
# debut du fichier
#------------------------------------------
data_all =  read_binary(filename_picture)
segment_picture = read_nb_byte_aux(obj_cnx_picture,10)

print(f"Le fichier binaire au complet :\n{data_all}")

print(f"Un segment de données : \n{segment_picture}")


#------------------------------------------
# Utiliser la fonction read_nb_byte
# Pour lire un bloc de données depuis le
# debut du fichier
#------------------------------------------
print("la suite")
segment_picture = read_nb_byte(filename_picture,10)
print("Utilisation de  la fonction 'read_nb_byte' :")
print(f"Un segment de données : \n{segment_picture}")


#------------------------------------------
# Utiliser la fonction read_byte_range
# Pour lire un bloc de données depuis une
# position du curseur défini dans un fichier
#------------------------------------------

segment_picture = read_byte_range(filename_picture, 12, 24)

print("Utilisation de  la fonction 'read_byte_range' :")
print(f"Un segment de données : \n{segment_picture}")