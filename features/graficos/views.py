from flask_restx import Namespace, Resource
from flask import request
from flask import Response
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import io

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
        
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        xs = np.random.rand(100)
        ys = np.random.rand(100)
        axis.plot(xs, ys)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
        #return f"Sem graficos definidos ainda, mas sua idade é {idade}!", 200