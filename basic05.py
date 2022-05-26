'''
Created on May 24, 2022

@author: Jim Yin
'''

# Run this app with `python basic05.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = px.data.gapminder()
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

data2 = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
fig2 = px.funnel(data2, x='number', y='stage')

df3 = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df3.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig3 = px.pie(df3, values='pop', names='country', title='Population of European continent')

df4 = px.data.carshare()
fig4 = px.scatter_mapbox(df4, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

     html.Div(children='''
        Dash: A web application framework for your data.
    '''),
     

    dcc.Graph(
        id='example-graph01',
        figure=fig),
        
    html.Div(children='''
        Dash: An example of a funnel chart.
    '''),

    dcc.Graph(
        id='example-graph02',
        figure=fig2),
        
    html.Div(children='''
        Dash: An example of a pie chart.
    '''),

    dcc.Graph(
        id='example-graph03',
        figure=fig3),
        
    html.Div(children='''
        Dash: An example of a pie chart.
    '''),

    dcc.Graph(
        id='example-graph04',
        figure=fig4
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)