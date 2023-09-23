from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_grades_exams_data

DATA_PATH = "./data/examsgraded.csv"

def main() -> None:
    
    df = load_grades_exams_data(DATA_PATH)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.layout = create_layout(app, df)
    app.run()

if __name__ == "__main__":
    main()