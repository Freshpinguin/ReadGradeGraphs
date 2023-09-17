from typing import List
import lxml
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import requests
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning, module='bs4')
from src.request_params import AuthParams, ExpandParams, GetGradesParams

class AuthRequest:
    def __init__(self, username: str, password: str, session: requests.Session):
        self.username = username
        self.password = password
        self.session = session
        self.url = 'https://studium.ohmportal.de/qisserver/rds'
        
    def __call__(self) -> requests.Response:
        return self.session.post(self.url, params=AuthParams.PARAMS, headers=AuthParams.HEADERS, data=AuthParams.DATA(username=self.username, password=self.password))
    

class OpenGradeViewRequest:
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = "https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml?_flowId=examsOverviewForPerson-flow&_flowExecutionKey=e1s1"
        
    def __call__(self) -> requests.Response:
        return self.session.get(self.url)
    
class ExpandGradesRequest:
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml'
    
    def __call__(self) -> requests.Response:
        resp = self.session.post(
        self.url,
        params=ExpandParams.PARAMS,
        headers=ExpandParams.HEADERS,
        data=ExpandParams.DATA,
        )

        self.resp_text = resp.text
        return resp
    
    def get_specifiers(self) -> List[str]:

        soup = BeautifulSoup(self.resp_text,features="lxml")
        buttons = soup.findAll(lambda tag: tag.name=="button" and tag['title'] == "Klassenspiegel anzeigen")
        return [button['id'] for button in buttons]

class GetGradesRequest:
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml'

    def __call__(self, specifier: str) -> requests.Response:
        resp = self.session.post(self.url, headers=GetGradesParams.HEADERS, params=GetGradesParams.PARAMS, data=GetGradesParams.DATA(specifier=specifier))
        self.resp_text =resp.text
        return resp
    
    def get_data(self) -> list:
        soup = BeautifulSoup(self.resp_text, features="lxml")
        return soup.findAll(lambda tag: tag.name=="div" and tag.has_attr('id') and  tag['id']=="graphPlaceholder")
    
    