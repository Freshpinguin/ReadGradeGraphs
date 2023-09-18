import pandas as pd
from dash import Dash, html
from src.components import bar_chart


def create_layout(app: Dash, df: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            bar_chart.render(app, df)
        ]

    )