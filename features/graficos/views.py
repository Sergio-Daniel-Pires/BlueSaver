from flask import render_template, Response, make_response
from flask_restx import Namespace, Resource

import plotly.express as px

from . import grafico_options

graficos_ns = Namespace("Graficos", description="Exibe gráficos interessantes sobre o uso da água de acordo com sua idade")

@graficos_ns.route('/')
class GraficosVer(Resource):
    @graficos_ns.doc(expect=[grafico_options])
    def get(self):
        """
        Pagina que renderiza os gráficos
        """
        return make_response(render_template('graficos.html'), 200)

import pandas as pd

@graficos_ns.route('/<idade>')
class GraficosVer(Resource):
    @graficos_ns.doc()
    def get(self, idade: str):
        if idade not in ('8_old', 'between_9_and_15', 'up_to_16'):
            return Response('Idade invalida, por favor, insira outra e tente novamente', 400)

        if idade == "8_old": # Simples, eu não importo, pedi pra não fazerem isso
            path_df = "static/industrial-water-withdrawal.csv"
            df_industrial = pd.read_csv(path_df, sep = ",")

            t = pd.DataFrame(df_industrial.groupby(by="Entity")["Industrial water withdrawal"].sum().reset_index())
            t = t.sort_values(by=t.columns[1], ascending=False).head(10)
            fig = px.pie(t, names="Entity", values="Industrial water withdrawal", title="Retirada de água para indústria por país")
            res_html =  fig.to_html(full_html=False)
            
        elif idade == "between_9_and_15":
            path_df = "static/global-freshwater-use-over-the-long-run.csv"
            df_uso_agua = pd.read_csv(path_df, sep = ",")
            df_uso_agua = df_uso_agua[df_uso_agua["Year"] <= 2010]
            df_uso_agua.rename(columns={"Year": "Ano", "Freshwater use": "Consumo de água potável"}, inplace=True)
            fig = px.bar(df_uso_agua, x="Ano", y="Consumo de água potável", title="Uso de água potável ao longo do tempo")
            res_html =  fig.to_html(full_html=False)

        elif idade == "up_to_16":
            path_df = "static/per-capita-renewable-freshwater-resources.csv"
            df_per_capita = pd.read_csv(path_df, sep = ",")
            df_per_capita.sort_values(by="Per capita renewable resources", ascending=False, inplace=True)
            df_per_capita.rename(columns={"Entity": "Entidade", "Per capita renewable resources": "Água renovável per capita"}, inplace=True)
            fig = px.bar(df_per_capita, x="Entidade", y="Água renovável per capita", title="Água renovável per capita por região")
            res_html = fig.to_html(full_html=False)

        return make_response(res_html, 200)