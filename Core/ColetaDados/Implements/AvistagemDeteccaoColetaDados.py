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

        # ----- Tamanho de grupo -----
        dados["Tamanho de grupo"] = dados["Tamanho de grupo"].astype(str).replace("x", "1")
  
        # d+ para pegar obrigatoriamente e os s* a* para capturar espaços e string
        dados[["Tamanho de grupo mínimo", "Tamanho de grupo máximo"]] = dados["Tamanho de grupo"].str.extract(r'(\d+)\s*a*\s*(\d*)')
        
        # Preenche o valor máximo com o mínimo onde o máximo estiver vazio
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].replace("", np.nan)
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].fillna(dados["Tamanho de grupo mínimo"])
        
        dados["Tamanho de grupo mínimo"] = pd.to_numeric(dados["Tamanho de grupo mínimo"], errors='coerce')
        dados["Tamanho de grupo máximo"] = pd.to_numeric(dados["Tamanho de grupo máximo"], errors='coerce')

        dados.drop(columns=["Tamanho de grupo"], inplace=True)

        self.persistirDados(dados)

    def persistirDados(self, dados: pd.DataFrame) -> None:
        self.repository.inserirDados(dados)
