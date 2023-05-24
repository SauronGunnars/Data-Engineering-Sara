
import plotly_express as px 
import numpy as np
from dash import Dash, dcc 
from dash.html import H1, Div, P, H2

dropdown_options = [{"label": f"{rolls} rolls", "value":rolls } for rolls in [10,100,1000,10000]]

app = Dash(__name__)

app.layout = Div([
    H1("Dice simulator"),
    P("Choose number of  dices and number of rolls"),
    H2("Number of rolls"),
    dcc.Dropdown(id = "number-rolls", options= dropdown_options)
])

if __name__ == "__main__":
    print('Hello from the docker side\n')

    app.run_server(debug=True)


    
