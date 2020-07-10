# -*- coding: utf-8 -*-

import webbrowser

search = "apple".split(" ")
print(search)
url = "https://www.google.com.br/search?q="

for i in range(len(search)):
    url += search[i] + "+" if i != len(search) - 1 else search[i]
    
webbrowser.open(url)