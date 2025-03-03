import numpy as np
import pandas as pd

from Core.Repositorys.Template.RepositoryTemplate import RepositoryTemplate

class AvistagemDeteccaoRepository(RepositoryTemplate):

    def inserirDados(self, dados: pd.DataFrame) -> None:
        sql = """
            INSERT INTO tb_avistagem_deteccao 
            (expedicao, numero, navio, data, registro, especie, nome_comum, latitude, longitude, filhotes, observacoes, tamanho_grupo_minimo, tamanho_grupo_maximo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.persistirDados(dados, sql)
    
