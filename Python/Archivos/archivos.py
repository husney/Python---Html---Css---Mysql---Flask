# x crea un archivo si no existe
# w crea una archivo  si no existe y escribe
# r lee una archivo
# a agrega texto a un archivo

#a = open("ArchivoCreado.txt", "w")

#a.write("Prueba")
#a.writelines("\nIngreso de datos")
#a.close()  # Cierre del archivo

#lectura = open("ArchivoCreado.txt")


# read lee  todo el archivo
    #print(lectura.read())
# readline lee linea por linea como un método Next (generador)
    #print(lectura.readline()) ## linea 1
    #print(lectura.readline()) ## linea 2 ....

#readlines lee todas las lineas  y las regresa en una lista
    #print(lectura.readlines())

#for linea in lectura:
#    print(linea)

# iteración de archivo se puede imprimir las lineas de un arhcivo con el ciclo for

#lectura.close()

import os

if os.path.exists("ArchivoCreado.txt"):
    os.remove("ArchivoCreado.txt")
else:
    print("El archivo no existe")


if os.path.exists("carpeta"):
    os.rmdir("carpeta")
else:
    print("La carpeta no existe")
