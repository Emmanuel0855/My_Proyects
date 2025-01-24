# Clase base Animal
class Animal:
    def hablar(self):
        pass

# Clase derivada Perro
class Perro(Animal):
    def hablar(self):
        return "Guau"

# Clase derivada Gato
class Gato(Animal):
    def hablar(self):
        return "Miau"

# Función que recibe un objeto de la clase Animal y llama al método hablar
def hacer_hablar(animal: Animal):
    print(animal.hablar())

# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()

# Llamar a la función con ambas instancias
hacer_hablar(perro)  # Debería imprimir "Guau"
hacer_hablar(gato)   # Debería imprimir "Miau"