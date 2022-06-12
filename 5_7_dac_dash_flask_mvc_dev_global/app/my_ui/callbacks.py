import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards",
              "basic_boxes", "value_boxes", "gallery_1", "gallery_2")


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
        return True, False, False, False, False, False, False  # App init


# =============================================================================
# Callbacks
# =============================================================================
def get_callbacks(app_dash):
    # -----------------------------------------------
    # -----------------------------------------------
    @app_dash.callback([Output('content_basic_cards', 'active'),
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
        # Callback context to recognize which input has been triggered
        ctx = dash.callback_context

        # Get id of input which triggered callback
        if not ctx.triggered:
            raise PreventUpdate
        else:
            input_id = ctx.triggered[0]['prop_id'].split('.')[0]

        return activate(input_id,
                        n_cards, n_social_cards, n_tab_cards, n_basic_boxes,
                        n_value_boxes, n_gallery_1, n_gallery_2)

    # -----------------------------------------------
    # -----------------------------------------------
    @app_dash.callback([Output('tab_cards', 'active'),
                        Output('tab_social_cards', 'active'),
                        Output('tab_tab_cards', 'active'),
                        Output('tab_basic_boxes', 'active'),
                        Output('tab_value_boxes', 'active'),
                        Output('tab_gallery_1', 'active'),
                        Output('tab_gallery_2', 'active')],
                       [Input('tab_cards',        'n_clicks'),
                        Input('tab_social_cards', 'n_clicks'),
                        Input('tab_tab_cards', 'n_clicks'),
                        Input('tab_basic_boxes', 'n_clicks'),
                        Input('tab_value_boxes', 'n_clicks'),
                        Input('tab_gallery_1', 'n_clicks'),
                        Input('tab_gallery_2', 'n_clicks')]
                       )
    def activate_tab(n_cards, n_social_cards, n_tab_cards, n_basic_boxes,
                     n_value_boxes, n_gallery_1, n_gallery_2):

        # Callback context to recognize which input has been triggered
        ctx = dash.callback_context

        # Get id of input which triggered callback
        if not ctx.triggered:
            raise PreventUpdate
        else:
            input_id = ctx.triggered[0]['prop_id'].split('.')[0]

        return activate(input_id,
                        n_cards, n_social_cards, n_tab_cards, n_basic_boxes,
                        n_value_boxes, n_gallery_1, n_gallery_2)



