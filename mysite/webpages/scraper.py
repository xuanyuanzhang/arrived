from bs4 import BeautifulSoup
import sys, os, codecs

inputfile = "static/resource/ngos_final.kml"
with open(inputfile, 'r') as f:
    soup = BeautifulSoup(f,"html5lib")
    table = []
    for node in soup.findAll('placemark'):
        col1 = node.find('name')
        thestrings = [unicode(s) for s in col1.findAll(text=True)]
        thetext1 = ''.join(thestrings)
        #thetext1.decode().encode('utf-8')
        col2 = node.find('description')
        thestrings = [unicode(s) for s in col2.findAll(text=True)]
        thetext2 = ''.join(thestrings)
        #thetext2.decode().encode('utf-8')
        col3 = node.find('styleurl')
        thestrings = [unicode(s) for s in col3.findAll(text=True)]
        thetext3 = ''.join(thestrings)
        #thetext3.decode().encode('utf-8')
        col4 = node.find('coordinates')
        thestrings = [unicode(s) for s in col4.findAll(text=True)]
        thetext4 = ''.join(thestrings)
        #thetext4.decode().encode('utf-8')
        table.append([thetext1,thetext2,thetext3,thetext4])
        #table.append([col1, col2, col3, col4])
    for ele in table:
        print(ele[0].encode('utf-8').strip())
        print(ele[1].encode('utf-8').strip())
        print(ele[2].encode('utf-8').strip())
        print(ele[3].encode('utf-8').strip())
