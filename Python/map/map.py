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
Empleado("Valentina", 100),
Empleado("Sara", 150),
Empleado("Alejandra", 300),
Empleado("Camila", 400)
]

def calcularBono(empleado):
    if empleado.getSalario() <250:
        empleado.setSalario(empleado.getSalario() * 1.3)

    return empleado


empleadosBono = map(calcularBono, listaEmpleados)


for empleado in empleadosBono:
    print(empleado)



