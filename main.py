from src.request_classes import AuthRequest, OpenGradeViewRequest, ExpandGradesRequest, GetGradesRequest
import requests

session = requests.Session()
auth = AuthRequest(username='username', password='password', session=session)
opengrades = OpenGradeViewRequest(session = session)
expandgrades = ExpandGradesRequest(session = session)
getgrades = GetGradesRequest(session = session)

auth()
opengrades()
expandgrades()

getgrades()

print(getgrades.get_data())