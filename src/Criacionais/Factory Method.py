from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        return "Au au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


class FabricaDeAnimais:
    def criar_animal(self, tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal inválido")


fabrica = FabricaDeAnimais()
animal1 = fabrica.criar_animal("cachorro")
animal2 = fabrica.criar_animal("gato")

print(animal1.falar())  # Saída: Au au!
print(animal2.falar())  # Saída: Miau!
