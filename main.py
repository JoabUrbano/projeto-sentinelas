from Core.ColetaDados.Implements.AvistagemDeteccaoColetaDados import AvistagemDeteccaoColetaDados
from Core.Repositorys.Implements.AvistagemDeteccaoRepository import AvistagemDeteccaoRepository

avistagemDeteccaoRepository = AvistagemDeteccaoRepository()
avistagemDeteccaoColetarDados = AvistagemDeteccaoColetaDados("Avistagens e detecções_Sentinelas_2023.xlsx - Detcções visuais e acústicas.csv",
                                    avistagemDeteccaoRepository)

avistagemDeteccaoColetarDados.carregarDados()
