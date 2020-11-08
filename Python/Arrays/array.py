
lista = [1,2,3,4,5]
lista2 = lista.copy()

print("Lista ")
lista.append("Buen día")
print(lista)
print("Lista copiada")
print(lista2)

print(lista.count(1))
print(lista2.count(3))

print("-----------------------")


elmentsList1 = len(lista)
elementsList2 = len(lista2)
print(len(lista))
print(elementsList2)
print("-------")
print(len("Hola"))

print("----------")

print(lista[0])

print("Usando Método pop")
print(lista)
print(lista.pop())
print(lista)


print("Usando método pop con indice")
print(lista)
print(lista.pop(2))#Regresa el indice 2 y lo elimina
print(lista)

lista.append("Hola")

print("Utilizando el método remove")
#Este método elimina el VALOR que coincida
print(lista)
lista.remove(2) #Elimina el número 2
print(lista)
lista.remove("Hola") #Elimina el elemento "Hola"
print(lista)


print("Nueva lista")

print()
print("Usando REVERSE")
print()
array = [1,2,3,4,5,6,7,8,9,10]
print("Normal = ", array)
array.reverse()
print("reverse() = ", array)
print()
arrayLetras = ['a', 'b', 'c', 'd', 'e']
print("Normal = ", arrayLetras)
arrayLetras.reverse()
print("reverse() = ", arrayLetras)


print()
print("Usando SORT")
print()
#Sort ordena de menor a mayor
arrayR = [10,9,8,7,6,5,4,3,2,1]
print("Normal = ", arrayR)
arrayR.sort()
print("sort() = ", arrayR)
print()
arrayLetrasR = ['e', 'd', 'c', 'b', 'a']
print("Normal = ", arrayLetrasR)
arrayLetrasR.sort()
print("sort() = ", arrayLetrasR)




#lista.clear()