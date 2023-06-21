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

    # Dispensaveis (Dois/Tres fragmentos identicos em if's)
    date_to_graph_name = {'8_old': 'industrial-water-withdrawal', 'between_9_and_15': 'global-freshwater-use-over-the-long-run', 'up_to_16': 'per-capita-renewable-freshwater-resources'}
    list_values = data.get_graph_as_csv(date_to_graph_name[idade])
    current_df = pd.DataFrame(list_values[1:], columns=list_values[0])

    if idade == "8_old": # Simples, eu não importo, pedi pra não fazerem isso
        t = pd.DataFrame(current_df.groupby(by="Entity")["Industrial water withdrawal"].sum().reset_index())
        t = t.sort_values(by=t.columns[1], ascending=False).head(10)
        fig = px.pie(t, names="Entity", values="Industrial water withdrawal", title="Retirada de água para indústria por país")
        
    elif idade == "between_9_and_15":
        current_df = current_df[current_df["Year"] <= 2010]
        current_df.rename(columns={"Year": "Ano", "Freshwater use": "Consumo de água potável"}, inplace=True)
        fig = px.bar(current_df, x="Ano", y="Consumo de água potável", title="Uso de água potável ao longo do tempo")

    elif idade == "up_to_16":
        current_df.sort_values(by="Per capita renewable resources", ascending=False, inplace=True)
        current_df.rename(columns={"Entity": "Entidade", "Per capita renewable resources": "Água renovável per capita"}, inplace=True)
        fig = px.bar(current_df, x="Entidade", y="Água renovável per capita", title="Água renovável per capita por região")

    res_html = fig.to_html(full_html=False)
    return make_response(res_html, 200)