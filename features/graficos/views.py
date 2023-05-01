from flask_restx import Namespace, Resource
from flask import request
from flask import Flask, render_template

from .funcoes import show_graph

from . import grafico_options

graficos_ns = Namespace("Graficos", description="Exibe gráficos interessantes sobre o uso da água de acordo com sua idade")

@graficos_ns.route('/visualizar')
class GraficosVer(Resource):
    @graficos_ns.doc(expect=[grafico_options])
    def post(self):
        """
        Preencha aqui a função 'ver graficos'

        Essa função deve retornar os graficos em formato visualização.
        """
        formulario = dict(request.form)
        idade = formulario.get('Idade', None)
        if idade is None:
            return "Idade não pode ser vazia!", 400
        
        return show_graph(idade)
