from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

app= Dash(__name__) #new Dash app named app

year_list = [i for i in range(1980, 2024, 1)]

app.layout = html.Div([
    html.H1(children='Automobile Sales Statistics Dashboard!!!',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    html.Div([
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            placeholder='Select Statistics',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        ),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)