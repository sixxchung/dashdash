from dash import Dash
import dash_admin_components as dac

from my_ui.view import navbar, sidebar, body, controlbar, footer

#from my_ui.callbacks import get_callbacks
import my_ui.callbacks as main
import dashPages.basic_boxes.callbacks as basic_boxes
import dashPages.tab_cards.callbacks as tab_cards
import dashPages.gallery_1.callbacks as gallery_1
import dashPages.gallery_2.callbacks as gallery_2
import dashPages.stock.callbacks as stock

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
main.get_callbacks(app)

tab_cards.get_callbacks(app)
basic_boxes.get_callbacks(app)

gallery_1.get_callbacks(app)
gallery_2.get_callbacks(app)

stock.get_callbacks(app)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
