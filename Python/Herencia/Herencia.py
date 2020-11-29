

class Animal:

    __tipo_animal = str
    __onomatopeya = str

    def __init__(self, tipo_animal, onomatopeya):
            self.__tipo_animal = tipo_animal
            self.__onomatopeya = onomatopeya

    def comer(self):
        print("El animal esta comiendo")

    def correr(self):
        print("El animal esta corriendo")

    def dormir(self):
        print("El animal esta durmiendo")

    def __str__(self):
        return f"Tipo Animal: {self.__tipo_animal}\nOnomatopeya: {self.__onomatopeya}"

class Gato(Animal):

    __nombre = str
    __raza = str
    __color = str

    def __init__(self, nombre, raza, color, tipo_animal, onomatopeya):
        Animal.__init__(self, tipo_animal, onomatopeya)
#       super(Animal).__init__(self, tipo_animal, onomatopeya)
        self.__nombre = nombre
        self.__raza = raza
        self.__color = color

    def comer(self):
        print(f"{self.__nombre} esta comiendo")

    def correr(self):
        print(f"{self.__nombre} esta corriendo")

    def dormir(self):
        print(f"{self.__nombre} esta durmiendo")

    def __str__(self):
        return "----------------\n" + Animal.__str__(self) + f"\nNombre: {self.__nombre}\nRaza: {self.__raza}\nColor: {self.__color}\n" + "----------------\n"

class Perro(Animal):

    __nombre = str
    __raza = str
    __color = str

    def __init__(self, nombre, raza, color, tipo_animal, onomatopeya):
#        Animal.__init__(self, tipo_animal, onomatopeya)
        super().__init__(tipo_animal, onomatopeya)
        self.__nombre = nombre
        self.__raza = raza
        self.__color = color

    def comer(self):
        print(f"{self.__nombre} esta comiendo")


    def correr(self):
        print(f"{self.__nombre} esta corriendo")

    def dormir(self):
        print(f"{self.__nombre} esta durmiendo")

    def __str__(self):
        return  "----------------\n" + Animal.__str__(self) + f"\nNombre: {self.__nombre}\nRaza: {self.__raza}\nColor: {self.__color}\n" + "----------------\n"


cat1 = Gato("Bubi", "Ahí", "Blanco", "Gato", "Miau")
#cat1.dormir()

dog1 = Perro("Bolt", "Pincher", "Blanco", "Perro", "Gau")
#dog1.correr()






