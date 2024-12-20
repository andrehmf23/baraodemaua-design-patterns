class Adaptado:
    def metodo_especifico(self) -> str:
        return "Específico"


class Alvo:
    def metodo_requerido(self) -> str:
        return "Alvo padrão"


# Adaptador
class Adaptador(Alvo):
    def __init__(self, adaptado: Adaptado):
        self._adaptado = adaptado

    def metodo_requerido(self) -> str:
        return f"Adaptador: {self._adaptado.metodo_especifico()}"


# Uso
adaptado = Adaptado()
adaptador = Adaptador(adaptado)
print(adaptador.metodo_requerido())
