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
        
        if idade == "Até 8 anos!":
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            xs = np.random.rand(100)
            ys = np.random.rand(100)
            axis.plot(xs, ys)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
            #return "A idade é até 8 anos"
        elif idade == "Entre 9 e 15!":
            
            return "A idade é entre 9 e 15 anos"
        elif idade == "16 ou mais!":
            
            return "A idade é 16 ou mais!"
        


        #return f"Sem graficos definidos ainda, mas sua idade é {idade}!", 200