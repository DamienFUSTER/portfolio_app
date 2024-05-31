import dash
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd
import plotly.express as px

dash.register_page(__name__, name="Dashboard example")

df = pd.read_excel(r"pages/data/database.xlsx")


# ----- Component -----

title_markdown = dcc.Markdown("""## Example of app \n data from https://draaf.occitanie.agriculture.gouv.fr/cereales-oleagineux-proteagineux-r571.html""", id="title_markdown", className="title_dashboard")

dropdown_parameter = dcc.Dropdown(["Rendement aux normes (q/ha)","Objectif de rendement moyen (q/ha)","Part surfaces irriguées (% de la sole implantée)"],"Rendement aux normes (q/ha)",id = "drop_para")

graphique_scat = dcc.Graph(id = "graph_agri")


layout = html.Div([
    title_markdown,
    html.Div([
        dropdown_parameter,
        graphique_scat
    ])
])

@callback(
    Output(component_id="graph_agri", component_property="figure"),
    Input(component_id="drop_para",component_property="value")
)
def scheme_change(input):
    list_y = []
    for i in df.loc[df["partie"] == input, ["1994", "2001", "2006", "2011", "2014", "2017"]].iloc[0]:
        list_y.append(i)
    return px.scatter(x=[1994,2001,2006,2011,2014,2017], y=list_y)

