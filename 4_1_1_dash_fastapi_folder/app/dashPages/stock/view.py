from dash import dcc, html
import dash_admin_components as dac

content = dac.TabItem(
    id='content_stock',
    children=html.Div([
        html.H1('Stock Tickers'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'},
                {'label': 'Coke', 'value': 'COKE'}
            ],
            value='TSLA'
        ),
        dcc.Graph(id='my-graph')
    ], className="row")
)
