from dash import Dash, html
import dash_bootstrap_components as dbc

def button_html() -> html:

    return html.Div([
        dbc.Button("Who am I ?", id="me", n_clicks=0, className="home_button",color="secondary"),
        dbc.Button("My Studies", id="studies", n_clicks=0, className="home_button",color="secondary"),
        dbc.Button("My Career", id="career", n_clicks=0, className="home_button",color="secondary"),
        dbc.Button("My python developpment", id="python", n_clicks=0, className="home_button",color="secondary"),
    ])
