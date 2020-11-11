#Para trabajar con el cilo for
#se utiliza los rangos
#1 argumento (5) va del 0 al 5
#2 argumentos (2,10) va desde el 2 hasta el 10
#3 argumentos (1, 50, 5) va del 1 hasta el 50 de 5 en 5
#para iterar un ciclo for se usa la palabra reservada |in| 

lista = ["Santi", "Valentina", "Camila", "Sara"]

for elemento in lista:
    print(elemento)

print("----------------")

palabra = "Una Palabra"

for letra in palabra:
    print(letra)


print("----------------")

for nombre in lista:
    for letra in nombre:
        print(letra)

print("----------------")

for nombre in lista:
    if(nombre == 'Camila'):
        break
    print(nombre)

print("----------------")

for nombre in lista:
    if(nombre == 'Santi'):
        continue
    print(nombre)

print("----------------")

for i in range(5):
    print(i)

print("----------------")

for i in range(3, 10):
    print(i)

print("----------------")

for i in range(0,50, 5):
    print(i)
else:
    print("Fin del bucle")
