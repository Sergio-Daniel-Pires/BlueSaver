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

    for questao in nivel:
        new_dict+=  nivel[questao]['Pergunta']
        new_dict+= nivel[questao]['Opcoes']

    return new_dict
    """
    return dict(nivel)
    out=""
    for q in nivel: 
        out += f"Pergunta: {nivel[q]['Pergunta']}  a"
        out += "\n"
    """
    """   
    response = make_response({'result': out})
    print(type(response))
    response.headers['Content-Type'] = 'text/markdown'
    #"\n".join(linhas)
    return response
    #return dict(perguntas)  
    """

