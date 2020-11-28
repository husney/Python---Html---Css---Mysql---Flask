"""
importa todo el documento se le puede agregar un alias con "as"
import funciones_matematicas 

Importa solo la función descrita
from funciones_matematicas import sumar

importa todas las funciones del modulo
from funciones_matematicas import *  """


"""Paquetes
Son direcorios, carpetas en donde se al macenan modulos
para crear un paquete es necesario crear una carpeta llamada __init__.py
"""



"""
Crear una carpeta y agregar un archivo __init__.py
hace que los archivos que se encuentren ne la carpeta actuen como
un paquete
"""

from Modulos.paquete1.sup_paquete.Coche import Vehiculo

miVehiculo = Vehiculo(5, True, 10)
print(miVehiculo.getEstado())


