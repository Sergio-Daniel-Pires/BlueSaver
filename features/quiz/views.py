from flask import Flask, render_template, request, jsonify, Blueprint, current_app
from .quiz_funcoes import escolher_perguntas, verifica_resposta

quiz_bp = Blueprint("Quiz", "quiz", url_prefix='/quiz')

@quiz_bp.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html')
    elif request.method == 'POST':
        """
        Preencha aqui a função 'receber quiz'
        
        Essa função deve retornar as perguntas do quiz no formato JSON.
        """
        formulario = dict(request.form)
        print(formulario)
        dificuldade = formulario.get('Dificuldade', None)
        if dificuldade is None:
            return "Dificuldade não pode ser vazia!", 400

        STATIC = current_app.config['STATIC']
        perguntas, _ = escolher_perguntas(dificuldade, STATIC)
        return jsonify(perguntas)

@quiz_bp.route('/verificar_respostas', methods=['POST'])
def verificar_respostas():
    """ 
    Preencha aqui a 'devolver quiz'
    
    Essa função deve receber as respostas das perguntas do quiz e devolver a pontuação.
    """
    formulario = dict(request.form)
    dificuldade = formulario.get('Dificuldade', None)
    respostas = [formulario.get(f'Resposta {n}', None) for n in range(1, 5)]  # ToDo tornar o último elemento (no caso, 5) variável
    if dificuldade is None:
        return "Dificuldade não pode ser vazia!", 400
    if None in respostas:
        return f"Resposta {respostas.index(None)} não pode ser vazia!"

    STATIC = current_app.config['STATIC']
    resultado = verifica_resposta(dificuldade, respostas, STATIC)
    return jsonify(resultado)
