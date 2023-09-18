import pandas as pd
from enum import StrEnum

class DataSchemaGraded(StrEnum):
    VORLESUNG = "lecture"
    SEMESTER = "semester"
    ANZAHL = "nGrades"
    EINSNULL = "1,00"
    EINSDREI = "1,30"
    EINSSIEBEN = "1,70"
    ZWEINULL = "2,00"
    ZWEIDREI = "2,30"
    ZWEISIEBEN = "2,70"
    DREINULL = "3,00"
    DREIDREIL = "3,30"
    DREISIEBEN = "3,70"
    VIERNULL = "4,00"
    FÜNF = "5,00"
    MEAN = "mean_value"
    STRDEV = "standard_deviation"

def load_grades_exams_data(path : str) -> pd.DataFrame:

    df = pd.read_csv(path)

    return df
