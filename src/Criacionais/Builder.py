from abc import ABC, abstractmethod


class Produto:
    def __init__(self):
        self.partes = []

    def adicionar(self, parte: str):
        self.partes.append(parte)

    def listar_partes(self) -> str:
        return ", ".join(self.partes)


# Builder abstrato
class Builder(ABC):
    @abstractmethod
    def produzir_parte_a(self): pass

    @abstractmethod
    def produzir_parte_b(self): pass


# Concreto Builder
class ConcretoBuilder(Builder):
    def __init__(self):
        self.produto = None
        self.reset()

    def reset(self):
        self.produto = Produto()

    def produzir_parte_a(self):
        self.produto.adicionar("Parte A")

    def produzir_parte_b(self):
        self.produto.adicionar("Parte B")

    def obter_produto(self) -> Produto:
        produto = self.produto
        self.reset()
        return produto


# Diretor
class Diretor:
    def __init__(self, builder: Builder):
        self._builder = builder

    def construir_produto_completo(self):
        self._builder.produzir_parte_a()
        self._builder.produzir_parte_b()


# Uso
builder = ConcretoBuilder()
diretor = Diretor(builder)
diretor.construir_produto_completo()

produto = builder.obter_produto()
print(produto.listar_partes())
