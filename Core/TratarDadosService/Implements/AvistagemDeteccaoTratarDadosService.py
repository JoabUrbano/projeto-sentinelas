import numpy as np
import pandas as pd

from Core.TratarDadosService.Template.TratarDadosServiceTemplate import TratarDadosServiceTemplate

class AvistagemDeteccaoTratarDadosService(TratarDadosServiceTemplate):
    """
    Implementação do template de tratamento de dados para especializar a classe para a
    tabela do tipo avistagem e detecção
    """

    def converterCoordenada(self, cord):
        """
        Realiza a conversão de coordenadas MD para decimais

        Args:
            cord str: Valor da coordenada MD

        Returns:
            grausConvertido float: graus convertidos
        """
        try:
            grausConvertido = float(cord)
            return grausConvertido
        
        except (ValueError, TypeError):
            if not isinstance(cord, str) or len(cord) < 4 or cord == "":
                return np.nan
            
            try:
                indice = cord[0]
                graus = cord[1:].split(":")
                if len(graus) != 2:
                    return np.nan

                grausConvertido = float(graus[0]) + float(graus[1])/60
                if indice == "S" or indice == "W":
                    grausConvertido = grausConvertido * -1
                return grausConvertido
            except: return np.nan
    
    def tratarPontoDuploCoordenada(self, cord):
        """
        Recebe os valores das cordenadas e trata os valores com mais de um "." 
        que dão erro na conversão para float

        Args:
            cord str: Valor da coordenada

        Returns:
            novaCord str: coordenada tratada
        """
        listValues = cord.split(".")
        if len(listValues) < 2:
            novaCord = listValues[0]
            return novaCord
        novaCord = listValues[0] + "." + listValues[1]
        return novaCord

    def tratarDadosfaltantes(self, dados: pd.DataFrame) -> str:
        """
        Trata as colunas com dados faltante, preenchendo as com um valores que
        alertem sobre a ausência de informação

        Args:
            dados (pd.DataFrame): dataframe de avistagem e detecção

        Returns:
            str: Mensagem de sucesso ou erro
        """
        dados["Observações"] = dados["Observações"].fillna("Nenhuma")
        dados["Tipo de som"] = dados["Tipo de som"].fillna("Não registrado")
        dados["Nome comum"] = dados["Nome comum"].fillna("Não identificado")

        return self.formatarDados(dados)

    def formatarDados(self, dados: pd.DataFrame) -> str:
        """
        Método que trata e formata os dados

        Args:
            dados (pd.DataFrame): dataframe com valores vazios tratados.

        Returns:
            str: Mensagem de sucesso ou erro
        """
        dados["Filhotes"] = pd.to_numeric(dados["Filhotes"], errors='coerce').infer_objects(copy=False)
         
        # Converte a coluna para datetime, tratando erros
        dados["Hora"] = dados["Hora"].fillna("00:00:00")

        # Garante que a hora tenha formato válido (ex: 14:30 -> 14:30:00)
        dados["Hora"] = dados["Hora"].astype(str).str.strip()
        dados["Hora"] = dados["Hora"].apply(lambda x: x if len(x.split(":")) == 3 else x + ":00" if len(x.split(":")) == 2 else "00:00:00")

        # Concatena data e hora
        dados["Data (d/m/a)"] = dados["Data (d/m/a)"].astype(str).str.strip() + " " + dados["Hora"]

        # Converte tudo para datetime
        dados["Data (d/m/a)"] = pd.to_datetime(dados["Data (d/m/a)"], format="%d/%m/%Y %H:%M:%S", errors="coerce")
        dados["Data (d/m/a)"] = dados["Data (d/m/a)"].dt.strftime("%Y-%m-%d %H:%M:%S")

        # d+ para pegar obrigatoriamente e os s* a* para capturar espaços e string
        dados["Tamanho de grupo"] = dados["Tamanho de grupo"].astype(str).str.lower()
        dados[["Tamanho de grupo mínimo", "Tamanho de grupo máximo"]] = dados["Tamanho de grupo"].str.extract(r'^\s*(\d+)\s*(?:a\s*(\d+))?\s*$')
        
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].replace("", np.nan)
        dados["Tamanho de grupo máximo"] = dados["Tamanho de grupo máximo"].fillna(dados["Tamanho de grupo mínimo"])
        
        dados["Tamanho de grupo mínimo"] = pd.to_numeric(dados["Tamanho de grupo mínimo"], errors='coerce')
        dados["Tamanho de grupo máximo"] = pd.to_numeric(dados["Tamanho de grupo máximo"], errors='coerce')

        # *** Tratar Latitude e Longitude
        dados["Lat (MD) (navio)"] = dados["Lat (MD) (navio)"].astype(str).str.replace(",", ".")
        dados["Long (MD) (navio)"] = dados["Long (MD) (navio)"].astype(str).str.replace(",", ".")
        
        dados["Lat (MD) (navio)"] = dados["Lat (MD) (navio)"].astype(str).str.replace("°", ":")
        dados["Long (MD) (navio)"] = dados["Long (MD) (navio)"].astype(str).str.replace("°", ":")

        dados["Lat (MD) (navio)"] = dados["Lat (MD) (navio)"].apply(self.tratarPontoDuploCoordenada)
        dados["Long (MD) (navio)"] = dados["Long (MD) (navio)"].apply(self.tratarPontoDuploCoordenada)

        dados["Lat (MD) (navio)"] = dados["Lat (MD) (navio)"].apply(self.converterCoordenada)
        dados["Long (MD) (navio)"] = dados["Long (MD) (navio)"].apply(self.converterCoordenada)

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].fillna(dados["Lat (MD) (navio)"])
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].fillna(dados["Long (MD) (navio)"])

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].astype(str).str.replace(",", ".")
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].astype(str).str.replace(",", ".")

        dados['Lat (GD) (avistagem)'] = dados['Lat (GD) (avistagem)'].apply(self.tratarPontoDuploCoordenada)
        dados['Long (GD) (avistagem)'] = dados['Long (GD) (avistagem)'].apply(self.tratarPontoDuploCoordenada)

        dados["Lat (GD) (avistagem)"] = dados["Lat (GD) (avistagem)"].astype(float).round(4)
        dados["Long (GD) (avistagem)"] = dados["Long (GD) (avistagem)"].astype(float).round(4)
        
        return self.limparDados(dados)
    
    def limparDados(self, dados: pd.DataFrame) -> str:
        """
        Remove as colunas que não são necessarias e as linhas com valores nulos

        Args:
            dados (pd.DataFrame): dataframe com data e coordenadas formatadas

        Returns:
            str: Mensagem de sucesso ou erro
        """
        colunas_obrigatorias = [
            "Expedição", "Pernada", "Navio", "Data (d/m/a)", "Registro",
            "Tipo de som", "Espécie", "Nome comum", "Lat (MD) (navio)",
            "Long (MD) (navio)", "Tamanho de grupo mínimo", "Tamanho de grupo máximo",
            "Filhotes", "Observações"
        ]
        dados = dados.dropna(subset=colunas_obrigatorias)

        dados = dados[dados["Filhotes"] != "sim"]

        colunasDrop = [
            "Número", "Tamanho de grupo", "Lat (MD) (navio)", "Long (MD) (navio)",
            "Hora", "Lat (GMS) (avistagem)", "Long (GMS) (avistagem)", "Lat (GMS)",
            "Long (GMS)", "Distancia da costa (km)", "Unnamed: 22"
        ]

        dados.drop(columns=colunasDrop, inplace=True)

        return self.persistirDados(dados)
