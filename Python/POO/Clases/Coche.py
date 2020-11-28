class Rueda():
    marca = str
    pesoKg = float

    def __init__(self, marca, pesoKg):
        self.marca = marca
        self.pesoKg = pesoKg

    def __str__(self):
        return "Rueda"


class Coche():
    __marca = str
    __ruedas = []
    __puertas = int
    __prendido = False

    

    #Constructor
    def __init__(self, marca, puertas):
      self.__marca = marca
      self.__puertas = puertas
      

    def __prender(self):
        return "El auto prendio"

    def prenderAuto(self):
        return self.__prender()
    
    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    def iniciar(self):
        print(self.__marca , "Iniciando")

    def estado(self):
        print("Marca : " + self.__marca + "\n"
             +"Puertas: " + str(self.__puertas) + "\n"   
             +"Prendido: " + str(self.__prendido)
            )
    
   

    
    
"""
prueba = Coche("BMW",4)
prueba.iniciar()

prueba.prender()
print(prueba.Prendido)
"""
"""rueda1 = Rueda("Ferrari", 10.2)
rueda2 = Rueda("Ferrari", 10.2)
rueda3 = Rueda("Ferrari", 15.2)
rueda4 = Rueda("Ferrari", 15.2)

ruedas = [rueda1, rueda2, rueda3, rueda4]
miCoche = Coche("Mercedez", 7)
miCoche.ruedas = ruedas"""




class Vehiculo():

    __ruedas = int
    __encendido = False
    __apagado = True
    __enMovimiento = False
    __aceleracion = 0

    def __init__(self, ruedas, enMovimiento, aceleracion):
        self.__ruedas = ruedas
        self.__enMovimiento = enMovimiento
        self.__aceleracion = aceleracion

    def encender(self):
        if not self.__encendido:
            self.__encendido = True
            print("El Vehiculo está encendido")
        else:
            print("El Vehiculo ya está encendido")

    def apagar(self):
        if not self.__apagado:
            self.__apagado = True
            print("El vehiculo se va a apagar")
        else:
            print("El vehiculo ya está apagado")
 
    def acelerar(self):
        if self.__aceleracion >= 0 and self.__aceleracion <=150:
            self.__aceleracion += 5

    def frenar(self):
        if self.__aceleracion >= 0:
            self.__aceleracion -= 5

    def getAceleracion(self):
        return self.__aceleracion

    def getEstado(self):
        return ("Ruedas: " , self.__ruedas , 
                "Encendido: " ,str(self.__encendido) , 
                "En Movimiento: ", str(self.__enMovimiento) ,"Aceleracion:" , 
                str(self.__aceleracion))


class Moto(Vehiculo): #Heredando de Vehiculo
    __caballito = 0

    def  hacerCaballito(self):
        if self.__caballito == 0:
            self.__caballito = 1
            print("Está moto esta haciendo el caballito")

    def getEstado(self):
        return Vehiculo.getEstado(self) , "Caballito" , self.__caballito
        #Tambien es posible con super(Moto, self).getEstado()

    
class VehiculoElectrico():

    __horas = int
    __totalWH = int
    __carga = int

    def __init__(self, horas, totalWH, carga):
        self.__horas = horas
        self.__totalWH = totalWH
        self.__carga = carga

    def cargar(self): 
        self.__carga += 5

    def getHoras(self):
        return self.__horas
    
    def getTotalWH(self):
        return self.__totalWH


class MotoElectrica(VehiculoElectrico, Vehiculo):
    
    def __init__(self,  horas, totalWH, carga, ruedas, enMovimiento, acelaracion):
        VehiculoElectrico.__init__(self, horas, totalWH, carga)
        Vehiculo.__init__(self, ruedas, enMovimiento, acelaracion)
        


miMoto = Moto(2, False, 0)#Constructor heredado de Vehiculo

miMoto.acelerar()
miMoto.acelerar()
miMoto.acelerar()
miMoto.acelerar()
"""print(miMoto.getAceleracion())
print(miMoto.getEstado())
print("-------------")"""


miMotoElectrica = MotoElectrica(10, 10000, 100, 2, False, 0)
"""print(miMotoElectrica.getEstado())
print(miMotoElectrica.getHoras())
print(miMotoElectrica.getTotalWH())
print("---------------------")
print("---------------------")
print("---------------------")
print("---------------------")"""


#Polimorfismo

class Auto():

    def desplazamiento(self):
        print("Me estoy desplazando en un auto")


class Motocicleta():
    def desplazamiento(self):
        print("Me estoy desplazando en una motocicleta")

class Avion():
    
    def desplazamiento(self):
        print("Me estoy desplazando en un avion")

def desplazar(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Motocicleta()
desplazar(miVehiculo)

"""print("---------------------")
print("---------------------")
print("---------------------")
print("---------------------")"""

"""variable = "Hola soy una variable"
print(variable.center(150))"""

"""print("---------------------")
print("---------------------")
print("---------------------")
print("---------------------")"""

"""var1 = "123"
print(var1.isdigit())"""
