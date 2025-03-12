from Core.ColetaDados.Implements.AvistagemDeteccaoColetaDados import AvistagemDeteccaoColetaDados
from Core.Repositorys.Implements.AvistagemDeteccaoRepository import AvistagemDeteccaoRepository

class Main:
    def carregarAvistagemDeteccao(self, path) -> str:

        avistagemDeteccaoRepository = AvistagemDeteccaoRepository()
        avistagemDeteccaoColetarDados = AvistagemDeteccaoColetaDados(
            path, avistagemDeteccaoRepository
        )

        return avistagemDeteccaoColetarDados.carregarDados()
