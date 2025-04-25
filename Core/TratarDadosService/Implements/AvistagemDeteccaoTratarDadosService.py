import numpy as np
import pandas as pd
import re

from Core.TratarDadosService.Interfaces.TratarDadosServiceInterface import TratarDadosServiceInterface

class AvistagemDeteccaoTratarDadosService(TratarDadosServiceInterface):

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

    def converterCoordenada(self, valor):
        """
        Método que faz a conversão de coordenadas MD para decimais

        :param valor: coordenada de latitute ou longitude em formato MD
        :type valor: str

        :return: grausConvertido 
        :rtype: str

        """
        try:
            return float(valor)
        
        except (ValueError, TypeError):
            if not isinstance(valor, str) or len(valor) < 4 or valor == "":
                return np.nan
            
            try:
                indice = valor[0]
                graus = valor[1:].split(":")
                if len(graus) != 2:
                    return np.nan

                grausConvertido = float(graus[0]) + float(graus[1])/60
                if indice == "S" or indice == "W":
                    grausConvertido = grausConvertido * -1
                return str(grausConvertido)
            except: return np.nan
    
    def tratarPontoDuploCoordenada(self, valor):
        """
        Método que recebe os valores das cordenadas e trata os valores com mais de um "." 
        para a conversão para float

        :param valor: coordenada de latitute ou longitude
        :type valor: str

        :return: listaValores[0] | novoValor 
        :rtype: str | str

        """
        listaValores = valor.split(".")
        if len(listaValores) < 2:
            return listaValores[0]
        novoValor = listaValores[0] + "." + listaValores[1]
        return novoValor
    
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
            return self.tratarDadosfaltantes(dados)
        
        except Exception as e:
           return f"Erro ao abrir o arquivo: {e}."

    def tratarDadosfaltantes(self, dados: pd.DataFrame) -> str:
        """
        Método que trata as colunas com dados faltante, tentando inserir dados neutros

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        dados["Observações"] = dados["Observações"].fillna("Nenhuma")
        dados["Tipo de som"] = dados["Tipo de som"].fillna("Não registrado")
        dados["Nome comum"] = dados["Nome comum"].fillna("Não identificado")
        dados["Filhotes"] = dados["Filhotes"].fillna("0")

        return self.formatarDados(dados)

    def formatarDados(self, dados: pd.DataFrame) -> str:
        """
        Método que trata e formata os dados

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        dados["Filhotes"] = dados["Filhotes"].astype(str).replace("x", "0")
        dados["Filhotes"] = pd.to_numeric(dados["Filhotes"], errors='coerce').infer_objects(copy=False)
         
        # Converte a coluna para datetime, tratando erros
        dados["Data (d/m/a)"] = pd.to_datetime(dados["Data (d/m/a)"], format="%d/%m/%Y", errors="coerce")
        dados["Data (d/m/a)"] = dados["Data (d/m/a)"].dt.strftime("%Y-%m-%d %H:%M:%S")
       
        # d+ para pegar obrigatoriamente e os s* a* para capturar espaços e string
        dados["Tamanho de grupo"] = dados["Tamanho de grupo"].astype(str).str.lower()
        dados[["Tamanho de grupo mínimo", "Tamanho de grupo máximo"]] = dados["Tamanho de grupo"].str.extract(r'^\s*(\d+)\s*(?:a\s*(\d+))?\s*$')
        
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].replace("", np.nan)
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].fillna(dados["Tamanho de grupo mínimo"])
        
        dados["Tamanho de grupo mínimo"] = pd.to_numeric(dados["Tamanho de grupo mínimo"], errors='coerce')
        dados["Tamanho de grupo máximo"] = pd.to_numeric(dados["Tamanho de grupo máximo"], errors='coerce')

        # *** Tratar Latitude e Longitude
        dados["Lat (MD) (navio)"] = dados["Lat (MD) (navio)"].apply(self.converterCoordenada)
        dados["Long (MD) (navio)"] = dados["Long (MD) (navio)"].apply(self.converterCoordenada)

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].fillna(dados["Lat (MD) (navio)"])
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].fillna(dados["Long (MD) (navio)"])

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].astype(str).str.replace(",", ".")
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].astype(str).str.replace(",", ".")

        dados['Lat (GD) (avistagem)'] = dados['Lat (GD) (avistagem)'].apply(self.tratarPontoDuploCoordenada)
        dados['Long (GD) (avistagem)'] = dados['Long (GD) (avistagem)'].apply(self.tratarPontoDuploCoordenada)

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].astype(float).round(3)
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].astype(float).round(3)
        
        return self.limparDados(dados)
    
    def limparDados(self, dados: pd.DataFrame) -> str:
        """
        Método que remove as colunas que não são necessarias

        :param dados: dataframe pandas que foi criado no método carregarDados
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        dados = dados.dropna(subset=["Expedição"])
        dados = dados.dropna(subset=["Pernada"])
        dados = dados.dropna(subset=["Navio"])
        dados = dados.dropna(subset=["Data (d/m/a)"])
        dados = dados.dropna(subset=["Registro"])
        dados = dados.dropna(subset=["Tipo de som"])
        dados = dados.dropna(subset=["Espécie"])
        dados = dados.dropna(subset=["Nome comum"])
        dados = dados.dropna(subset=["Lat (MD) (navio)"])
        dados = dados.dropna(subset=["Long (MD) (navio)"])
        dados = dados.dropna(subset=["Tamanho de grupo mínimo"])
        dados = dados.dropna(subset=["Tamanho de grupo máximo"])
        dados = dados.dropna(subset=["Filhotes"])
        dados = dados.dropna(subset=["Observações"])
        dados = dados[dados["Filhotes"] != "sim"]

        dados.drop(columns=["Número"], inplace=True)
        dados.drop(columns=["Tamanho de grupo"], inplace=True)
        dados.drop(columns=["Lat (MD) (navio)"], inplace=True)
        dados.drop(columns=["Long (MD) (navio)"], inplace=True)
        dados.drop(columns=["Hora"], inplace=True)
        dados.drop(columns=["Lat (GMS) (avistagem)"], inplace=True)
        dados.drop(columns=["Long (GMS) (avistagem)"], inplace=True)
        dados.drop(columns=["Lat (GMS)"], inplace=True)
        dados.drop(columns=["Long (GMS)"], inplace=True)
        dados.drop(columns=["Distancia da costa (km)"], inplace=True)
        dados.drop(columns=["Unnamed: 22"], inplace=True)

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
