# ----- Import -----
import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from time import localtime, strftime


# ----- Application -----


def main():  # our function for the starting app
    """ import the app """

    # ----- app start -----
    app = Dash(__name__, pages_folder="pages", use_pages=True,  external_stylesheets=[dbc.themes.DARKLY])
    server = app.server

    # ----- app components -----

    title_markdown = dcc.Markdown("""### Portfolio Application""", id = "title_markdown",className="title_app")

    side_bar = dbc.Nav([
        dbc.NavLink([html.Div(page["name"])],href=page["path"],active="exact")for page in dash.page_registry.values()],vertical=True,pills=True)

    time = html.H6(strftime("%H:%M", localtime()),className="time")

    # ----- app layout -----

    app.layout = html.Div([
        html.Div([
            html.Div([
                title_markdown,
                html.Hr(),
                side_bar],
                className="page_selection"),

            html.Div([
                dash.page_container],
                className="page_show"),

            html.Div([
                html.H6("FUSTER Damien",className="center_footer_app"),
                time
                ],className="app_footer")])

    ],className="all_page")


    # ----- app Run ------

    app.run(debug = True)

if __name__ == "__main__":
    main()

