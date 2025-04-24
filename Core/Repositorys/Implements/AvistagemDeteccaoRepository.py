from Core.Repositorys.Template.RepositoryTemplate import RepositoryTemplate

class AvistagemDeteccaoRepository(RepositoryTemplate):

    def inserirDados(self, dados) -> str:
        """
        Sobrescrição do método com os parametros do dataframe para inserir no banco

        :param dados: dataframe pronto que será inserido no banco de dados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        sql = """
            INSERT INTO tb_avistagem_deteccao 
            (expedicao, numero, navio, data, registro, especie, nome_comum, latitude, longitude, filhotes, observacoes, tamanho_grupo_minimo, tamanho_grupo_maximo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        return self.persistirDados(dados, sql)
