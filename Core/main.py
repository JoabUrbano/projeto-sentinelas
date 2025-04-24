from Core.TratarDadosService.Implements.AvistagemDeteccaoTratarDadosService import AvistagemDeteccaoTratarDadosService
from Core.Repositorys.Implements.AvistagemDeteccaoRepository import AvistagemDeteccaoRepository

class Main:
    def carregarAvistagemDeteccao(self, path) -> str:

        avistagemDeteccaoRepository = AvistagemDeteccaoRepository()
        avistagemDeteccaoColetarDados = AvistagemDeteccaoTratarDadosService(
            path, avistagemDeteccaoRepository
        )

        return avistagemDeteccaoColetarDados.carregarDados()
