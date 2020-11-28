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
