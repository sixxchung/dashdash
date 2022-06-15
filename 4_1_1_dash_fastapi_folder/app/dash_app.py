from dash import Dash
import dash_admin_components as dac

from dashMain.view import navbar, sidebar, body, controlbar, footer

import dashMain
import dashPages.stock as cb

import flask
import os


# def create_dash_app(requests_pathname_prefix: str = None) -> Dash:
#     app_flask = flask.Flask(__name__)
#     #app_flask.secret_key = os.environ.get('secret_key', 'secret')

#     app_dash = Dash(__name__,
#                     server=app_flask,
#                     requests_pathname_prefix=requests_pathname_prefix)

#     app_dash.scripts.config.serve_locally = False
#     #dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

#     #app_dash.layout = layout


# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = Dash(__name__)
server = app.server

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Callback
# =============================================================================
dashMain.callbacks.get_callbacks(app)
cb.callbacks.get_callbacks(app)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
