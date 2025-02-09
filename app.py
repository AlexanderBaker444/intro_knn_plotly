import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='knn'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Nats'),
    html.Div([
        html.H6('Sepal Length'),
        dcc.Slider(id='slider-1',min=1,max=8,step=0.1,marks={i:str(i) for i in range(1,9)}),
        html.H6('Sepal Width'),
        dcc.Slider(id='slider-2',min=1,max=8,step=0.1,marks={i:str(i) for i in range(1,9)}),
        html.Br(),
        dcc.Dropdown(id='k-drop',options=[{'label':5,'value':5},{'label':10,'value':10},{'label':15,'value':15},{'label':20,'value':20},{'label':25,'value':25}],value=5)
            ]),
    html.Div(id='output-message',children=''),
    html.Br(),
    html.A('Code on Github', href='https://github.com/austinlasseter/knn_iris_plotly'),
])

@app.callback(Output('output-message','children'),[Input('k-drop','value'),Input('slider-1','value'),Input('slider-2','value')])

def my_funky_function(k,value0,value1):
    file=open(f'resources/model_k{k}.pkl','rb')
    model=pickle.load(file)
    file.close()
    new_obs=[[value0,value1]]
    my_prediction=model.predict(new_obs)
    return (f'you chose {k} and {new_obs} predicted {my_prediction}')
############ Execute the app
if __name__ == '__main__':
    app.run_server()
