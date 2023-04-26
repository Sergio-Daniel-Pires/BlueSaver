from flask_restx import Namespace, Resource
from flask import request

from . import quiz_gerar, quiz_responder

quiz_ns = Namespace("Quiz da Água", description="Sabe bastante sobre o uso da água no mundo? Teste seu conhecimento aqui!")

@quiz_ns.route('/gerar')
class GerarQuiz(Resource):
    @quiz_ns.doc(expect=[quiz_gerar])
    def post(self):
        """
        Preencha aqui a função 'receber quiz'
        
        Essa função deve retornar as perguntas do quiz no formato JSON.
        """
        formulario = dict(request.form)
        dificuldade = formulario.get('Dificuldade', None)
        if dificuldade is None:
            return "Dificuldade não pode ser vazia!", 400

        return f"Seu quiz tem dificuldade {dificuldade}", 200

@quiz_ns.route('/responder')
class ResponderQuiz(Resource):
    @quiz_ns.doc(expect=[quiz_gerar, quiz_responder])
    def post(self):
        """
        Preencha aqui a 'devolver quiz'
        
        Essa função deve receber as respostas das perguntas do quiz e deolver a pontuação.
        """
        formulario = dict(request.form)
        dificuldade = formulario.get('Dificuldade', None)
        respostas = [formulario.get(f'Resposta {n}', None) for n in range(1, 4)]
        if dificuldade is None:
            return "Dificuldade não pode ser vazia!", 400
        if None in respostas:
            return f"Resposta {respostas.index(None)} não pode ser vazia!"

        return f"Suas respostas para o quiz {dificuldade} foram: {respostas}", 200