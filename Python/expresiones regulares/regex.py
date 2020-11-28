import re

#cadena = "Estamos en Python aprendiendo Python expreciones regulares Python"
#busqueda = "Python"
#print(len(re.findall(busqueda, cadena)))

#search(busqueda,fuente) = Objeto || None
    #start() inicio de match
    #end() fin del match
#findall(busqueda, fuente) = Lista


codigos = [ "Hola Buen día",
            "Buen día",
            "Hola Buena tarde",
            "Buena tarde",
            "Hola Buena noche",
            "Buena noche"
            ]

for cod in codigos:
    if re.match("Buen", cod):
        print(cod)







