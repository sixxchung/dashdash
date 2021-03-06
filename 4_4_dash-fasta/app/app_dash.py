import dash
from dash import dcc, html 

import dash_bootstrap_components as dbc
import dash_admin_components as dac
import flask

from app.utils.external_assets import ROOT, EXTERNAL_STYLESHEETS, FONT_AWSOME
from app.ui.main_content import navbar, sidebar, body, controlbar, footer

import datetime
import os

def create_dashApp(requests_pathname_prefix: str = None) -> dash.Dash:
    # =============================================================================
    # DashApp and Flask Server
    # =============================================================================
    server = flask.Flask(__name__)
    #server.secret_key = os.environ.get('secret_key', 'secret')

    dashApp = dash.Dash(
        name=__name__, 
        server=server, 
        #routes_pathname_prefix=requests_pathname_prefix,
        requests_pathname_prefix=requests_pathname_prefix,
        #assets_folder=ROOT+"/assets",

        #suppress_callback_exceptions=True, 
        # external_stylesheets=[
        #     dbc.themes.CYBORG, 
        #     FONT_AWSOME,
        #     #EXTERNAL_STYLESHEETS
        # ], 
        # meta_tags=[
        #     {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        # ]     
    )
    #dashApp.scripts.config.serve_locally = False
    #dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'
    dashApp.layout =  dac.Page([navbar, sidebar, body, controlbar, footer])
    
    return dashApp

dash_app = create_dashApp(requests_pathname_prefix="/dash/")
