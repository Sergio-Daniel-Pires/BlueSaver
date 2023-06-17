from flask import render_template, Response, make_response, Blueprint
import plotly.express as px
import pandas as pd
from factory import data

graficos_bp = Blueprint("Graficos", __name__)

@graficos_bp.route('/')
def show_graph():
    """
    Pagina que renderiza os gráficos
    """
    return make_response(render_template('graficos.html'), 200)

@graficos_bp.route('/<idade>')
def show_graph_specify(idade: str):
    if idade not in ('8_old', 'between_9_and_15', 'up_to_16'):
        return Response('Idade invalida, por favor, insira outra e tente novamente', 400)

    if idade == "8_old": 
        list_values = data.get_graph_as_csv("industrial-water-withdrawal")
        df_industrial = pd.DataFrame(list_values[1:], columns=list_values[0])

        t = pd.DataFrame(df_industrial.groupby(by="Entity")["Industrial water withdrawal"].sum().reset_index())
        t = t.sort_values(by=t.columns[1], ascending=False).head(10)
        fig = px.pie(t, names="Entity", values="Industrial water withdrawal", title="Retirada de água para indústria por país")
        res_html =  fig.to_html(full_html=False)
        
    elif idade == "between_9_and_15":
        list_values = data.get_graph_as_csv("global-freshwater-use-over-the-long-run")
        df_uso_agua = pd.DataFrame(list_values[1:], columns=list_values[0])

        df_uso_agua = df_uso_agua[df_uso_agua["Year"] <= 2010]
        df_uso_agua.rename(columns={"Year": "Ano", "Freshwater use": "Consumo de água potável"}, inplace=True)
        fig = px.bar(df_uso_agua, x="Ano", y="Consumo de água potável", title="Uso de água potável ao longo do tempo")
        res_html =  fig.to_html(full_html=False)

    elif idade == "up_to_16":
        list_values = data.get_graph_as_csv("per-capita-renewable-freshwater-resources")
        df_per_capita = pd.DataFrame(list_values[1:], columns=list_values[0])

        df_per_capita.sort_values(by="Per capita renewable resources", ascending=False, inplace=True)
        df_per_capita.rename(columns={"Entity": "Entidade", "Per capita renewable resources": "Água renovável per capita"}, inplace=True)
        fig = px.bar(df_per_capita, x="Entidade", y="Água renovável per capita", title="Água renovável per capita por região")
        res_html = fig.to_html(full_html=False)

    return make_response(res_html, 200)