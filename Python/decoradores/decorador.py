def decorador(funcion_param):
    def funcion_interna(*args ):
        print("Realizando calculo:")
        funcion_param(*args)
        print("Calculo realizado:")
    return funcion_interna


@decorador
def suma(n1, n2):
    print(n1 + n2)


#suma(8,2)


def introductor(function):
    def wrapper(*args, **kwargs):
        print("-------------")
        return function(*args, **kwargs)
    return wrapper


@introductor
def multiplicar(n1, n2):
    return (n1 * n2)


import time

def calcular_tiempo_operacion(nombre):
    def wraper(function):
        def wraper2(*args, **kwargs):
            start = time.time()
            resultado = function(*args, **kwargs)
            print(f"Tiempo total de la {nombre} es : " , int(time.time() - start), "segundos" )
            return resultado
        return wraper2
    return wraper



@calcular_tiempo_operacion
def sumar(self, n1, n2):
    """Esta función realiza una suma"""
    time.sleep(2)
    return n1 + n2

def restar(self, n1, n2):
    '''Esta función realiza una resta'''
    return n1 -n2


import doctest

def areaTriangulo(base, altura):
    """
    Esta función calcula el área de un triángulo dado

    >>> areaTriangulo(3,6)
    1.0
    """
    return (base*altura)/2


doctest.testmod()





