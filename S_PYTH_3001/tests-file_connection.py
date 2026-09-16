# TESTS
from S_PYTH_3001.file_connection import open_connection, BINARY_WRITE_READ_MODE, READ_ONLY_MODE, close_connection

path_1 = "C:\\Users\\stebar\\Python\\exemple_1.txt"
path_2 =  "C:\\Users\\stebar\\Python\\exemple.txt"

obj_cnx_1 = open_connection(path_1,BINARY_WRITE_READ_MODE)
obj_cnx_2 = open_connection(path_2,READ_ONLY_MODE)

# Traitement à faire
print(obj_cnx_1)
print(obj_cnx_2)
# fin des traitement

end_1 = close_connection(obj_cnx_1)
end_2 = close_connection(obj_cnx_2)

if end_1 == 1 :
    print("La connexion au fichier est fermée")

if end_2 == 1 :
    print("La connexion au fichier est fermée")
