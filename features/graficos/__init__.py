from flask_restx import reqparse

grafico_options = reqparse.RequestParser()
grafico_options.add_argument('Idade', type=str, help='Insira sua idade para podermos filtrar melhor quais informações mostrar!',
                             required=True, location="form", choices=("Até 8 anos!", "Entre 9 e 15!", "16 ou mais!"))