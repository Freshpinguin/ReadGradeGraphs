from typing import Dict

class AuthParams:
    HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://studium.ohmportal.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces',
    'Origin': 'https://studium.ohmportal.de',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    }
    PARAMS = {
    'state': 'user',
    'type': '1',
    'category': 'auth.login',
    }

    def DATA(username: str, password: str)-> Dict[str,str]:
        return {
        'userInfo': '',
        'asdf': username,
        'fdsa': password,
        'submit': '',
        }
    
class ExpandParams:
    HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Referer': 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml?_flowId=examsOverviewForPerson-flow&_flowExecutionKey=e1s1',
    'Faces-Request': 'partial/ajax',
    'Origin': 'https://studium.ohmportal.de',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    }
    
    PARAMS = {
    '_flowId': 'examsOverviewForPerson-flow',
    '_flowExecutionKey': 'e1s1',
    }
    
    DATA = {
    'activePageElementId': '',
    'refreshButtonClickedId': '',
    'navigationPosition': 'hisinoneMeinStudium,examAssessmentForStudent',
    'autoScroll': '',
    'examsReadonly:overviewAsTreeReadonly:collapsiblePanelCollapsedState': 'false',
    'examsReadonly:degreeProgramProgressForReportAsTree:collapsiblePanelCollapsedState': 'true',
    'examsReadonly_SUBMIT': '1',
    'javax.faces.ViewState': 'e1s1',
    'javax.faces.behavior.event': 'action',
    'javax.faces.partial.event': 'click',
    'javax.faces.source': 'examsReadonly:overviewAsTreeReadonly:tree:expandAll2',
    'javax.faces.partial.ajax': 'true',
    'javax.faces.partial.execute': 'examsReadonly:overviewAsTreeReadonly:tree:expandAll2',
    'javax.faces.partial.render': 'examsReadonly:overviewAsTreeReadonly:tree:expandAll2 examsReadonly:overviewAsTreeReadonly:tree:ExamOverviewForPersonTreeReadonly examsReadonly:overviewAsTreeReadonly:tree:collapseAll2 examsReadonly:messages-infobox',
    'examsReadonly': 'examsReadonly',
    }
    
class GetGradesParams:
    HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Referer': 'https://studium.ohmportal.de/qisserver/pages/sul/examAssessment/personExamsReadonly.xhtml?_flowId=examsOverviewForPerson-flow&_flowExecutionKey=e1s1',
    'Faces-Request': 'partial/ajax',
    'Origin': 'https://studium.ohmportal.de',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    }

    PARAMS = {
    '_flowId': 'examsOverviewForPerson-flow',
    '_flowExecutionKey': 'e1s1',
    }
    
    def DATA(specifier: str = 'examsReadonly:overviewAsTreeReadonly:tree:ExamOverviewForPersonTreeReadonly:0:1:0:0:0:5:1:j_id_4h_2g_4h_1_15_w_2_2_2_2_1:openGraph') -> Dict[str,str]:
        return {
    'activePageElementId': '',
    'refreshButtonClickedId': '',
    'navigationPosition': '',
    'autoScroll': '',
    'examsReadonly:overviewAsTreeReadonly:collapsiblePanelCollapsedState': 'false',
    'examsReadonly:degreeProgramProgressForReportAsTree:collapsiblePanelCollapsedState': 'true',
    'examsReadonly_SUBMIT': '1',
    'javax.faces.ViewState': 'e1s1',
    'javax.faces.behavior.event': 'action',
    'javax.faces.partial.event': 'click',
    'javax.faces.source': specifier,
    'javax.faces.partial.ajax': 'true',
    'javax.faces.partial.execute': specifier,
    'javax.faces.partial.render': 'examsReadonly:overlays examsReadonly:messages-infobox',
    'examsReadonly': 'examsReadonly',
    }