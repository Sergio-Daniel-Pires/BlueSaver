from flask_restx import reqparse

quiz_gerar = reqparse.RequestParser()
quiz_gerar.add_argument('Dificuldade', type=str, help='Insira a dificuldade do quiz!',
                        required=True, location="form", choices=("Fácil", "Médio", "Difícil"))

quiz_responder = reqparse.RequestParser()
quiz_responder.add_argument('Resposta 1', type=str, help='Letra referente a resposta 1',
                            required=True, location="form", choices=('a', 'b', 'c'))
quiz_responder.add_argument('Resposta 2', type=str, help='Letra referente a resposta 2',
                            required=True, location="form", choices=('a', 'b', 'c'))
quiz_responder.add_argument('Resposta 3', type=str, help='Letra referente a resposta 3',
                            required=True, location="form", choices=('a', 'b', 'c'))
quiz_responder.add_argument('Resposta 4', type=str, help='Letra referente a resposta 4',
                            required=True, location="form", choices=('a', 'b', 'c'))

#ToDo Tornar esta seção automatizada, ou escolher 3~4 perguntas aleatoriamente dentre várias em um banco de dados