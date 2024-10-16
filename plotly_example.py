from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app= Dash(__name__) #new Dash app named app

app.layout = html.Div([
    html.H1(children = 'Hello Dash app', style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Finland', id='dropdown-country'),
    dcc.Graph(id='graph-content')
])


@callback(Output('graph-content', 'figure'),
          Input('dropdown-country', 'value'))

def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop', color='country')

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)