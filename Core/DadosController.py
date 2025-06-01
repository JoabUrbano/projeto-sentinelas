from Core.TratarDadosService.Implements.AvistagemDeteccaoTratarDadosService import AvistagemDeteccaoTratarDadosService
from Core.Repositorys.Implements.AvistagemDeteccaoRepository import AvistagemDeteccaoRepository

class DadosController:
    """
    Constrolador que organiza as chamadas de acordo com a opção selecionada
    """
    def tratarRequisicao(self, path, opcao) -> str:
        """
        Instância de service correspondente a opção selecionada e passa o repository
        correspondente ao service como parâmetro
        """
        if opcao == "Avistagem e detecção":
            avistagemDeteccaoRepository = AvistagemDeteccaoRepository()
            avistagemDeteccaoColetarDados = AvistagemDeteccaoTratarDadosService(
                path, avistagemDeteccaoRepository
            )

            return avistagemDeteccaoColetarDados.carregarDados()
        else:
            return "Opção inválida!"
