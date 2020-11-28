"""
def generador(limite):
    n = 1
    while n <= limite:
        yield n * 2
        n+= 1


resultados = generador(20)

print(next(resultados))
print("Codigo.......")
print("Codigo.......")
print("Codigo.......")
print("Codigo.......")
print("Codigo.......")
print(next(resultados))
"""

def funcion(*elementos):
    for i in (elementos):
        return i


print(funcion(1,2,3,4,5))

print("------------")


def generador(*elementos):
    for elemento in elementos:
        yield elemento


iterable = generador("Valentina", 1,2,4,5,8.212, "Sara Orrego")


print(next(iterable))
print("muchas lineas de código")
print("muchas lineas de código")
print("muchas lineas de código")
print("muchas lineas de código")
print("muchas lineas de código")
print("muchas lineas de código")
print(next(iterable))
print("muchas lineas de código")
print(next(iterable))
print(next(iterable))

print("------------------")


def generadorF(*nombres):
    for nombre in nombres:
        yield nombre

nombres = generadorF("Valentina", "Sara", "Camila", "Alejandra")

print("----------------")


def generador2(*numeros):
    for i in numeros:
        yield i , True


resultados = generador2(1,2,3,4,5)

print(next(resultados))
print("Código")
print(next(resultados))
print(next(resultados))




def evaluarEdad(edad):
    
    if edad <= 0 or edad >= 100:
        raise ValueError("La edad no es valida")
    if edad >0 and edad <= 18:
        return "Puede entrar"
    
print(evaluarEdad(int(0))) 






