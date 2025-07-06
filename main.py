class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def hacer_sonido(self):
        return "Sonido genérico"

    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza

    def hacer_sonido(self):
        return "Guau guau"

    def descripcion(self):
        return f"{super().descripcion()}, Raza: {self.__raza}"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

def main():
    perro1 = Perro("Max", 4, "Labrador")
    gato1 = Gato("Michi", 3)

    print(perro1.descripcion())
    print(gato1.descripcion())

    animales = [perro1, gato1]
    for animal in animales:
        print(f"{animal._nombre} dice: {animal.hacer_sonido()}")

if __name__ == "__main__":
    main()
