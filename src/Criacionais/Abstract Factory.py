from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def ligar_motor(self):
        pass


class Carro(Veiculo):
    def ligar_motor(self):
        print("Ligando o motor a gasolina...")


class Moto(Veiculo):
    def ligar_motor(self):
        print("Ligando o motor a combustão...")
