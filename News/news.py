# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

newsTypes = {"Tech": {"link" : "https://techcrunch.com/", "classes": ["post-block__title__link"] }}

page = requests.get(newsTypes["Texh"]["link"])

bsPage = BeautifulSoup(page.text, 'html.parser')

news = []
for c in newsTypes["Tech"]["classes"]:
    new = bsPage.find_all('a', class_= c)
    for n in new:
        news.append(n.contents[0].replace("\n", "").replace("\t", ""))

for n in news:
    print(n)