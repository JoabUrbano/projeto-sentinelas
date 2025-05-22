from Core.TratarDadosService.Implements.AvistagemDeteccaoTratarDadosService import AvistagemDeteccaoTratarDadosService
from Core.Repositorys.Implements.AvistagemDeteccaoRepository import AvistagemDeteccaoRepository

class Main:
    """
    Classe mais que chama as camadas de service
    """
    def carregarAvistagemDeteccao(self, path) -> str:
        """
        Cria o objeto repository adequando e passa o caminho e parametro
        para a camada de serviço

        Args:
            path str: caminho da planilha

        Returns:
            str: Mensagem de sucesso ou erro
        """

        avistagemDeteccaoRepository = AvistagemDeteccaoRepository()
        avistagemDeteccaoColetarDados = AvistagemDeteccaoTratarDadosService(
            path, avistagemDeteccaoRepository
        )

        return avistagemDeteccaoColetarDados.carregarDados()
