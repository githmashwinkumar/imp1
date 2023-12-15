import openpyxl
from pdfquery import PDFQuery
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.high_level import extract_pages, extract_text
import re
import os

class LabDataObject(object):
    def __init__(self,dateoftest,labResult):
        self.dateoftest = dateoftest
        self.labResult = labResult

    def setDateoftest(self,dateoftest): self.dateoftest = dateoftest
    def setlabResult(self,labresult): self.labResult = labresult

    def getDateoftest(self): return self.dateoftest
    def getLabresult(self): return  self.labResult

dir = 'D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar'
files = os.listdir(dir)
index = 0

c1 = 0
results = []
labresults = []

for file in files:
    text = extract_text(dir + '\\' + file )
    reportType = "Only HBA1C"
    reportType1 = file[0:14]
    l = LabDataObject("","")
    if reportType == "Only HBA1C":
        c1 = 0
        date = ''
        for t in text.split('\n'):
            if c1 == 52:
                date = t.strip()
                c1 += 1
                #l.dateoftest = date
                l.setDateoftest(date)
                results.append(date)
                #labresults[date] = date
                    #= date
            elif c1 == 77:
                #l.labResult = t.strip()
                l.setlabResult(t.strip())
                c1 += 1
                #labresults[date].__add__(l)
            else:
                c1 += 1
        labresults.append(l)

for o in labresults:
    print(o.dateoftest)
    print(o.labResult)

for r in results:
    print(r)
    d = r



