from dash import Dash

import dash_admin_components as dac
from app.dashMain.view import navbar, sidebar, body, controlbar, footer
import flask

import dashPages
def create_dash_app(requests_pathname_prefix: str = None) -> Dash:
    app_flask = flask.Flask(__name__)
    # =============================================================================
    # Dash App and Flask Server
    # =============================================================================
    app = Dash(
        __name__, 
        server = app_flask, 
        requests_pathname_prefix=requests_pathname_prefix)
    #server = app.server
    # =============================================================================

    app.scripts.config.serve_locally = False
    # =============================================================================
    # App Layout
    # =============================================================================
    app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

    return app


    # =============================================================================
    # Callback
    # =============================================================================
    # dashMain.callbacks.get_callbacks(app)

    # dashPages.tab_cards.callbacks.get_callbacks(app)
    # dashPages.basic_boxes.callbacks.get_callbacks(app)

    # dashPages.gallery_1.callbacks.get_callbacks(app)
    # dashPages.gallery_2.callbacks.get_callbacks(app)
    

# =============================================================================
# Run app
# =============================================================================
# if __name__ == '__main__':
#     app.run_server(debug=False)
