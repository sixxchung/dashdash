

#import dash
from dash.dependencies import Input, Output
from dash import Dash, dcc, html

import dash_bootstrap_components as dbc
import dash_admin_components as dac

import flask
import pandas as pd
import os


from .my_assets.external_assets import * #ROOT, EXTERNAL_STYLESHEETS, FONT_AWSOME
from .my_ui.main_content import *


urlPath_dash = '/dash'
port_dash = 8050


def create_dash_app(requests_pathname_prefix: str = None) -> Dash:
    app_flask = flask.Flask(__name__)
    #app_flask.secret_key = os.environ.get('secret_key', 'secret')
    
    app_dash = Dash(__name__, 
        server=app_flask,
        requests_pathname_prefix=requests_pathname_prefix,
        assets_folder=ROOT+"/assets",
        suppress_callback_exceptions=True,
        external_stylesheets=[
            dbc.themes.CYBORG,
            FONT_AWSOME,
            EXTERNAL_STYLESHEETS
        ],
        # meta_tags=[
        #     {"name": "viewport",
        #      "content": "width=device-width, initial-scale=1"}
        # ]
    )

    app_dash.scripts.config.serve_locally = False
    #dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'
    
    # =============================================================================
    # App Layout
    # =============================================================================
    app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

    #app_dash.layout = layout 
    # app_dash.layout = html.Div([
    #     html.H1('Stock Tickers'),
    #     dcc.Dropdown(
    #         id='my-dropdown',
    #         options=[
    #             {'label': 'Tesla', 'value': 'TSLA'},
    #             {'label': 'Apple', 'value': 'AAPL'},
    #             {'label': 'Coke', 'value': 'COKE'}
    #         ],
    #         value='TSLA'
    #     ),
    #     dcc.Graph(id='my-graph')
    # ], className="container")
    # df = pd.read_csv(
    #     'https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

    # @app_dash.callback(Output('my-graph', 'figure'),
    #               [Input('my-dropdown', 'value')])
    # def update_graph(selected_dropdown_value):
    #     dff = df[df['Stock'] == selected_dropdown_value]
    #     return {
    #         'data': [{
    #             'x': dff.Date,
    #             'y': dff.Close,
    #             'line': {
    #                 'width': 3,
    #                 'shape': 'spline'
    #             }
    #         }],
    #         'layout': {
    #             'margin': {
    #                 'l': 30,
    #                 'r': 20,
    #                 'b': 30,
    #                 't': 20
    #             }
    #         }
    #     }

    return app_dash


app_dash = create_dash_app(requests_pathname_prefix=urlPath_dash)