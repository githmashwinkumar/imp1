import openpyxl
from pdfquery import PDFQuery
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.high_level import extract_pages, extract_text
import re
import os

#text = extract_text('D:\\Newfolder\\Per\\Healthview\\Reports\\49_61539409_0_1.pdf')
#text1 = extract_text('D:\\Newfolder\\Per\\Healthview\\Reports\\MED120473722_49_61451353 (1).pdf')

dir = 'D:\\Newfolder\\Per\\Healthview\\Reports'
files = os.listdir(dir)
index = 0

c1 = 0
results = {'HBA1C': []}

for file in files:
    text = extract_text(dir + '\\' + file )
    reportType = file[0:10]
    #print(reportType)
    reportType1 = file[0:14]
    #print(reportType1)
    #print(reportType)
    #print(file)
    if reportType == "Only HBA1C":
        #results = {'HBA1C':[]}
        #print(reportType)
        c1 = 0
        date = ''
        for t in text.split('\n'):
            #print(t + ' - ' + str(c1) )
            if c1 == 52:
                date = t.strip()
                c1 += 1
                #print(t.strip())
                #print( ' t.strip() + ' + t.strip())
            elif c1 == 77:
                #results['HBA1C'] += t.strip()
                results['HBA1C'].append(date)
                #results['HBA1C'].append(t.strip())
                results['HBA1C'].append(t.strip())
                #print(t.strip())
                #print(results)
                c1 += 1
               # print(c1)
            else:
                c1 += 1
    elif reportType1 == "Complete Blood":
        #print(reportType1)
        #results = {'HBA1C': []}
        d1 = 0
        date1 = ''
        for t in text.split('\n'):
            #print(t + ' - ' + str(d1) )
            #print(d1)
            if d1 == 52:
                #print(d1)
                #print(t.strip())
                date1 = t.strip()
                d1 += 1
            elif d1 == 934:
                #results['HBA1C'] += t.strip()
                results['HBA1C'].append(date1)
                #results['HBA1C'].append(t.strip())
                results['HBA1C'].append(t.strip())
                #print(results)
                #print(t.strip())
                d1 += 1
            else:
                #print(d1)
                d1 += 1
            #d1 += 1
print(results)

            #print(t)
            #print(c1)
            #c1 += 1

    #c1 =0


    #HbA1C
#pattern = re.compile(r"[HbA1C]")
#matches = pattern.findall(text)

        #print(ch.strip())


