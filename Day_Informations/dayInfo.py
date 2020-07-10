# -*- coding: utf-8 -*-

import datetime

import requests
from bs4 import BeautifulSoup

now = datetime.datetime.now()
months = {1: "January", 2: "February", 3: "March",
          4:"April", 5: "May", 6:"June", 7:"July",
          8:"August", 9 : "September", 10:"October",
          11:"November", 12:"December"}

page = requests.get('https://www.timeanddate.com/weather/')
bsPage = BeautifulSoup(page.text, 'html.parser')

city = bsPage.findAll(class_="my-city__city")
temp = bsPage.findAll(class_="my-city__temp")
status = bsPage.findAll(class_="my-city__wtdesc")

for i in range(len(city)):
    print("City: %s  Temperature: %s  Status: %s" %(city[i].contents[0], temp[i].contents[0], status[i].contents[0]))

string = "Today is %s %dth, %d. It's %d hours and %d minutes" %(months[now.month], now.day, now.year, now.hour, now.minute)
print(string)

