import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchemaGraded
from . import ids

def render(app: Dash, df: pd.DataFrame) -> html.Div:
    # @app.callback(
    #     Output(ids.BAR_CHART, "children"),
    #     Input(ids.BAR_CHART, "value")
    # )
    # def update_bar_chart() -> html.Div:

    #     return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    df = df.sort_values("semester")

    df = df.assign(
        semester = df['semester'].apply(lambda x: x.name)
    )
    fig = px.bar(
        df,
        x= DataSchemaGraded.SEMESTER,
        y=DataSchemaGraded.MEAN,
        color=DataSchemaGraded.VORLESUNG
    )
    
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)