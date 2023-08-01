import openpyxl
from pdfquery import PDFQuery
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.high_level import extract_pages, extract_text
import re
import os

dir = 'D:\\Newfolder\\Per\\Healthview\\Reports'
files = os.listdir(dir)
index = 0

c1 = 0
results = {'HBA1C': []}

for file in files:
    text = extract_text(dir + '\\' + file )
    reportType = file[0:10]
    reportType1 = file[0:14]
    if reportType == "Only HBA1C":
        c1 = 0
        date = ''
        for t in text.split('\n'):
            if c1 == 52:
                date = t.strip()
                c1 += 1
            elif c1 == 77:
                results['HBA1C'].append(date)
                results['HBA1C'].append(t.strip())
                c1 += 1
            else:
                c1 += 1
    elif reportType1 == "Complete Blood":
        d1 = 0
        date1 = ''
        for t in text.split('\n'):
            if d1 == 52:
                date1 = t.strip()
                d1 += 1
            elif d1 == 934:
                results['HBA1C'].append(date1)
                results['HBA1C'].append(t.strip())
                d1 += 1
            else:
                d1 += 1
print(results)

