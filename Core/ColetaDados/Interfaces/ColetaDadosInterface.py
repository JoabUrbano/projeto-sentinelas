from abc import ABC, abstractmethod

class ColetaDadosInterface:

    @abstractmethod
    def carregarDados(self) -> str:
        """
        Método para abrir o arquivo

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        pass
    
    @abstractmethod
    def formatarDados(self) -> str:
        """
        Método que trata os dados, realiza a limpeza e formata aos dados

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        pass
    
    @abstractmethod
    def persistirDados(self) -> str:
        """
        Método que chama o repository para persistir os dados do dataframe

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        pass
