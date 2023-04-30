from flask_restx import Namespace, Resource
from flask import request
from flask import Flask, render_template
from flask import Response
import plotly.express as px
import pandas as pd
import os

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
            df_industrial = pd.read_csv(path_df, sep = ",")


            t = pd.DataFrame(df_industrial.groupby(by="Entity")["Industrial water withdrawal"].sum().reset_index())
            t = t.sort_values(by=t.columns[1], ascending=False).head(10)
            fig = px.pie(t, names="Entity", values="Industrial water withdrawal", title="Retirada de água para indústria por país")
            if ["fig1.png"] not in os.listdir():
                fig.write_image("static/fig1.png", "png")
            img = open("static/fig1.png", "rb")
            return Response(img, mimetype="image/png")
        
        elif idade == "Entre 9 e 15!":
        
            path_df = "static/global-freshwater-use-over-the-long-run.csv"
            df_uso_agua = pd.read_csv(path_df, sep = ",")
            df_uso_agua = df_uso_agua[df_uso_agua["Year"] <= 2010]
            df_uso_agua.rename(columns={"Year": "Ano", "Freshwater use": "Consumo de água potável"}, inplace=True)
            fig = px.bar(df_uso_agua, x="Ano", y="Consumo de água potável", title="Uso de água potável ao longo do tempo")
            if ["fig2.png"] not in os.listdir():
                fig.write_image("static/fig2.png", "png")   
            img = open("static/fig2.png", "rb")
            return Response(img, mimetype="image/png")

        elif idade == "16 ou mais!":

            path_df = "static/per-capita-renewable-freshwater-resources.csv"
            df_per_capita = pd.read_csv(path_df, sep = ",")
            df_per_capita.sort_values(by="Per capita renewable resources", ascending=False, inplace=True)
            df_per_capita.rename(columns={"Entity": "Entidade", "Per capita renewable resources": "Água renovável per capita"}, inplace=True)
            fig = px.bar(df_per_capita, x="Entidade", y="Água renovável per capita", title="Água renovável per capita por região")
            if ["fig3.png"] not in os.listdir():
                fig.write_image("static/fig3.png", "png")
            img = open("static/fig3.png", "rb")
            return Response(img, mimetype="image/png")
