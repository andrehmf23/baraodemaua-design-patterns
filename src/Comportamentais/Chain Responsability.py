from abc import abstractmethod, ABC


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request: str) -> str:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return ''


class HandlerConcretoA(AbstractHandler):
    def handle(self, request: str) -> str:
        if request == "A":
            return f"HandlerConcretoA lidou com {request}"
        else:
            return super().handle(request)


class HandlerConcretoB(AbstractHandler):
    def handle(self, request: str) -> str:
        if request == "B":
            return f"HandlerConcretoB lidou com {request}"
        else:
            return super().handle(request)


# Uso
handler_a = HandlerConcretoA()
handler_b = HandlerConcretoB()

handler_a.set_next(handler_b)

print(handler_a.handle("A"))  # HandlerConcretoA lidou com A
print(handler_a.handle("B"))  # HandlerConcretoB lidou com B
