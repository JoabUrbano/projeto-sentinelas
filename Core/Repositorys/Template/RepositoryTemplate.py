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
        Define o comando SQL INSERT como vazio para ser sobrescrito

        Args:
            dados (pd.DataFrame): dataframe que será persistido

        Returns:
            str: Mensagem de sucesso ou erro
        """
        sql = ""
        return self.persistirDados(dados, sql)
    
    def persistirDados(self, dados, sql) -> str:
        """
        Persiste os dados no banco, inserindo em lotes de 300 em 300 para evitar erros
        de mémoria ou disco com grandes inserções

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
        batch_size: int = 300
        try:
            with pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            ) as connection:
                with connection.cursor() as cursor:
                    total_rows = len(dados)
                    for start in range(0, total_rows, batch_size):
                        end = min(start + batch_size, total_rows)
                        batch = dados.iloc[start:end].to_records(index=False).tolist()
                        cursor.executemany(sql, batch)
                        connection.commit()
            return "Todos os dados foram inseridos com sucesso!"
        
        except AttributeError:
            return "O dataframe fornecido não é válido!"

        except ValueError:
            return "Houve um erro na conversão dos dados para tuplas!"
        
        except pymysql.err.OperationalError:
            return "Erro ao tentar conectar com o banco de dados!"
        
        except pymysql.err.ProgrammingError:
            return "Comando SQL inválido!"
        
        except pymysql.err.IntegrityError:
            return "Violação da integridade do banco de dados!"
        
        except pymysql.MySQLError as e:
            return f"Erro no MySQL: {e}!"
    
        except Exception as e:
           return f"Erro ao inserir no banco: {e}"
