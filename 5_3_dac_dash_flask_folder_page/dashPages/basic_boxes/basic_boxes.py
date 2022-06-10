from dash import html
from dash import dcc
import dash_admin_components as dac

from example_plots import plot_scatter

tab = dac.TabItem(id='content_basic_boxes', 
                              
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