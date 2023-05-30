import json
import os
from flask import Flask, Response

def escolher_perguntas(dificuldade: str, arquivos_estaticos: str) -> dict:
    """
    Com base numa dificuldade, devolve perguntas dela em forma de lista de dicts:
    [{
        '1': 'Qual a resposta?',
        'opcoes:' [
            "Opcoes": {
                "a": "H2O",
                "b": "NaCl",
                "c": "CaO"
            }
        ]
    }]
    """
    if dificuldade not in ('Fácil', 'Médio', 'Difícil'):
        return 'Dificuldade invalida!', 400
    with open(os.path.join(arquivos_estaticos, 'perguntas.json'), "r") as perguntas_json:
        perguntas = json.loads(perguntas_json.read())   

    nivel = perguntas[dificuldade]
    perguntas = []

    for questao in nivel:
        new_dict = {
            questao: nivel[questao]['Pergunta'],
            'Opcoes': nivel[questao]['Opcoes']
        }
        perguntas.append(new_dict)

    return perguntas, 200

def verifica_resposta(dificuldade: str, respostas: dict, arquivos_estaticos: str)-> dict:
    """
    respostas = {
        '1': 'a'
    }
    resultado = {
            '1': {
                'resposta': 'x',
                'correta': 'y'
            }
            ...
            'resultado': {
                'total': y
                'acertos': x,
                'porcentagem': 0
            }
        }
    """
    with open(os.path.join(arquivos_estaticos, 'perguntas.json'), "r") as perguntas_json:
        perguntas = json.loads(perguntas_json.read())
    
    perguntas = perguntas.get(dificuldade, None)
    if perguntas is None:
        return 'Dificuldade invalida!', 400
    

    acertos = 0
    total = len(perguntas.keys())
    result = {}

    for num_resp in perguntas:
        resposta = respostas.get(num_resp, False)
        correta = perguntas[num_resp]['Correta']
        new_resp = {
            'resposta': resposta,
            'correta': correta,
        }
        result.append(new_resp)
        acertos += (resposta == correta)
        
    result['resultado'] = {
            'total': total,
            'acertos': acertos,
        }

    return result