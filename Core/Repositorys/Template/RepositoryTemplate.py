import pymysql
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

class RepositoryTemplate:
    """
    Template do repository para inserir os dados na tabela correspondente
    """

    def __init__(self):
        """
        Construtor que pega as variaveis de ambiente com as informações do banco
        """
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def inserirDados(self, dados: pd.DataFrame) -> str:
        """
        Define o INSERTcomando SQL como vazio para ser sobrescrito

        Args:
            dados (pd.DataFrame): dataframe que será persistido

        Returns:
            str: Mensagem de sucesso ou erro
        """
        sql = ""
        return self.persistirDados(dados, sql)
    
    def persistirDados(self, dados, sql) -> str:
        """
        Persiste os dados no banco

        Args:
            dados (pd.DataFrame): dataframe que será persistido
            sql str: Comando SQL para rodar no banco

        Returns:
            str: Mensagem de sucesso ou erro

        Errors:
            AttributeError: Se o objeto `dados` não for um DataFrame válido.
            ValueError: Se houver problemas na conversão dos dados para tuplas.
            pymysql.err.OperationalError: Se houver erro na conexão com o banco de dados.
            pymysql.err.ProgrammingError: Se o comando SQL estiver incorreto.
            pymysql.err.IntegrityError: Se houver violação de integridade no banco.
            pymysql.MySQLError: Para quaisquer outros erros relacionados ao MySQL.
        """
        valores = dados.to_records(index=False).tolist()
        try:
            with pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(sql, valores)

                connection.commit()
                return "Dados inseridos com sucesso!"
        
        except Exception as e:
           return f"Erro ao inserir no banco: {e}"
