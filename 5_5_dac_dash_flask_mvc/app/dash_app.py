from dash import Dash
import dash_admin_components as dac

from my_ui.view import navbar, sidebar, controlbar, body, footer

#from my_ui.callbacks import get_callbacks
import my_ui.callbacks as main
import dashPages.tab_cards.callbacks as tab_cards
#from example_plots import plot_scatter
#from dashPages.tab_cards import text_1, text_2, text_3
# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = Dash(__name__)
server = app.server

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])


main.get_callbacks(app)
tab_cards.get_callbacks(app)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
