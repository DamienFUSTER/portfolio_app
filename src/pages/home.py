import dash
from dash import (dcc, html, Input, Output, callback, ctx)
from src.pages.component.button_comp import button_html
from src.pages.text.text import me_text, study_text, career_text, python_text



dash.register_page(__name__, path="/", name="About Me")


# ----- Component -----

title_markdown = dcc.Markdown("""## About Me""", id="title_markdown",className="title_home")

button_selection = button_html()

text_showing = html.Div([
    dcc.Markdown(id="text_show", className="text_showing_home")
    ], className="div_text_showing_home")


# ----- app layout -----

layout = html.Div([
    title_markdown,
    html.Br(),
    button_selection,
    html.Br(),
    text_showing
    ])

# ----- Callback


@callback(
    Output(component_id = "text_show", component_property = "children"),
    Input(component_id = "me", component_property = "n_clicks"),
    Input(component_id="studies", component_property="n_clicks"),
    Input(component_id="career", component_property="n_clicks"),
    Input(component_id="python", component_property="n_clicks"),
    )
def text_selection(me,study,career,python):
    id = ctx.triggered_id
    if id == "me":
        return me_text()
    elif id == "studies":
        return study_text()
    elif id == "career":
        return career_text()
    elif id == "python":
        return python_text()
    elif id is None:
        return me_text()

