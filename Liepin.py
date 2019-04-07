import requests
from bs4 import BeautifulSoup
import csv
import copy
import sys
import io
it = 'https://www.liepin.com/it/'
realestate = 'https://www.liepin.com/realestate/'
financial = 'https://www.liepin.com/financial/'
consumergoods = 'https://www.liepin.com/consumergoods/'
automobile = 'https://www.liepin.com/automobile/'
medicine = 'https://www.liepin.com/medicine/'
test = set()
out = open("liepinoutput.csv",'a+',newline='',encoding='utf-8')

classes = [it, realestate, financial, consumergoods, automobile, medicine]
for link in classes:
    r = requests.get(link)
    s = BeautifulSoup(r.text, 'lxml')
    firstLevel = s.find(class_='sidebar').find_all(name='h2')
    f = len(firstLevel)#一级长度

    l1 = []
    l2 = []
    l3 = []
    for first in firstLevel:
        l1.append(first.text)

    secondLevel = s.find_all(name='dl')

    ctr = 0
    for i in secondLevel:
        ctr += 1
        l2 = []
        levell = list()
        levell.append(l1[ctr - 1])
        for se in (i.find_all(name='dt')):
            thirdLevel = se.next_sibling.next_sibling
            print(thirdLevel)
            for k in thirdLevel.find_all(name='a'):
                l3.append(k.text)
                level = copy.deepcopy(levell)
                level.append(se.text)
                level.append(k.text)
                test.add(k.text)
                csv_writer = csv.writer(out, dialect='excel')
                csv_writer.writerow(level)
                #print(level)

        if ctr >= f:
            break
print(len(test))





