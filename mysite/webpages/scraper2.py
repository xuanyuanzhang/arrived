import xml.etree.ElementTree
import re
from bs4 import BeautifulSoup
import sys, os, codecs
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'static/resource/strings.xml')
inputfile = file_path
with open(inputfile, 'r') as f:
    soup = BeautifulSoup(f,"html5lib")
    table = []

def get_about():
    about = soup.find(attrs={"name" : re.compile("^AboutUs")})
    email = soup.find(attrs={"mailto"})
    return about

def get_homepage():
    homepage = []
    for node in soup.findAll(attrs={"name" : re.compile("^homepage")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        homepage.append(''.join(thestrings))
    return homepage

def get_visaHelp_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^visaHelpQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^visaHelpAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"visaHelp"+str(i)])
    return q_a_tuple;

def get_housing_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^housingQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^housingAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"housing"+str(i)])
    return q_a_tuple;

def get_careerGuidance_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^careerGuidanceQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^careerGuidanceAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"careerGuidance"+str(i)])
    return q_a_tuple;

def get_legalHelp_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^legalHelpQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^legalHelpAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"legalHelp"+str(i)])
    return q_a_tuple;

def get_deportationHelp_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^deportationHelpQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^deportationHelpAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"deportationHelp"+str(i)])
    return q_a_tuple;

def get_englishHelp_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^englishHelpQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^englishHelpAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i],a[i],"englishHelp"+str(i)])
    return q_a_tuple

def get_supportGroups_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^supportGroupsQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^supportGroupsAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"supportGroups"+str(i)])
    return q_a_tuple

def get_faq_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^faqQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^faqAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"faq"+str(i)])
    return q_a_tuple

def get_driving_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^drivingQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^drivingAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"driving"+str(i)])
    return q_a_tuple;

def get_financial_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^financialQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^financialAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"financial"+str(i)])
    return q_a_tuple;

def get_mexicanNational_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^mexicanNationalQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^mexicanNationalAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"mexicanNational"+str(i)])
    return q_a_tuple;

def get_immigrationReform_QnA():
    q = []
    a = []
    q_a_tuple = []
    for node in soup.findAll(attrs={"name": re.compile("^immigrationReformQuestion")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        q.append(''.join(thestrings))
    for node in soup.findAll(attrs={"name": re.compile("^immigrationReformAnswer")}):
        thestrings = [unicode(s) for s in node.findAll(text=True)]
        a.append(''.join(thestrings))
    for i in range(len(q)):
        q_a_tuple.append([q[i], a[i],"immigrationReform"+str(i)])
    return q_a_tuple;
