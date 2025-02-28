from abc import ABC, abstractmethod

class RepositoryInterface:

    @abstractmethod
    def inserirDados(self) -> None:
        pass
