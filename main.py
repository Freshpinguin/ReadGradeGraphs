from src.request_classes import AuthRequest, OpenGradeViewRequest, ExpandGradesRequest, GetGradesRequest
from src.data_classes import ExamFactory
import requests



session = requests.Session()
auth = AuthRequest(username='username', password='password', session=session)
opengrades = OpenGradeViewRequest(session = session)
expandgrades = ExpandGradesRequest(session = session)
getgrades = GetGradesRequest(session = session)

auth()
opengrades()
expandgrades()
specifiers = expandgrades.get_specifiers()

for spec in specifiers:
    getgrades(spec)
    exam = ExamFactory.exam_from_div(getgrades.get_data())
    if exam is None:
        continue
    exam.write_to_csv("exams")
