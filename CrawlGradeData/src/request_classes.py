from typing import List
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import requests
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning, module='bs4')
from src.request_params import AuthParams, ExpandParams, GetGradesParams

class AuthRequest:
    """
    Class contains code for doing authentification on ohmportal page.
    """
    def __init__(self, username: str, password: str, session: requests.Session):
        self.username = username
        self.password = password
        self.session = session
        self.url = 'https://studium.ohmportal.de/qisserver/rds'
        
    def __call__(self) -> requests.Response:
        resp = self.session.post(self.url, params=AuthParams.PARAMS, headers=AuthParams.HEADERS, data=AuthParams.DATA(username=self.username, password=self.password))

        failed = "Ihre Anmeldung war leider nicht erfolgreich. Bitte versuchen Sie es noch einmal und prüfen Sie die Benutzerkennung und das Passwort"

        if failed in resp.text:
            raise Exception("Authentification failed. Try with correct credentials.")


        return resp

class OpenGradeViewRequest:
    """
    Class contains request to visit grade view on ohmportal. Necessary to get statistiks data afterwards.
    """
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = "https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml?_flowId=examsOverviewForPerson-flow&_flowExecutionKey=e1s1"
        
    def __call__(self) -> requests.Response:
        return self.session.get(self.url)
    
class ExpandGradesRequest:
    """
    Class contains requestexpand grade view on ohmportal. Necessary to get statistiks data afterwards.
    Also provides specifiers and numbers to acess the data for single exams afterwards.
    """
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = 	"https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml?_flowId=examsOverviewForPerson-flow&_flowExecutionKey=e1s1"

        # 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml'
    
   
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
        """
        Get specifier for every single existing exam, necessary to query the data afterwards.
        """
        soup = BeautifulSoup(self.resp_text,features="lxml")
        buttons = soup.findAll(lambda tag: tag.name=="button" and tag['title'] == "Notenverteilung anzeigen")
        return [button['id'] for button in buttons]
    
    def get_exam_numbers(self, specifiers: List[str]) -> List[str]:
        """
        Get exam numbers for every specifiers. 
        """
        soup = BeautifulSoup(self.resp_text,features="lxml")
        specifiers = [":".join(spec.split(":")[4:-2]) for spec in specifiers]
        find_func = lambda spec, tag: tag.name=="span" and  tag.has_attr('id') and "elementnr" in tag['id'] and spec in tag['id']
        divs = [soup.find(lambda tag: find_func(spec, tag)).text for spec in specifiers]
        return divs
    

class GetGradesRequest:
    """
    Class to query the data for a single exam and extracts the div containting the data.
    """
    def __init__(self, session: requests.Session):
        self.session = session
        self.url = 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml'

    def __call__(self, specifier: str) -> requests.Response:
        resp = self.session.post(self.url, headers=GetGradesParams.HEADERS, params=GetGradesParams.PARAMS, data=GetGradesParams.DATA(specifier=specifier))
        self.resp_text = resp.text
        return resp
    
    def get_data(self) -> list:
        """
        Extracts the div cotaining statistics data.
        """
        soup = BeautifulSoup(self.resp_text, features="lxml")
        return soup.findAll(lambda tag: tag.name=="div" and tag.has_attr('id') and  tag['id']=="graphPlaceholder")[0]
    
    