from Core.Repositorys.Template.RepositoryTemplate import RepositoryTemplate

class AvistagemDeteccaoRepository(RepositoryTemplate):
    """
    Implementação do Template do repository, que define a inserção dos dados
    """

    def inserirDados(self, dados) -> str:
        """
        Sobrescrição do método com os parametros do dataframe para inserir no banco

        Args:
            dados (pd.DataFrame): dataframe pronto que será inserido no banco de dados

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        sql = """
            INSERT INTO tb_avistagem_deteccao 
            (expedicao, pernada, navio, data, registro, tipo_som, especie, nome_comum, latitude, longitude, filhotes, observacoes, mes_avistagem, tamanho_grupo_minimo, tamanho_grupo_maximo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        return self.persistirDados(dados, sql)
