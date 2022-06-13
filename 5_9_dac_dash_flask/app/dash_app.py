from dash import Dash
import dash_admin_components as dac
from dashMain.view import navbar, sidebar, body, controlbar, footer

import dashPages
import dashMain

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
dashPages.tab_cards.callbacks.get_callbacks(app)
dashPages.basic_boxes.callbacks.get_callbacks(app)
dashPages.gallery_1.callbacks.get_callbacks(app)
dashPages.gallery_2.callbacks.get_callbacks(app)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
