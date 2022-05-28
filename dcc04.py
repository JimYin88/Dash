'''
Created on May 26, 2022

@author: Jim Yin
'''


from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    html.H1(children='Hello Dash'),
    html.H2(children='An example of a Range Slider.'),
    dcc.RangeSlider(0, 20, 1, value=[5, 15], id='my-range-slider'),
    html.Div(id='dd-output-container5'),
    html.H2(children='An example of a Radio Selector.'),    
    dcc.RadioItems(['New York City', 'Montreal','San Francisco'], 'Montreal', id ='demo-radioitem'),
    html.Div(id='dd-output-container4'),
    html.H2(children='An example of a Check List Selector.'),
    dcc.Checklist(['New York City', 'Montreal', 'San Francisco'], ['Montreal'], id='demo-checklist'),
    html.Div(id='dd-output-container3'),
    html.H2(children='Examples of a Dropdown Menu.'),   
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
    html.Div(id='dd-output-container'),
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown2'),
    html.Div(id='dd-output-container2')
])


@app.callback(
    Output('dd-output-container5', 'children'),
    Input('my-range-slider', 'value')
)
def update_output5(value):
    return f'You have selected {value}'

@app.callback(
    Output('dd-output-container4', 'children'),
    Input('demo-radioitem', 'value')
)
def update_output4(value):
    return f'You have selected {value}'

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