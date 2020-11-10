opcion = 1

while opcion != 0:
    print()
    opcion = input("Por favor ingrese una opción\n1-suma\n2-resta\n3-multiplicación\n4-división\n5-división entera\n6-potenciación\n0-salir\n... :")
    try:
        opcion = int(opcion)
    except:
        print("Error opción no valida")
        continue

    n1 = 0
    n2 = 0
    resultado = 0

    if(opcion != 0):
        boln1 = False

        while not boln1:
            try:
                n1 = int(input("Por favor ingrese el primer valor: "))
                boln1 = True
            except:
                print("Valor no valido por favor ingreselo de nuevo")

        boln2 = False
        while not boln2:
            try:
                n2 = int(input("Por favor ingrese el segundo valor: "))
                boln2 = True
            except:
                print("Valor no valido por favor ingreselo de nuevo")        

    if(opcion == 1):
        resultado = n1 + n2
    elif(opcion == 2):
        resultado = n1 - n2
    elif(opcion == 3):
        resultado = n1 * n2
    elif(opcion == 4):
        try:
            resultado = n1 / n2
        except:
            if(n2 == 0):
                print("------ERROR--------")
                print("Error no se puede dividir por 0")
                print("------ERROR--------")
                continue
    elif(opcion == 5):        
        try:
            resultado = n1 // n2
        except:
            if(n2 == 0):
                print("------ERROR--------")
                print("Error no se puede dividir por 0")
                print("------ERROR--------")
                continue
    elif(opcion == 6):
        resultado = n1 ** n2
    if(resultado != 0):
        print("------------")
        print(resultado)
        print("------------")
    else:
        print("Muchas gracias, que estes bien")
    
    
