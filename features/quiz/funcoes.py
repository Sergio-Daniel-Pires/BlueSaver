import json
import os

def escolher_perguntas(dificuldade: str, arquivos_estaticos: str) -> dict:
    """
    Com base numa dificuldade, devolve perguntas dela.
    """
    print(f"Seu quiz tem dificuldade {dificuldade}")

    with open(os.path.join(arquivos_estaticos, 'perguntas.json'), "r") as perguntas_json:
        perguntas = json.loads(perguntas_json.read())

    for numquestao in perguntas[dificuldade] :
        print(perguntas[dificuldade][numquestao]['Pergunta'])

        for alternativa in perguntas[dificuldade][numquestao]['Opcoes'] :
            print(alternativa,") ",perguntas[dificuldade][numquestao]['Opcoes'][alternativa])