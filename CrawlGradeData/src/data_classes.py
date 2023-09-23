from pydantic import BaseModel, Field
from typing import Dict, List
from strenum import StrEnum
from bs4.element import Tag
import json
import csv
import os.path


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
    exam_nr: str

    def headers(self) -> List[str]:
        return ['lecture','semester','nGrades','exam_nr']
    
    def values(self) -> List:
        return [self.lecture, self.semester.value, self.all_grades, self.exam_nr]
    
    def write_to_csv(self, path:str) -> None:

        file_exists = os.path.isfile(path)

        with open(path, 'a', encoding='UTF8') as f:
        
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(self.headers())

            writer.writerow(self.values())


class gradedExam(Exam):
    grade_numbers: Dict[str, int]
    mean_value: float
    standard_deviation: float

    def headers(self) -> List[str]:
        return super().headers() + list(self.grade_numbers.keys()) + ["mean_value"] + ["standard_deviation"]
    
    def values(self) -> List:
        return super().values() + list(self.grade_numbers.values()) + [self.mean_value] + [self.standard_deviation]
    
    def write_to_csv(self, path: str) -> None:
        return super().write_to_csv(path+"graded.csv")

class passedExam(Exam):
    passed: int
    not_passed: int

    def headers(self) -> List[str]:
        return super().headers() + ["passed", "not_passed"]
    
    def values(self) -> List:
        return super().values() + [self.passed, self.not_passed]
    
    def write_to_csv(self, path: str) -> None:
        return super().write_to_csv(path+"passed.csv")
    


class ExamFactory:
    @staticmethod
    def semester_from_title(title: str) -> Semester:
        year = float(title.split(' ')[-1].split('/')[0]) + (0.5 if len(title.split(' ')[-1].split('/')  ) == 2 else 0 )
        semester = Semester(name=title.split(' ')[-2],value=year)

        return semester

    @staticmethod
    def exam_from_div(div:Tag, exam_nr: str) -> Exam:
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
                exam_nr = exam_nr,
                all_grades=all_grades,
                grade_numbers=grades,
                mean_value=mean_value,
                standard_deviation=standard_deviation
            )

        if bar_charts[0]['barChartTitle'] == 'Bewertungsart mit/ohne Erfolg':
            bar_chart= bar_charts[0]

            x_axis = bar_chart['xAxis']
            y_axis = bar_chart['yAxis']
            title = bar_chart['unitTitle']
            lecture = " ".join(title.split(' ')[2:-2])
            semester = ExamFactory.semester_from_title(title=title)
            all_grades = bar_chart['allN']
            if len(y_axis) != 2 and x_axis==['BE']:
                passed = y_axis[0]
                not_passed = 0
            else:
                if len(y_axis) != 2 and x_axis==['NB']:
                    passed = 0
                    not_passed = y_axis[0]
                else:
                    passed = y_axis[0]
                    not_passed= y_axis[1]
            
            return passedExam(
                lecture=lecture,
                semester=semester,
                exam_nr= exam_nr,
                all_grades=all_grades,
                passed = passed,
                not_passed= not_passed,
            )

