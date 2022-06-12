import numpy as np
import pandas as pd
import plotly.graph_objs as go

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_admin_components as dac

# import basic_boxes.callbacks as callbacks
# import basic_boxes.view as view
import callbacks
import view
# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = Dash(__name__)
#server = app.server

# =============================================================================
# App Layout
# =============================================================================
# app.layout = dac.Page(
#     dac.Body(
#         dac.TabItems([view.content])
#     )
# )


def plot_scatter(N=50):
    trace1 = go.Scatter(
        y=np.random.randn(N),
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(N),  # set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
    return dict(data=[trace1])


# app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
app.layout = dac.Page([
    dac.Navbar(
        dac.NavbarDropdown(
            dac.NavbarDropdownItem()
        )
    ),
    dac.Sidebar(
        dac.SidebarMenu(
            dac.SidebarMenuItem(id='tab_cards', label='A', icon='heart'),
        ),
        title='BECOM',
    ),
    dac.Body(
        dac.TabItems([
            dac.TabItem(id='content_basic_boxes',
                        children=html.Div(
                            [
                                html.H1("dddddd"),
                                dac.SimpleBox(
                                    style={'height': "600px"},
                                    title="Box 1",
                                    children=[
                                        dcc.Graph(
                                            id='box-graph',
                                            config=dict(displayModeBar=False),
                                            style={'width': '38vw'}
                                        )
                                    ]
                                ),
                                dac.SimpleBox(
                                    style={'height': "600px"},
                                    title="Box 2",
                                    children=[
                                        dcc.Graph(
                                            figure=plot_scatter(),
                                            config=dict(displayModeBar=False),
                                            style={'width': '38vw'}
                                        )
                                    ]
                                )
                            ],
                            className='row'
                        )
                        )
        ])
    ),
    dac.Controlbar(),
    dac.Footer()
])
# =============================================================================
# Callback
# =============================================================================
callbacks.get_callbacks(app)


# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=False)
