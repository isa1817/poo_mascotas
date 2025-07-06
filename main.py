# Clase base Animal: demuestra herencia, encapsulación simple y métodos comunes
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad      # Atributo protegido

    def hacer_sonido(self):   # Método que será sobrescrito (polimorfismo)
        return "Sonido genérico"

    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

# Clase derivada Perro: hereda de Animal y añade encapsulación con atributo privado
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)   # Llama al constructor de la clase base
        self.__raza = raza               # Atributo privado (encapsulación fuerte)

    def hacer_sonido(self):  # Sobrescribe el método: ejemplo de polimorfismo
        return "Guau guau"

    def descripcion(self):   # Sobrescribe descripción y usa super()
        return f"{super().descripcion()}, Raza: {self.__raza}"

# Clase derivada Gato: también sobrescribe el método hacer_sonido
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

# Función principal: instancia objetos y demuestra polimorfismo
def main():
    perro1 = Perro("Max", 4, "Labrador")
    gato1 = Gato("Michi", 3)

    print(perro1.descripcion())
    print(gato1.descripcion())

    animales = [perro1, gato1]
    for animal in animales:
        # Polimorfismo: cada animal responde con su propio sonido
        print(f"{animal._nombre} dice: {animal.hacer_sonido()}")

if __name__ == "__main__":
    main()
