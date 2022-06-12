import plotly.graph_objs as go
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State
#from components.example_plots import plot_scatter


def get_callbacks(app_dash):
    # Update figure on slider change
    @app_dash.callback(
        Output('box-graph', 'figure'),
        [Input('controlbar-slider', 'value')])
    def update_box_graph(value):
        # go.Figure()
        return plot_scatter(value)




def plot_scatter(N=50):
    trace1 = go.Scatter(
        y = np.random.randn(N),
        mode='markers',
        marker=dict(
            size=16,
            color = np.random.randn(N), #set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
    return dict(data=[trace1])
