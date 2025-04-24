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
        Método que trata e formata os dados

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        pass

    @abstractmethod
    def tratarDadosfaltantes(self) -> str:
        """
        Método que trata as colunas com dados faltante, tentando inserir dados neutros

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        pass

    @abstractmethod
    def limparDados(self) -> str:
        """
        Método que remove as colunas que não são necessarias

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
