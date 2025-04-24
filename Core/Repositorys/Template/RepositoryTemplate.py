import pymysql
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

class RepositoryTemplate:

    def __init__(self):
        """
        Método construtor que pega as variaveis de ambiente com as informações do banco
        """
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def inserirDados(self, dados: pd.DataFrame) -> str:
        """
        Método a ser sobrescrita com os parametros do dataframe para inserir no banco

        :param dados: dataframe enviado epla camada de serviço
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        sql = ""
        return self.persistirDados(dados, sql)
    
    def persistirDados(self, dados, sql) -> str:
        """
        Método para persistir os dados no banco

        :param dados: dataframe enviado epla camada de serviço
        :type dados: pd.DataFrame
        :param sql: Comando SQL para inserir os dados
        :type sql: str

        :return: Mensagem de sucesso ou erro.
        :rtype: str

        :raises AttributeError: Se o objeto `dados` não for um DataFrame válido.
        :raises ValueError: Se houver problemas na conversão dos dados para tuplas.
        :raises pymysql.err.OperationalError: Se houver erro na conexão com o banco de dados.
        :raises pymysql.err.ProgrammingError: Se o comando SQL estiver incorreto.
        :raises pymysql.err.IntegrityError: Se houver violação de integridade no banco.
        :raises pymysql.MySQLError: Para quaisquer outros erros relacionados ao MySQL.
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
