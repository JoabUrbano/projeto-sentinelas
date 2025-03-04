from Core.Repositorys.Template.RepositoryTemplate import RepositoryTemplate

class AvistagemDeteccaoRepository(RepositoryTemplate):

    def inserirDados(self, dados) -> None:
        sql = """
            INSERT INTO tb_avistagem_deteccao 
            (expedicao, numero, navio, data, registro, especie, nome_comum, latitude, longitude, filhotes, observacoes, tamanho_grupo_minimo, tamanho_grupo_maximo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.persistirDados(dados, sql)
