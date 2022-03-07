# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

newsTypes = {
    "Tech Crunch": {"link" : "https://techcrunch.com/", "classes": ["post-block__title__link"]},
    "CNN": {"link" : "https://www.cnnbrasil.com.br/", "classes": ["home__title"]},
}

type_ = "CNN"

page = requests.get(newsTypes[type_]["link"])

bsPage = BeautifulSoup(page.text, 'html.parser')

news = []
for c in newsTypes[type_]["classes"]:
    new = bsPage.find_all(class_= c)
    for n in new:
        news.append(n.contents[0].replace("\n", "").replace("\t", ""))

for n in news:
    print("==> " + n + "\n")