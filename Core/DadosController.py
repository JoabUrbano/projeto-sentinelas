from Core.main import Main

class DadosController:
    """
    Constrolador que organiza as chamadas de acordo com o tipo da planilha
    """
    def __init__(self):
        """
        Construtor que instância o main
        """
        self.main = Main()
    
    def tratarRequisicao(self, path, opcao) -> str:
        """
        Chama o método correspondente no mais para o tipo da planilha
        """
        if opcao == "Avistagem e detecção":
            return self.main.carregarAvistagemDeteccao(path)
        else:
            return "Opção inválida!"
