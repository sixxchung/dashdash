from app.dash_app import dash_app
from dash.dependencies      import Input, Output, State
from . import example_plots

# Update figure on slider change
@dash_app.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')] )
def update_box_graph(value):
    # go.Figure()
    return example_plots.plot_scatter(value)



