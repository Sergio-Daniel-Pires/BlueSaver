from flask_restx import Namespace, Resource
from flask import request
from flask import Flask, render_template
from flask import Response
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import plotly.express as px
import plotly
import pandas as pd
import numpy as np
import json
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
            path_df = "static/industrial-water-withdrawal.csv"
            df_uso_agua = pd.read_csv(path_df, sep = ",")
            t = pd.DataFrame(df_uso_agua.groupby(by="Entity")["Industrial water withdrawal"].sum().reset_index())
            t = t.sort_values(by=t.columns[1], ascending=False).head(10)
            fig = px.pie(t, names="Entity", values="Industrial water withdrawal", title="Retirada de água para indústria por país")
            fig.write_image("static/fig2.png", "png")
            img = open("static/fig2.png", "rb")
            return Response(img, mimetype="image/png")
        
        elif idade == "Entre 9 e 15!":
        
            path_df = "static/global-freshwater-use-over-the-long-run.csv"
            df_uso_agua = pd.read_csv(path_df, sep = ",")
            df_uso_agua = df_uso_agua[df_uso_agua["Year"] <= 2010]
            fig = px.bar(df_uso_agua, x="Year", y="Freshwater use", title="Uso de água ao longo do tempo")
            fig.write_image("static/fig1.png", "png")
            img = open("static/fig1.png", "rb")
            return Response(img, mimetype="image/png")

        elif idade == "16 ou mais!":
            
            return "A idade é 16 ou mais!"
        


        #return f"Sem graficos definidos ainda, mas sua idade é {idade}!", 200