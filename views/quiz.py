from flask import render_template, request, jsonify, current_app, make_response, Blueprint
import json

from utils.quiz_funcoes import escolher_perguntas, verifica_resposta

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route('/', methods=['GET', 'POST'])
def generate_quiz():
    if request.method == "GET":
        return make_response(render_template('quiz.html'), 200)
    
    elif request.method == "POST":
    #     """
    #     Preencha aqui a função 'receber quiz'
        
    #     Essa função deve retornar as perguntas do quiz no formato JSON.
    #     """
    #     formulario = dict(request.form)
    #     dificuldade = formulario.get('Dificuldade', None)
    #     if dificuldade is None:
    #         return "Dificuldade não pode ser vazia!", 400

    #     STATIC = current_app.config['STATIC']
    #     perguntas, _ = escolher_perguntas(dificuldade, STATIC)
    #     return jsonify(perguntas)
        return make_response(render_template('quiz.html'), 200)
    
    
# @quiz_bp.route('/responder', methods=['POST'])
# def answer_quiz():
#     """ 
#     Preencha aqui a 'devolver quiz'
    
#     Essa função deve receber as respostas das perguntas do quiz e devolver a pontuação.
#     """
#     formulario = dict(request.form)
#     dificuldade = formulario.get('Dificuldade', None)
#     respostas = formulario.get('Resposta', None)
#     if dificuldade is None:
#         return "Dificuldade não pode ser vazia!", 400
#     if respostas is None:
#         return f"Resposta não pode ser vazia!"

#     STATIC = current_app.config['STATIC']
#     respostas = json.loads(respostas)
#     resultado = verifica_resposta(dificuldade, respostas, STATIC)
#     return jsonify(resultado)
