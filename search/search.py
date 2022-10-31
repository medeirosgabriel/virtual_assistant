# -*- coding: utf-8 -*-

import webbrowser

search = "apple"
url = "https://www.google.com.br/search?q="

for i in range(len(search)):
    url += search[i]

webbrowser.open(url)