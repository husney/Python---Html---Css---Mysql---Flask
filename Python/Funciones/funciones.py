#Bloques de codigo que permiten reutilizar código y pueden regresar un valor o realizar una acción
# def es la palabra reservada para "DEFINIR" funciones

def suma(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return n1 + n2

print(suma(5,2))

def decirAlgo():
    print("Hola Buen día")

decirAlgo()


def parametrosDefault(nombre = "santi"):
    print("Hola " + nombre)

parametrosDefault()

parametrosDefault("Valentina Marin")

def parametrosLista(*ingredientes):
    print("Los ingredientes son: ", ingredientes)

parametrosLista("Tomate", "Lechuga", "Queso", "Salsa", "Cebolla")


def parametrosSinOrden(edad, apellido, nombre):
    print("Hola " + nombre + " " + apellido + " tiene  " + str(edad))


parametrosSinOrden(nombre = "Sara", edad= 23, apellido = "Orrego")

def parametrosDiccionario(**kwargs):
    print("Recibido como diccionario nombre = " , kwargs["nombre"] + "\n" +
        "Recibido como diccionario apellido = " , kwargs["apellido"])

parametrosDiccionario(nombre = "Alejandra", apellido = "Aleja")

def mi_recursiva(n):
    print(n)
    if(n > 0):
        mi_recursiva(n -1)

mi_recursiva(5)