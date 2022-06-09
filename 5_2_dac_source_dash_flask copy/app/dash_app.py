import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_admin_components as dac

from dash.exceptions import PreventUpdate

from my_ui.main_content import body , footer
from my_ui.main_sidebar import navbar, sidebar, controlbar

from example_plots import plot_scatter
from app.tab_cards import text_1, text_2, text_3
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
# Callbacks
# =============================================================================
def activate(input_id, 
             n_cards, n_social_cards, n_tab_cards, n_basic_boxes,
             n_value_boxes, n_gallery_1, n_gallery_2):
    
    # Depending on tab which triggered a callback, show/hide contents of app
    if input_id == 'tab_cards' and n_cards:
        return True, False, False, False, False, False, False
    elif input_id == 'tab_social_cards' and n_social_cards:
        return False, True, False, False, False, False, False
    elif input_id == 'tab_tab_cards' and n_tab_cards:
        return False, False, True, False, False, False, False
    elif input_id == 'tab_basic_boxes' and n_basic_boxes:
        return False, False, False, True, False, False, False
    elif input_id == 'tab_value_boxes' and n_value_boxes:
        return False, False, False, False, True, False, False
    elif input_id == 'tab_gallery_1' and n_gallery_1:
        return False, False, False, False, False, True, False
    elif input_id == 'tab_gallery_2' and n_gallery_2:
        return False, False, False, False, False, False, True
    else:
        return True, False, False, False, False, False, False # App init
    
@app.callback([Output('content_cards', 'active'),
               Output('content_social_cards', 'active'),
               Output('content_tab_cards', 'active'),
               Output('content_basic_boxes', 'active'),
               Output('content_value_boxes', 'active'),
               Output('content_gallery_1', 'active'),
               Output('content_gallery_2', 'active')],
               [Input('tab_cards', 'n_clicks'),
                Input('tab_social_cards', 'n_clicks'),
                Input('tab_tab_cards', 'n_clicks'),
                Input('tab_basic_boxes', 'n_clicks'),
                Input('tab_value_boxes', 'n_clicks'),
                Input('tab_gallery_1', 'n_clicks'),
                Input('tab_gallery_2', 'n_clicks')]
)
def display_tab(n_cards, n_social_cards, n_tab_cards, n_basic_boxes, 
                n_value_boxes, n_gallery_1, n_gallery_2):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   

    return activate(input_id, 
                    n_cards, n_social_cards, n_tab_cards, n_basic_boxes, 
                    n_value_boxes, n_gallery_1, n_gallery_2)

@app.callback([Output('tab_cards', 'active'),
               Output('tab_social_cards', 'active'),
               Output('tab_tab_cards', 'active'),
               Output('tab_basic_boxes', 'active'),
               Output('tab_value_boxes', 'active'),
               Output('tab_gallery_1', 'active'),
               Output('tab_gallery_2', 'active')],
               [Input('tab_cards', 'n_clicks'),
                Input('tab_social_cards', 'n_clicks'),
                Input('tab_tab_cards', 'n_clicks'),
                Input('tab_basic_boxes', 'n_clicks'),
                Input('tab_value_boxes', 'n_clicks'),
                Input('tab_gallery_1', 'n_clicks'),
                Input('tab_gallery_2', 'n_clicks')]
)
def activate_tab(n_cards, n_social_cards, n_tab_cards, n_basic_boxes, 
                n_value_boxes, n_gallery_1, n_gallery_2):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   

    return activate(input_id, 
                    n_cards, n_social_cards, n_tab_cards, n_basic_boxes, 
                    n_value_boxes, n_gallery_1, n_gallery_2)
















@app.callback(Output('tab_box_1', 'children'),
              [Input('tab_box_1_menu', 'active_tab')]
)
def display_tabbox1(active_tab):

    # Depending on tab which triggered a callback, show/hide contents of app
    if active_tab == 'tab_box_1_tab1':
        return text_1
    elif active_tab == 'tab_box_1_tab2':
        return text_2
    elif active_tab == 'tab_box_1_tab3':
        return text_3

@app.callback(Output('tab_box_2', 'children'),
              [Input('tab_box_2_menu', 'active_tab')]
)
def display_tabbox2(active_tab):

    # Depending on tab which triggered a callback, show/hide contents of app
    if active_tab == 'tab_box_2_tab1':
        return text_1
    elif active_tab == 'tab_box_2_tab2':
        return text_2
    elif active_tab == 'tab_box_2_tab3':
        return text_3
    
# Update figure on slider change
@app.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    return plot_scatter(value)

# =============================================================================
# Run app    
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
