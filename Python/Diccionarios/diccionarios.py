diccionario = { 
    "nombre" : "Un nombre",
    "tipo" : "Persona",
    "edad" : 20
}

#print(diccionario["edad"])
#print(diccionario.get('nombre'))

diccionario["nombre"] = "Santi"

print(diccionario["nombre"])

diccionario["genero"] = "Masculino"

diccionario["prueba"] = "ultimo insertado"
print(diccionario)
diccionario.popitem()
print(diccionario)

print()

print("Copia")
diccionarioCopia = dict(diccionario)
print(diccionarioCopia)
print("---")


diccionario.clear()
print(diccionario)


print("-------------------------------")
print("--------Diccionarios Anidados--------")

animales = {
    "Lazy" : {
        "nombre" : "Lazy",
        "raza" : "no se",
        "edad": 3
    },

    "Chester" : {
        "nombre": "Chester",
        "raza": "pincher",
        "edad": 8
    },

    "Fluffy" : {
        "nombre": "Fluffy",
        "raza": "Gato",
        "edad": 1
    }

}

print(animales["Lazy"]["nombre"])

lazy = {
    "nombre" : "lazy",
    "raza" : "no se",
    "edad" : 3
}

chester = {
    "nombre" : "Chester",
    "raza" : "pincher",
    "edad" : 3
}

fluffy = { 
    "nombre" : "Fluffy",
    "raza" : "Gato",
    "edad" : 1
}

animales2 = {
    "lazy" : lazy,
    "chester" :chester,
    "flufy" : fluffy
}

print(animales2)



prueba = dict(nombre = "Lazy", edad = 3)

print(prueba)