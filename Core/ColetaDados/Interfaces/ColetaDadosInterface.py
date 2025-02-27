from abc import ABC, abstractmethod

class ColetaDadosInterface:

    @abstractmethod
    def carregarDados(self) -> None:
        pass

    def formatarDados(self) -> None:
        pass

    def persistirDados(self) -> None:
        pass
