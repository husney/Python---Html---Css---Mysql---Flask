class Usuario:
    def __init__(self, nombre, apellido ):  #self es opcional
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print("Hola soy", self.nombre , self.apellido)

    def saltar(self):
        print("Hola soy " + self.nombre + " y estoy saltando")

    def getNombre(self):
        return self.nombre
    

usuario = Usuario('Valentina', 'Marin')

print(usuario.nombre, usuario.apellido)
usuario.saludar()

print("------------ ")
usuario.saltar()

print("---------")
print(usuario.getNombre())


