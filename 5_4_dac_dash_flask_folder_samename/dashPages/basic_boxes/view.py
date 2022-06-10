from dash import html
from dash import dcc
import dash_admin_components as dac

from . import example_plots

content = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div(
        [
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 1",
                children=[
                    dcc.Graph(
                        id='box-graph',
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            ),
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 2",
                children=[
                    dcc.Graph(
                        figure=example_plots.plot_scatter(),
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            )
        ], 
        className='row'
    )
)