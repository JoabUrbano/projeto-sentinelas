import numpy as np
import pandas as pd

from Core.ColetaDados.Interfaces.ColetaDadosInterface import ColetaDadosInterface

class AvistagemDeteccaoColetaDados(ColetaDadosInterface):

    def __init__(self, fileName: str, repository):
        self.path = "Dados/" + fileName
        self.repository = repository

    def carregarDados(self) -> None:
        dados = pd.read_csv(
            self.path, sep=",", encoding="utf-8", escapechar="\n"
        )
        self.formatarDados(dados)

    def formatarDados(self, dados: pd.DataFrame) -> None:
        dados["Filhotes"] = dados["Filhotes"].replace("x", 0)
        dados["Observações"] = dados["Observações"].fillna("Nenhuma")
        print(dados)
        self.persistirDados(dados)

    def persistirDados(self, dados: pd.DataFrame) -> None:
        pass
