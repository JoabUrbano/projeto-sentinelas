from Core.main import Main

class DadosController:
    def __init__(self):
        self.main = Main()
    
    def tratarRequisicao(self, path, opcao) -> str:
        if opcao == "Avistagem e detecção":
            return self.main.carregarAvistagemDeteccao(path)
        else:
            return "Opção inválida!"
