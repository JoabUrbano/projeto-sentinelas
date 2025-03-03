import pymysql
import numpy as np
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

    def inserirDados(self, dados: pd.DataFrame) -> None:
        sql = ""
        self.persistirDados(dados, sql)
    
    def persistirDados(self, dados, sql):
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
                print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir no banco: {e}")

