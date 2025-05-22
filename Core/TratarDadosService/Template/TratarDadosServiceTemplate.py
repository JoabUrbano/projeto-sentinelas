import numpy as np
import pandas as pd
import re

class TratarDadosServiceTemplate():
    def __init__(self, path: str, repository):
        """
        Método construtor

        :param path: Caminho para o arquivo a ser lido
        :type path: str
        :param repository: Instância de RepositoryTemplate
        :type repository: RepositoryTemplate
        """
        self.path = path
        self.repository = repository
    
    def carregarDados(self) -> str:
        """
        Método para abrir o arquivo .csv e coloca em um dataframe pandas

        :return: Mensagem de sucesso ou erro.
        :rtype: str

        :raises FileNotFoundError: Se o arquivo não for encontrado no caminho recebido.
        :raises UnicodeDecodeError: Se a codificação do arquivo for incompatível com 'utf-8'.
        :raises pandas.errors.ParserError: Se o conteúdo do CSV estiver mal formado.
        :raises OSError: Em caso de problemas ao acessar o arquivo.
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
        Método a ser sobrescrito que trata as colunas com dados faltante,
        tentando inserir dados neutros

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """

        return self.formatarDados(dados)

    def formatarDados(self, dados: pd.DataFrame) -> str:
        """
        Método a ser sobrescrito que trata e formata os dados

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.limparDados(dados)
    
    def limparDados(self, dados: pd.DataFrame) -> str:
        """
        Método a ser sobrescrito que remove as colunas que não são necessarias

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.persistirDados(dados)


    def persistirDados(self, dados: pd.DataFrame) -> str:
        """
        Método que chama o repository para persistir os dados do dataframe

        :param dados: dataframe pandas que já foi tratado no método de formatarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.repository.inserirDados(dados)
