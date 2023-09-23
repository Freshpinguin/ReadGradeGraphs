import pandas as pd
from enum import StrEnum
from math import floor
from functools import total_ordering
    

class DataSchemaGraded(StrEnum):
    VORLESUNG = "lecture"
    SEMESTER = "semester"
    ANZAHL = "nGrades"
    EXAM_NR = "exam_nr"
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
    DURCHFALL = "durchfall_quote"


@total_ordering
class TestClass():
    def __init__(self, value: float):
        self.value = value
        self.name = map_semester(value)
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    

def map_semester(semester: float) -> str:
    if semester % 1 == 0.5:
        return f"WiSe {floor(semester)}"
    else:
        return f"SoSe {floor(semester)}"



def load_grades_exams_data(path : str) -> pd.DataFrame:

    df = pd.read_csv(path)
    df = df.assign(
        semester = df[DataSchemaGraded.SEMESTER].apply(lambda x: TestClass(x)),
        durchfall_quote = df.apply(lambda x: x[DataSchemaGraded.FÜNF]/x[DataSchemaGraded.ANZAHL], axis=1)
    )
    return df
