import numpy as np
import pandas as pd
import re

class TratarDadosServiceTemplate():
    """
    Template do tratamento de dados da camada de serviço
    """
    def __init__(self, path: str, repository):
        """
        Construtor

        Args:
            path str: Caminho para abrir o arquivo csv com os dados
            repository (RepositoryTemplate): Implementação de repository correspondente
        """
        self.path = path
        self.repository = repository
    
    def carregarDados(self) -> str:
        """
        Abre o arquivo .csv como um dataframe pandas

        Returns:
            str: Mensagem de sucesso ou erro

        Errors:
            FileNotFoundError: Se o arquivo não for encontrado no caminho recebido
            UnicodeDecodeError: Se a codificação do arquivo for incompatível com 'utf-8'
            pandas.errors.ParserError: Se o conteúdo do CSV estiver mal formado
            OSError: Em caso de problemas ao acessar o arquivo
        """
        try:
            dados = pd.read_csv(
                self.path, sep=",", encoding="utf-8", escapechar="\n"
            )
            return self.tratarDadosfaltantes(dados)
        
        except Exception as e:
           return f"Erro ao abrir o arquivo: {e}."

    def tratarDadosfaltantes(self, dados: pd.DataFrame) -> str:
        """
        Tratar dados faltantes, pode ser sobrescrito

        Args:
            dados (pd.DataFrame): dataframe com dados de avistagem e detecção

        Returns:
            str: Mensagem de sucesso ou erro
        """

        return self.formatarDados(dados)

    def formatarDados(self, dados: pd.DataFrame) -> str:
        """
        Formata os dados, pode ser sobrescrito

        Args:
            dados (pd.DataFrame): dataframe com valores vazios tratados

        Returns:
            str: Mensagem de sucesso ou erro
        """
        return self.limparDados(dados)
    
    def limparDados(self, dados: pd.DataFrame) -> str:
        """
        Limpeza de dados inválidos, pode ser sobrescrito

        Args:
            dados (pd.DataFrame): dataframe com data e coordenadas formatadas.

        Returns:
            str: Mensagem de sucesso ou erro
        """
        return self.persistirDados(dados)


    def persistirDados(self, dados: pd.DataFrame) -> str:
        """
        Método que chama o repository para persistir os dados do dataframe

        Args:
            dados (pd.DataFrame): dataframe pronto para persistência

        Returns:
            str: Mensagem de sucesso ou erro
        """
        return self.repository.inserirDados(dados)
