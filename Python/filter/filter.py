
#La función filter regresa otra función filtrada
#filter(Función, Lista)

lista = [1,2,3,4,5,6,7,8,9,10]

def pares(n):
    if n % 2 == 0:
        return True

resultado = filter(pares, lista)
print(resultado)
   

pares = list(filter(lambda par: par % 2 == 0, lista))
print(pares)





#listaR = filter(lambda x : x % 2 == 0, lista)

#for valor in lista:
#    print(valor)


#x = filter(lambda x : x > 3 and x < 8, lista)

#for valor in x:
    #print(valor)

class Empleado:
    __nombre = str
    __salario = int

    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    
    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def __str__(self):
        return "Nombre : " + self.__nombre + " Salario: " + str(self.__salario)


listaEmpleados = [
Empleado("Valentina", 1000000),
Empleado("Sara", 1500000),
Empleado("Alejandra", 2000000),
Empleado("Camila", 4000000)
]

salariosEmpleados = list(filter(lambda emp: emp.getSalario() > 1500000, listaEmpleados))
print(salariosEmpleados)

for empleado in salariosEmpleados:
    print(empleado)
       