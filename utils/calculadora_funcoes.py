from typing import Literal

def calcular_valor(qtd_pessoas: int, gasto_mensal: float, estado: Literal['norte', 'nordeste', 'sudeste', 'sul', 'centro-oeste']):
    taxas_estado = {"norte":1.92, "nordeste":2.13, "sudeste":3.17, "sul":3.80, "centro-oeste":4.17}

    resultados = {
        'gasto_pessoa': (gasto_mensal*1000)/(qtd_pessoas*30),
        'gasto_agua': gasto_mensal * taxas_estado[estado]
    }

    return resultados