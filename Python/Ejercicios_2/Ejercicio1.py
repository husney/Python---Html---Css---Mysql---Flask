
#Multiplicación
def multiplicacion(n1, n2):
    r = 0
    for x in range(n2):
       r += n1
    return r


#print(multiplicacion(5,5))

#nombre = input("Por favor ingrese su nombre: ")
#apellido = input("Por favor ingrese su apellido: ")

#nombres = nombre + " "+ apellido

#for x in range(len(nombres) -1, -1, -1):
#    print(nombres[x])

#print(nombres[::-1])


lista = [2,3,1541,2,13,1,32,54,12,31,23,5,1231,1,4,12,3]


for x in range(len(lista)):
    for y in range(len(lista) -1):
        if lista[x] < lista[y]:
            temp = lista[x]
            lista[x] = lista[y]
            lista[y] = temp



menor = 1000000

for x in lista:
    if x < menor:
        menor = x

#print(menor)

import math

def volumen(radio):
    return 4/3 * math.pi * radio **3

#print(volumen(6))

#try:
#    edad = int(input("Ingrese su edad: "))
#except:
#    pass

#if edad >= 18:
#    print("Es mayor de edad")
#else:
#    print("No es mayor de edad")


#numero = int(input("Por favor ingrese un número: "))

#if numero % 2 == 0:
#    print("Es par")
#else:
#   print("Es inpar")


#palabra = "HolA Mundo"
#vocales = 0

#for x in palabra:
#    x = x.lower()
#    if x in ('a', 'e', 'i', 'o', 'u'):
#        vocales += 1

#print(vocales)


#basta = False
#suma = 0

#while not basta:
#    try:
#        valor = int(input("Por favor ingrese un número: "))
#        suma += valor
#        print(suma)
#    except:
#        print("Solo se admiten valores númericos")



#    opcion = input("Si desea terminar escriba 'Basta': ")
#    if opcion == 'Basta':
#        print("Suma total : ", suma)
#        basta = True

while True:
    opt = int(input("Desea agregar un nombre ? 1 = Si, 2 = No: "))
    if(opt == 1):
        archivo = open("Nombres.txt", "a")
        nombreCompleto = input("Por favor ingrese el nombre completo para agregarlo al archivo: ")
        archivo.write(nombreCompleto + "\n")
        archivo.close()
    else:
        break









