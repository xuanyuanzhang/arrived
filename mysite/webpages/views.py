from django.shortcuts import render, render_to_response
from django.template import RequestContext
import scraper2
from bs4 import BeautifulSoup
import os
from django.core.mail import send_mail
from webpages.forms import ContactForm
from django.http import HttpResponseRedirect, HttpRequest
from django.conf import settings
from ipware.ip import get_ip
import geocoder

import requests
import json
from urllib2 import urlopen
import socket


def getUserInfo():
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    print type(response)
    print "response is: " + str(response)
    data = json.load(response)

    IP = data['ip']
    city = data['city']
    country = data['country']
    region = data['region']

    content = []
    # content.append(IP)
    content.append(city)
    content.append(region)
    content.append(country)

    return content


def index(request):
    # ip = get_client_ip(request)

    # urlFoLaction = "http://www.freegeoip.net/json/{0}".format(get_client_ip(request))
    # locationInfo = json.loads(urlopen(urlFoLaction).read())
    #
    # client_info.append(locationInfo['city'])
    # # client_info.append(locationInfo['region'])
    # client_info.append(locationInfo['country_name'])
    g = geocoder.ip(get_client_ip(request))
    location = g.city + ", " + g.state + ", " + g.country
    # location = client_info[0] + ", " + client_info[1]

    if request.method == 'POST':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "127.0.0.1"
        port = "10003"
        s.connect((host, int(port)))
        text = request.POST["textfield"]
        s.send(text)
        data = s.recv(2048)
        print "data is: " + data
        s.close()
        return render(request, 'index.html', {"location": location, "text": data})
    return render(request, 'index.html', {"location": location})


def watch(request):
    return render_to_response('watch.html')


def learn(request):
    table = []
    homepage = scraper2.get_homepage()
    visa = scraper2.get_visaHelp_QnA()
    table.append(["Visa_Help", visa])
    career = scraper2.get_careerGuidance_QnA()
    table.append(["Job_Assistance", career])
    legal = scraper2.get_legalHelp_QnA()
    table.append(["Legal_Section", legal])
    deportation = scraper2.get_deportationHelp_QnA()
    table.append(["Deportation_Help", deportation])
    driving = scraper2.get_driving_QnA()
    table.append(["Driving", driving])
    english = scraper2.get_englishHelp_QnA()
    table.append(["Education", english])
    faq = scraper2.get_faq_QnA()
    table.append(["FAQ", faq])
    financial = scraper2.get_financial_QnA()
    table.append(["Financial_Advice", financial])
    housing = scraper2.get_housing_QnA()
    table.append(["Housing", housing])
    mexican = scraper2.get_mexicanNational_QnA()
    table.append(["Mexican_Nationals", mexican])
    support = scraper2.get_supportGroups_QnA()
    table.append(["Support_Groups", support])
    immigration = scraper2.get_immigrationReform_QnA()
    table.append(["Immigration_Reform-DACA-Trump_Plans_2017", immigration])
    emergency = scraper2.get_emergency_QnA()
    table.append(["Emergency", emergency])
    health = scraper2.get_health_QnA()
    table.append(["Health_Knowledge", health])
    return render(request, 'learn.html', {'homepage': homepage, 'table': table})


def see(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/resource/ngos_final.kml')
    inputfile = file_path
    index = 0
    with open(inputfile, 'r') as f:
        soup = BeautifulSoup(f, "html5lib")
        table = []
        for node in soup.findAll('placemark'):
            coordinate = []
            col1 = node.find('name')
            thestrings = [unicode(s) for s in col1.findAll(text=True)]
            thetext1 = ''.join(thestrings)
            col2 = node.find('description')
            thestrings = [unicode(s) for s in col2.findAll(text=True)]
            thetext2 = ''.join(thestrings)
            col3 = node.find('styleurl')
            thestrings = [unicode(s) for s in col3.findAll(text=True)]
            thetext3 = ''.join(thestrings)
            col4 = node.find('coordinates')
            thestrings = [unicode(s) for s in col4.findAll(text=True)]
            thetext4 = ''.join(thestrings)

            for x in thetext4.split(','):
                coordinate.append(float(x))
            table.append((thetext1, thetext2, thetext3, coordinate, index))
            index += 1
    return render(request, 'see.html', {'table':table})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            from_email=settings.EMAIL_HOST_USER
            send_mail(
                cd['subject'],
                cd['message'],
                from_email,
                ['530310387@qq.com'],
                fail_silently=False
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})


def chat(request):
    return render(request, 'chat.html')


def get_client_ip(request):
    ip = get_ip(request)
    return ip


# def client_question(input):
