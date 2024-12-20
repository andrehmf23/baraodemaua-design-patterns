from abc import ABC, abstractmethod


# Criar Interface do Handler
class InterfaceHandler(ABC):

    @abstractmethod
    def set_next_handler(self, handler: 'InterfaceHandler' = None):
        pass

    @abstractmethod
    def handle(self, request):
        pass


# Criar Handler Base
class Handler(InterfaceHandler):

    def __init__(self, handler: InterfaceHandler = None):
        self.next_handler: InterfaceHandler = handler

    def set_next_handler(self, handler: InterfaceHandler = None):
        self.next_handler = handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        else:
            return None


# Criar Funcionário - 0~500
class Funcionario(Handler):
    def handle(self, request: float) -> str:
        if 0 < request < 500:
            return f'O orçamento de R${request} foi aprovado pelo {type(self).__name__}'
        elif self.next_handler:
            print(f'O orçamento foi repassado para {type(self.next_handler).__name__}')
            return self.next_handler.handle(request)
        else:
            return f'O orçamento de R${request} foi reprovado pelo {type(self).__name__}'

# Criar Gestor - 500~2000
class Gestor(Handler):
    def handle(self, request: float) -> str:
        if 500 < request < 2000:
            return f'O orçamento de R${request} foi aprovado pelo {type(self).__name__}'
        elif self.next_handler:
            print(f'O orçamento foi repassado para {type(self.next_handler).__name__}')
            return self.next_handler.handle(request)
        else:
            return f'O orçamento de R${request} foi reprovado pelo {type(self).__name__}'

# Criar Gerente - 2000~10000
class Gerente(Handler):
    def handle(self, request: float) -> str:
        if 2000 < request < 10000:
            return f'O orçamento de R${request} foi aprovado pelo {type(self).__name__}'
        elif self.next_handler:
            print(f'O orçamento foi repassado para {type(self.next_handler).__name__}')
            return self.next_handler.handle(request)
        else:
            return f'O orçamento de R${request} foi reprovado pelo {type(self).__name__}'


# Criar Diretor - 10000~20000
class Diretor(Handler):
    def handle(self, request: float) -> str:
        if 10000 < request < 20000:
            return f'O orçamento de R${request} foi aprovado pelo {type(self).__name__}'
        elif self.next_handler:
            print(f'O orçamento foi repassado para {type(self.next_handler).__name__}')
            return self.next_handler.handle(request)
        else:
            return f'O orçamento de R${request} foi reprovado pelo {type(self).__name__}'


if __name__ == '__main__':
    # Criar chain
    chain = Funcionario(Gestor(Gerente(Diretor())))

    while True:
        orcamento = input("\nInsira o orçamento para ser aprovado: ")
        if orcamento.isnumeric():
            orcamento = float(orcamento)
            if orcamento <= 0:
                print(f'Valor inserido inválido!')
            else:
                print(f'Aprovação de orçamento de R${orcamento} foi iniciado pelo {type(chain).__name__}')
                print("Conclusão:", chain.handle(orcamento))
        else:
            print(f'Valor inserido inválido!')
''
