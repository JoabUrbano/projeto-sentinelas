from Core.main import Main

class DadosController:
    def __init__(self):
        self.main = Main()
    
    def tratarRequisicao(self, path, opcao):
        self.main.carregarAvistagemDeteccao()
