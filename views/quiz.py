from flask import render_template, request, jsonify, current_app, make_response, Blueprint
import os
import json

from utils.quiz_funcoes import escolher_perguntas, verifica_resposta

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route('/', methods=['GET', 'POST'])
def generate_quiz():
    if request.method == "GET":
        return make_response(render_template('quiz.html'), 200)
    
    elif request.method == "POST":
        """
        Preencha aqui a função 'receber quiz'
        Essa função deve retornar as perguntas do quiz no formato JSON.
        """

        STATIC = current_app.config['STATIC']
        with open(os.path.join(STATIC, 'perguntas.json'), "r") as file:
            perguntas = json.load(file)  
        return jsonify(perguntas)
    