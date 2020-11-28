def sumar(n1, n2):
    return n1 + n2

lambdaSumar = lambda n1, n2 : n1 + n2
# variable = lambda parametros : regreso 
# (El return es implicito)
# devuelven un calculo no permite
# condicionales ni bucles 
# son funciones de solo una linea

print(lambdaSumar(2, 3))


alcubo = lambda x : x ** 3
alcubo2 = lambda x : pow(x,3)

print(alcubo(2))

prueba = lambda : print("Hola")
prueba()


