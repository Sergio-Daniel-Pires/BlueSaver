import json
import os
from flask import Flask, Response

def escolher_perguntas(dificuldade: str, arquivos_estaticos: str) -> dict:
    """
    Com base numa dificuldade, devolve perguntas dela.
    """
    #print(f"Seu quiz tem dificuldade {dificuldade}")

    with open(os.path.join(arquivos_estaticos, 'perguntas.json'), "r") as perguntas_json:
        perguntas = json.loads(perguntas_json.read())   

    #linhas = []
    nivel=perguntas[dificuldade]
    new_dict = {}

    for idx, questao in enumerate(nivel):
        new_dict.update({f"Pegunta {idx+1}":nivel[questao]['Pergunta']})
        new_dict.update({f"Opcoes {idx+1}": [nivel[questao]['Opcoes']]})

    return new_dict

def verifica_resposta(dificuldade: str, respostas: list, arquivos_estaticos: str)-> dict:
    with open(os.path.join(arquivos_estaticos, 'perguntas.json'), "r") as perguntas_json:
        perguntas = json.loads(perguntas_json.read())
    
    nivel=perguntas[dificuldade]
    new_dict= {f'Suas respostas para o quiz': dificuldade}

    for idx, questao in enumerate(nivel):
        if respostas[idx] == nivel[questao]['Correta']:
            new_dict.update({f"Pergunta {idx+1}) Sua resposta: {respostas[idx]}":" Correta"})
        else:
            new_dict.update({f"Pergunta {idx+1}) Sua resposta: {respostas[idx]}":" Incorreta"})
            new_dict.update({f"Resposta correta questão {idx+1}":nivel[questao]['Correta']})

    return new_dict