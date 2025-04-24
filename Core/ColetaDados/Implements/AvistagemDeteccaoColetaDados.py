import numpy as np
import pandas as pd

from Core.ColetaDados.Interfaces.ColetaDadosInterface import ColetaDadosInterface

class AvistagemDeteccaoColetaDados(ColetaDadosInterface):

    def __init__(self, path: str, repository):
        """
        Método construtor

        :param path: Caminho para o arquivo a ser lido
        :type path: str
        :param repository: Instância de RepositoryTemplate
        :type repository: RepositoryTemplate
        """
        self.path = path
        self.repository = repository

    def carregarDados(self) -> str:
        """
        Método para abrir o arquivo .csv e coloca em um dataframe pandas

        :return: Mensagem de sucesso ou erro.
        :rtype: str

        :raises FileNotFoundError: Se o arquivo não for encontrado no caminho recebido.
        :raises UnicodeDecodeError: Se a codificação do arquivo for incompatível com 'utf-8'.
        :raises pandas.errors.ParserError: Se o conteúdo do CSV estiver mal formado.
        :raises OSError: Em caso de problemas ao acessar o arquivo.
        """
        try:
            dados = pd.read_csv(
                self.path, sep=",", encoding="utf-8", escapechar="\n"
            )
            return self.formatarDados(dados)
        
        except Exception as e:
           return f"Erro ao abrir o arquivo: {e}."

    def formatarDados(self, dados: pd.DataFrame) -> str:
        """
        Método que trata os dados, realiza a limpeza e formata aos dados

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
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
        
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].replace("", np.nan)
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].fillna(dados["Tamanho de grupo mínimo"])
        
        dados["Tamanho de grupo mínimo"] = pd.to_numeric(dados["Tamanho de grupo mínimo"], errors='coerce')
        dados["Tamanho de grupo máximo"] = pd.to_numeric(dados["Tamanho de grupo máximo"], errors='coerce')

        dados.drop(columns=["Tamanho de grupo"], inplace=True)

        return self.persistirDados(dados)

    def persistirDados(self, dados: pd.DataFrame) -> str:
        """
        Método que chama o repository para persistir os dados do dataframe

        :param dados: dataframe pandas que já foi tratado no método de formatarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.repository.inserirDados(dados)
