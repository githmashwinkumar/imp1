import openpyxl
from pdfquery import PDFQuery
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.high_level import extract_pages, extract_text
import re
import os

class LabDataObject(object):
    def __init__(self):
        self.dateoftest = ''
        self.labResult = ''

dir = 'D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar'
files = os.listdir(dir)
index = 0

c1 = 0
results = []
labresults = []

for file in files:
    text = extract_text(dir + '\\' + file )
    reportType = "Only HBA1C"
        #file[0:10]
    #print(reportType)
    reportType1 = file[0:14]
    l = LabDataObject()
    if reportType == "Only HBA1C":
        c1 = 0
        date = ''
        for t in text.split('\n'):
            #print(t + ' - ' + str(c1) )
            if c1 == 52:
                date = t.strip()
                c1 += 1
                l.dateoftest = date
                results.append(date)
                #print(t.strip())
                #print( ' t.strip() + ' + t.strip())
            elif c1 == 77:
                l.labResult = t.strip()
                c1 += 1
            else:
                c1 += 1
        labresults.append(l)
    elif reportType == "Complete Blood":
        d1 = 0
        date1 = ''
        for t in text.split('\n'):
            if d1 == 52:
                # print(d1)
                # print(t.strip())
                date1 = t.strip()
                d1 += 1
                l.dateoftest = date1
                results.append(date1)
            elif d1 == 934:
                l.labResult = t.strip()
                d1 += 1
            else:
                d1 += 1
        labresults.append(l)

for e in labresults:
    print(e.dateoftest)
    print(e.labResult)

for key in results:
    print(key)
