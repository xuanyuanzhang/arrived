from django.shortcuts import render
import scraper2
from bs4 import BeautifulSoup
import os
from django.core.mail import send_mail
from webpages.forms import ContactForm
from django.http import HttpResponseRedirect
from django.conf import settings

def index(request):
    return render(request, 'index.html')


def watch(request):
    return render(request, 'watch.html')


def learn(request):
    table = []
    homepage = scraper2.get_homepage()
    visa = scraper2.get_visaHelp_QnA()
    table.append(["Visa Help", visa])
    career = scraper2.get_careerGuidance_QnA()
    table.append(["Job Assistance", career])
    legal = scraper2.get_legalHelp_QnA()
    table.append(["Legal Section", legal])
    deportation = scraper2.get_deportationHelp_QnA()
    table.append(["Deportation Help", deportation])
    driving = scraper2.get_driving_QnA()
    table.append(["Driving", driving])
    english = scraper2.get_englishHelp_QnA()
    table.append(["Education", english])
    faq = scraper2.get_faq_QnA()
    table.append(["FAQ", faq])
    financial = scraper2.get_financial_QnA()
    table.append(["Financial Advice", financial])
    housing = scraper2.get_housing_QnA()
    table.append(["Housing", housing])
    mexican = scraper2.get_mexicanNational_QnA()
    table.append(["Mexican Nationals", mexican])
    support = scraper2.get_supportGroups_QnA()
    table.append(["Support Groups", support])
    immigration = scraper2.get_immigrationReform_QnA()
    table.append(["Immigration Reform/DACA/Trump Plans 2017", immigration])
    print table
    return render(request, 'learn.html', {'homepage': homepage, 'table': table})
    # return render(request, 'learn.html',
    #               {'table':homepage, 'visaHelp':visa, 'housing':housing,
    #                'careerGuidance':career, 'legalHelp':legal,
    #                'deportationHelp':deportation, 'driving':driving,
    #                'englishHelp':english, 'faq':faq, 'financial':financial,
    #                'mexicanNational':mexican, 'supportGroups':support,
    #                'immigrationReform':immigration})


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
            cd = form.cleaned_data
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                cd['subject'],
                cd['message'],
                from_email,
                ['530310387@qq.com'],
                fail_silently= False
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})
