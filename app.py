from dash import Dash, dcc, Output, Input, html, dash_table
import dash_bootstrap_components as dbc
from dash import Dash, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import file
# file_name = "train.csv"
# df = pd.read_csv(file_name)

# initialize the application with theme
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
server = app.server

# revised figure 1
x = {
    "Region": ["Central", "East", "South", "West"],
    "Sales": [492646, 669518, 389151, 710219],
}

df_x = pd.DataFrame(x)
fig1 = px.bar(df_x, x="Region", y="Sales")
fig2 = px.line(df_x, x="Region", y="Sales")


# Doing Figure 1
# example = df[["State", "Sales"]]
# example_sales = df[["State", "Sales"]].groupby("State").sum()
# fig1 = px.bar(example_sales, title="Long-Form Input")


# Doing figure 2
# df_region = df.groupby("Region").sum()
# df_region = df_region.drop(["Postal Code"], axis=1)
# df_region = df[["Region", "Sales"]].groupby("Region").sum()
# df_region.head()
# fig2 = px.line(df_region)

# Doing Figure 3
# df_categories = df.groupby("Category").sum()
# df_categories = df_categories.drop(["Postal Code"], axis=1)
# fig3 = px.bar(df_categories)


app.layout = html.Div(
    [
        # Graph 1
        html.Div([dcc.Graph(id="graph1", figure=fig1)]),
        # Graph 2
        html.Div([dcc.Graph(id="graph2", figure=fig2)]),
        # # Graph 3
        # html.Div([dcc.Graph(id="graph3", figure=fig3)]),
    ]
)

# html.Div([
#     dcc.Graph(id ='graph2', figure= fig2)
# ])


if __name__ == "__main__":
    app.run_server(debug=True)
