
#import beautifulsoup4 as beautifulsoup4

print("Herp Derp")

newgenpoke = 1

if newgenpoke == 0:
    print("maybe true")
else:
    print("eh, probably not true")

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(soup.title)

import urllib.request
page = urllib.request.urlopen('https://maplelegends.com/')#.read()

page = urllib.request.urlopen('https://www.jetbrains.com/help/pycharm/settings-tools-server-certificates.html')
soup2 = BeautifulSoup(page, 'html.parser')
print(soup2.prettify())

import requests
import re

name = list()
classm = list()
world = list()
level = list()
rank = list()

page3 = requests.get("https://maplelegends.com/ranking/monsterbook")
soup3 = BeautifulSoup(page3.text, 'html.parser')
print(soup3.prettify())

page4 = requests.get("http://maplestory.nexon.net/rankings/overall-ranking/legendary?rebootIndex=0&pageIndex=6#ranking")
soup4 = BeautifulSoup(page4.text, 'html.parser')
print(soup4.prettify())

soup4.tbody #chunk of user data
junk = soup4.tbody.find_all('tr')
junkjunk = junk[0].find_all('td')

int(junkjunk[0].string)
#junkjunk[1] link for avatar all broken due to NEXON
junkjunk[2].string
re.split(r'["]|world ' , str(junkjunk[3]))[6]
re.split(r'[="]' , str(junkjunk[4]))[2]


rank.append(list((int(junkjunk[0].string), )))

#after Scrapy stuff
with open('gms.html', 'wb') as f:
    f.write(page4.content)

#practicing reading with CSS / XPath

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

Selector(text=page4.content).xpath('//tr/td/img/@title').extract()
Selector(text=page4.content).xpath('//tr/td/a/@title').extract()