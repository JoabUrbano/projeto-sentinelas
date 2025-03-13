from abc import ABC, abstractmethod

class ColetaDadosInterface:

    @abstractmethod
    def carregarDados(self) -> str:
        pass
    
    @abstractmethod
    def formatarDados(self) -> str:
        pass
    
    @abstractmethod
    def persistirDados(self) -> str:
        pass
