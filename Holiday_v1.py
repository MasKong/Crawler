#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import xlwt
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/calendar/custom.html?year=2038&country=42&cols=3&df=1&hol=1"
date = []
#requests.adapters.DEFAULT_RETRIES = 5
for t in range(2037,2048):      #a parameters set by user. Holidays from and to which year you like.
    url = "https://www.timeanddate.com/calendar/custom.html?year="+str(t)+"&country=42&cols=3&df=1&hol=1"
    r = requests.get(url)      #get from the url
    # print (r.encoding)
    # print (r.text)
    soup = BeautifulSoup(r.text)   #use beautifulsoup to extra information we want
    #print(soup.prettify())
    for da in soup.find_all("div", id="calarea")[0].find_all('span',class_="co1")[:-1]:   #here we find all holidays in one year
        date.append(da.text + " " + str(t))    #process the holiday, add year behind it
        print (da.text + "-" + str(t))



import pandas as pd
a = pd.Series([pd.to_datetime(dat) for dat in date])
for t in a:
    print (t)
df = pd.DataFrame(a)
# df = pd.DataFrame(date)
df.to_excel('output.xlsx', header=False, index=False)
