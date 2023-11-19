from src.request_classes import AuthRequest, OpenGradeViewRequest, ExpandGradesRequest, GetGradesRequest
from src.data_classes import ExamFactory
import requests

USERNAME = 'username'
PASSWORD = 'password'
PATH_TO_CSVS = "data/exams_test"



session = requests.Session()
auth = AuthRequest(username=USERNAME, password=PASSWORD, session=session)
opengrades = OpenGradeViewRequest(session = session)
expandgrades = ExpandGradesRequest(session = session)
getgrades = GetGradesRequest(session = session)

auth()
opengrades()
expandgrades()
specifiers = expandgrades.get_specifiers()
exam_nrs = expandgrades.get_exam_numbers(specifiers)


for spec, exam_nr in zip(specifiers,exam_nrs):
    getgrades(spec)
    exam = ExamFactory.exam_from_div(getgrades.get_data(), exam_nr=exam_nr)
    if exam is None:
        continue
    exam.write_to_csv(PATH_TO_CSVS)
