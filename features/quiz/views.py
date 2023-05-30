from flask import render_template, request, jsonify, current_app, make_response
from flask_restx import Namespace, Resource

from .quiz_funcoes import escolher_perguntas, verifica_resposta
from . import quiz_gerar, quiz_responder


quiz_ns = Namespace("Quiz da Água", description="Sabe bastante sobre o uso da água no mundo? Teste seu conhecimento aqui!")

@quiz_ns.route('/')
class GerarQuiz(Resource):
    def get(self):
        return make_response(render_template('quiz.html'), 200)
    
    @quiz_ns.doc(expect=[quiz_gerar])
    def post(self):
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

@quiz_ns.route('/responder')
class ResponderQuiz(Resource):
    @quiz_ns.doc(expect=[quiz_gerar, quiz_responder])
    def post(self):
        """ 
        Preencha aqui a 'devolver quiz'
        
        Essa função deve receber as respostas das perguntas do quiz e devolver a pontuação.
        """
        formulario = dict(request.form)
        dificuldade = formulario.get('Dificuldade', None)
        respostas = formulario.get(f'Resposta')
        if dificuldade is None:
            return "Dificuldade não pode ser vazia!", 400
        if respostas is None:
            return f"Resposta não pode ser vazia!"

        STATIC = current_app.config['STATIC']
        resultado = verifica_resposta(dificuldade, respostas, STATIC)
        return jsonify(resultado)
