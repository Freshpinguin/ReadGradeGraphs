from pydantic import BaseModel, Field
from typing import Dict
from strenum import StrEnum
from bs4.element import Tag
import json


class Semester(BaseModel):
    name: str
    value: float

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value


class Exam(BaseModel):
    lecture: str
    semester: Semester
    all_grades: int

class gradedExam(Exam):
    grade_numbers: Dict[str, int]
    mean_value: float
    standard_deviation: float

class passedExam(Exam):
    passed: int
    not_passed: int


class ExamFactory:


    @staticmethod
    def semester_from_title(title: str) -> Semester:
        year = float(title.split(' ')[-1].split('/')[0]) + (0.5 if len(title.split(' ')[-1].split('/')  ) == 2 else 0 )
        semester = Semester(name=title.split(' ')[-2],value=year)

        return semester

    @staticmethod
    def exam_from_div(div:Tag) -> Exam:
        bar_charts = json.loads(div['data-barcharts'])['barCharts']
        if len(bar_charts) ==0:
            return None
        
        
        if bar_charts[0]['barChartTitle'] == 'Bewertungsart Komma-Noten':
            bar_chart= bar_charts[0]
            x_axis = bar_chart['xAxis']
            y_axis = bar_chart['yAxis']

            
            grades = {entry[0]:entry[1] for entry in zip(x_axis,y_axis)}
            mean_value = bar_chart['meanValue']
            standard_deviation = bar_chart['standardDeviation']
            all_grades = bar_chart['allN']
            title = bar_chart['unitTitle']
            lecture = " ".join(title.split(' ')[2:-2])
            semester = ExamFactory.semester_from_title(title=title)
            return gradedExam(
                lecture=lecture,
                semester=semester,
                all_grades=all_grades,
                grade_numbers=grades,
                mean_value=mean_value,
                standard_deviation=standard_deviation
            )

        if bar_charts[0]['barChartTitle'] == 'Bewertungsart mit/ohne Erfolg':
            bar_chart= bar_charts[0]
            y_axis = bar_chart['yAxis']
            title = bar_chart['unitTitle']
            lecture = " ".join(title.split(' ')[2:-2])
            semester = ExamFactory.semester_from_title(title=title)
            all_grades = bar_chart['allN']
            if len(y_axis) != 2:
                return passedExam(
                lecture=lecture,
                semester=semester,
                all_grades=all_grades,
                passed = y_axis[0],
                not_passed= 0,
            )
            return passedExam(
                lecture=lecture,
                semester=semester,
                all_grades=all_grades,
                passed = y_axis[0],
                not_passed= y_axis[1],
            )

