import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_admin_components as dac

from my_ui.menubar   import navbar, sidebar, controlbar
from my_ui.contents  import body , footer
from my_ui.callbacks import get_callbacks

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
get_callbacks(app)














# =============================================================================
# Run app    
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
