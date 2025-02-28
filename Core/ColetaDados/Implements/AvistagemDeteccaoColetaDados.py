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
        dados["Filhotes"] = dados["Filhotes"].astype(str).replace("x", "0")
        dados["Filhotes"] = pd.to_numeric(dados["Filhotes"], errors='coerce').infer_objects(copy=False)

        dados["Observações"] = dados["Observações"].fillna("Nenhuma")
         
        dados["Lat"] = dados["Lat"].astype(str).str.replace(",", ".").astype(float)
        dados["Long"] = dados["Long"].astype(str).str.replace(",", ".").astype(float)
        
        # Converte a coluna para datetime, tratando erros
        dados["Data"] = pd.to_datetime(dados["Data"], format="%m/%d/%Y", errors="coerce")
        dados["Data"] = dados["Data"].dt.strftime("%Y-%m-%d %H:%M:%S")

        self.persistirDados(dados)

    def persistirDados(self, dados: pd.DataFrame) -> None:
        self.repository.inserirDados(dados)
