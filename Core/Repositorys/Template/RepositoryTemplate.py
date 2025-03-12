import pymysql
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

class RepositoryTemplate:

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def inserirDados(self, dados: pd.DataFrame) -> str:
        sql = ""
        return self.persistirDados(dados, sql)
    
    def persistirDados(self, dados, sql) -> str:
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
