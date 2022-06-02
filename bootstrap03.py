'''
Created on May 29, 2022

@author: Jim Yin
'''

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, 
                  bordered=True, 
                  dark=True,
                  hover=True,
                  responsive=True,
                  striped=True)

color_selector = html.Div(
    [
        html.Div("Select a colour theme:"),
        dbc.Select(
            id="change-table-color",
            options=[
                {"label": "primary", "value": "primary"},
                {"label": "secondary", "value": "secondary"},
                {"label": "success", "value": "success"},
                {"label": "danger", "value": "danger"},
                {"label": "warning", "value": "warning"},
                {"label": "info", "value": "info"},
                {"label": "light", "value": "light"},
                {"label": "dark", "value": "dark"},
            ],
            value="primary",
        ),
    ],
    className="p-3 m-2 border",
)


app.layout = html.Div(children=[
    html.H1('Hello Dash', style={'textAlign': 'left', 'color': '#7FDBFF'}),
    
    dbc.NavbarSimple(children=[dbc.NavItem(dbc.NavLink("Page 1", href="#")),
                               dbc.DropdownMenu(children=[dbc.DropdownMenuItem("More pages", header=True),
                                                          dbc.DropdownMenuItem("Page 2", href="#"),
                                                          dbc.DropdownMenuItem("Page 3", href="#")],
                               nav=True,
                               in_navbar=True,
                               label="More")
                               ],
                    brand="NavbarSimple",
                    brand_href="#",
                    color="primary",
                    dark=True),
        
    html.H2(children='''Dash: A web application framework for your data.'''),
    
    color_selector,
    
    dbc.Table(table_header + table_body,
              bordered=True, 
              dark=True,
              hover=True,
              responsive=True,
              striped=True,
              id="table-color",
              color="primary"),
        
    html.H2(children='Headline: Level 2 Size'),
    
    dbc.DropdownMenu(label="Menu",
                     children=[dbc.DropdownMenuItem("Item 1"),
                               dbc.DropdownMenuItem("Item 2"),
                               dbc.DropdownMenuItem("Item 3")]
                     ),

    html.Label('Dropdown'),
    
    dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),

    html.Br(),
    
    html.Label('Multi-Select Dropdown'),
    
    dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'],
                 ['Montreal', 'San Francisco'], multi=True),
        
    html.Br(),
    
    html.Label('Slider'),
    
    dcc.Slider(min=0,
               max=9,
               marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
               value=5,),
    
    html.H3(children='Headline: Level 3 Size'),

    html.H4(children='Headline: Level 4 Size'),
    
    html.H5(children='Headline: Level 5 Size')
])

@app.callback(
    Output("table-color", "color"), Input("change-table-color", "value") 
)
def change_table_colour(color):
    return color

if __name__ == "__main__":
    app.run_server(debug=True)
