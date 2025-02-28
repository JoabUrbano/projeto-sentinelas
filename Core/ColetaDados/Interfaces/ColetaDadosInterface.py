from abc import ABC, abstractmethod

class ColetaDadosInterface:

    @abstractmethod
    def carregarDados(self) -> None:
        pass
    
    @abstractmethod
    def formatarDados(self) -> None:
        pass
    
    @abstractmethod
    def persistirDados(self) -> None:
        pass
