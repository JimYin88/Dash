'''
Created on May 26, 2022

@author: Jim Yin
'''


from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    dcc.Checklist(['New York City', 'Montreal', 'San Francisco'], ['Montreal'], id='demo-checklist'),
    html.Div(id='dd-output-container3'),    
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
    html.Div(id='dd-output-container'),
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown2'),
    html.Div(id='dd-output-container2')
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'

@app.callback(
    Output('dd-output-container3', 'children'),
    Input('demo-checklist', 'value')
)
def update_output3(value):
    return f'You have selected {value}'

@app.callback(
    Output('dd-output-container2', 'children'),
    Input('demo-dropdown2', 'value')
)
def update_output2(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)