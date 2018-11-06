import os
from selenium.webdriver import Firefox
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import csv


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


soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(soup.title)

import urllib.request

page = urllib.request.urlopen('https://maplelegends.com/')  # .read()

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

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'

page3 = requests.get("https://maplelegends.com/ranking/monsterbook", headers=headers)
soup3 = BeautifulSoup(page3.text, 'html.parser')
print(soup3.prettify())

page4 = requests.get("http://maplestory.nexon.net/rankings/overall-ranking/legendary?rebootIndex=0&pageIndex=6#ranking")
soup4 = BeautifulSoup(page4.text, 'html.parser')
print(soup4.prettify())

soup4.tbody  # chunk of user data
junk = soup4.tbody.find_all('tr')
junkjunk = junk[0].find_all('td')

int(junkjunk[0].string)
# junkjunk[1] link for avatar all broken due to NEXON
junkjunk[2].string
re.split(r'["]|world ', str(junkjunk[3]))[6]
re.split(r'[="]', str(junkjunk[4]))[2]

rank.append(list((int(junkjunk[0].string),)))

# after Scrapy stuff
with open('gms.html', 'wb') as f:
    f.write(page4.content)

# practicing reading with CSS / XPath

from scrapy.http import HtmlResponse

int(Selector(text=page4.content).xpath('//tr/td/text()').extract()[0])

Selector(text=page4.content).xpath('//tr').extract()[0]  # first element is the column names
len(Selector(text=page4.content).xpath('//tr'))
Selector(text=page4.content).xpath('//tr/td').extract()  # first element is the column names

[x.xpath('//td/text()').extract()[0] for x in Selector(text=page4.content).xpath('//child::tr')[1:5]]

debugx = Selector(text=page4.content).xpath('//tr/td[1]/text()').extract()
debugx = Selector(text=page4.content).xpath('//tr/following-sibling::tr[1]')  # same as above, but bad notation
debugx[1].xpath('//td')

# [int(x) for x in debugx]


# now looking for Character Names

debugx = Selector(text=page4.content).xpath('//tr/td[3]').extract()

[int(x) for x in Selector(text=page4.content).xpath('//tr/td[1]/text()').extract()]
Selector(text=page4.content).xpath('//tr/td[3]/text()').extract()
Selector(text=page4.content).xpath('//tr/td/img/@title').extract()
Selector(text=page4.content).xpath('//tr/td/a/@title').extract()[0]
Selector(text=page4.content).xpath('//tr/td/img[contains(@class, "avatar")]/@src').extract()

# looking for next page link
Selector(text=page4.content).xpath('//ul/li/a[contains(@class, "next")]/@href').extract()

next_page = Selector(text=page4.content).xpath('//ul/li/a[contains(@class, "next")]/@href').extract()[0]
print('http://maplestory.nexon.net/rankings/overall-ranking/legendary{}'.format(next_page))
# print(Selector(text=page4.content).urljoin(next_page)) does not work. scrapy.request contains urljoin

# Selenium stuff


# from lxml import html

browser = Chrome('/Users/Tim/PyCharmProjects/learning/chromedriver')
browser.get('https://maplelegends.com/ranking/monsterbook?page=1&search=')
tree = browser.page_source
tree2 = browser.execute_script("return document.documentElement.outerHTML;")
# Apparently Selenium can perform XPath in house using the browser, so it might be more efficient so use the built
# in finding methods. To retrieve a complete xml/html file, just find(root)
groot = browser.find_elements_by_xpath('//*')
# tree = html.fromstring(tree)
# tree = html.fromstring(browser.get)

# browser.find_elements_by_xpath('//tr')
# returns web page elements, NOT HTML
browser.execute_script("return document.documentElement.outerHTML;") == browser.page_source

html = browser.execute_script("return document.documentElement.outerHTML;")
html = Selector(text=html)
html.xpath('//tr/td/b/text()').extract()
# html.xpath('//tr/td/img[contains(@src, "magician")]/following-sibling::*[text()]').extract()
# html.xpath('//tr/td/br').extract()
junk = html.xpath('//tr/comment()[contains(., "job")]/following-sibling::*[1]').extract()
for x in range(5):
    print(html.xpath('//tr/td/b/text()').extract()[5 * x])
    print(html.xpath('//tr/td/b/text()').extract()[5 * x + 1])
    print(html.xpath('//tr/td/b/text()').extract()[5 * x + 2])
    print(html.xpath('//tr/td/b/text()').extract()[5 * x + 3])
    print(html.xpath('//tr/td/b/text()').extract()[5 * x + 4])
    print(
        re.split(r'<br>|</td>', html.xpath('//tr/comment()[contains(., "job")]/following-sibling::*[1]').extract()[x])[
            1])
# not sure if this is most efficient way to write. Use junk dummy instead?


with open('Legends.csv', 'a', newline='') as file:
    filewriter = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    filewriter.writerow(['Rank', 'IGN', 'Fame', 'Level', 'Cards', 'Class'])
    for x in range(5):
        filewriter.writerow(list((html.xpath('//tr/td/b/text()').extract()[5 * x],
                            html.xpath('//tr/td/b/text()').extract()[5 * x + 1],
                            html.xpath('//tr/td/b/text()').extract()[5 * x + 2],
                            html.xpath('//tr/td/b/text()').extract()[5 * x + 3],
                            html.xpath('//tr/td/b/text()').extract()[5 * x + 4],
                            re.split(r'<br>|</td>',
                                     html.xpath('//tr/comment()[contains(., "job")]/following-sibling::*[1]').extract()[
                                         x])[1])))

browser.find_element_by_xpath('//li/a[contains(.,"Next")]').click()
#browser.get('https://maplelegends.com/ranking/monsterbook?page=2&search=')
html = Selector(text=browser.execute_script("return document.documentElement.outerHTML;"))
#html = Selector(text=html)

# downloading images
browser.get('https://maplelegends.com/avatar/create.php?name=Nell')
html.xpath('//img').extract()
elem = browser.find_element_by_xpath('//img')
elem.send_keys(Keys.COMMAND)

# Keys = selenium.webdriver.common.keys.Keys      # ok, this is how to create shorthands
# ActionChains = selenium.webdriver.common.action_chains.ActionChains
ActionChains(browser).key_down(Keys.COMMAND).send_keys('s').key_up(Keys.COMMAND).perform()
action = ActionChains(browser)
action.key_down(Keys.COMMAND)
action.send_keys('s')
action.key_up(Keys.COMMAND)
action.perform()

ActionChains(browser).context_click(elem).perform()




# FIRST TEST

# ActionChains(browser).context_click(elem).perform()
# time.sleep(1)
# pyautogui.typewrite(['down', 'down', 'enter'], interval=.5)
# ERMAHGERD IT WERRRRRRKKKKSSSSS!
# pyautogui.hotkey('command', 's')       #SAME PROBLEM WITH CHROMEDRIVER?????

# time.sleep(1)
# pyautogui.moveTo(500, 60)
# pyautogui.click(interval=1)
# pyautogui.typewrite(['backspace', 'N', 'e', 'l', 'l', 'enter'], interval=1)


# pyautogui.typewrite(['backspace', junk ], interval=1)      # ok, so typewrite works if 1 character at a time
# junk = "Nell"



# THE FUN FOR 5 IMAGES AT ONCE STARTS HERE!!!

# html.xpath('//tr/td/img[contains(@class, "avatar")]').extract()
# html.xpath('//tr/td/img[contains(@class, "avatar")]/@alt').extract()

browser = Chrome('/Users/Tim/PyCharmProjects/learning/chromedriver')
browser.get('https://maplelegends.com/ranking/monsterbook?page=1&search=')
html = Selector(text=browser.execute_script("return document.documentElement.outerHTML;"))
pics = browser.find_elements_by_xpath('//tr/td/img[contains(@class, "avatar")]')
# ActionChains(browser).context_click(pics[0]).perform()
for x in range(len(pics)):
    ActionChains(browser).context_click(pics[x]).perform()
    pyautogui.typewrite(['down', 'down', 'enter'], interval=.5)
    pyautogui.moveTo(500, 60)
    pyautogui.click(interval=1)
    time.sleep(2)
    pyautogui.typewrite(html.xpath('//tr/td/img[contains(@class, "avatar")]/@alt').extract()[x], interval=.5)
    pyautogui.typewrite(['enter'], interval=.5)
    time.sleep(2)
browser.find_element_by_xpath('//li/a[contains(.,"Next")]').click()
# 1 CASE TEST ***

ActionChains(browser).context_click(pics[0]).perform()
pyautogui.typewrite(['down', 'down', 'enter'], interval=.5)
pyautogui.moveTo(500, 60)
pyautogui.click(interval=1)
time.sleep(2)
# pyautogui.typewrite(['backspace'], interval=.5)
pyautogui.typewrite('Nell', interval=.5)
pyautogui.typewrite(['enter'])

for y in range(len(html.xpath('//tr/td/img[contains(@class, "avatar")]/@alt').extract()[0])):
    time.sleep(.5)
    pyautogui.typewrite(html.xpath('//tr/td/img[contains(@class, "avatar")]/@alt').extract()[0][y])
pyautogui.typewrite('enter', interval=.5)
time.sleep(2)
# 1 CASE TEST /

browser.close()
# browser = Chrome('chromedriver')

# browser = Chrome()

# APPARENTLY CHROMEDRIVER HAS SEND_KEYS BUG SINCE 2011
# TRY FIREFOX/GECKO INSTEAD


# from lxml import html

browser = Firefox('/Users/Tim/PyCharmProjects/learning/geckodriver')
browser = Firefox()
browser.get('https://maplelegends.com/ranking/monsterbook?page=1&search=')



print(os.getcwd())


#image processing / classification

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2grey
from skimage.io import imread
from skimage.io import imshow

# img_rgb = mpimg.imread('/Users/Tim/PyCharmProjects/learning/Legends_Avatars/Nell.png')
img = imread('/Users/Tim/PyCharmProjects/learning/Legends_Avatars/Nell.png', as_gray=True)
imshow(img)

# img_rgb = cv2.imread('/Users/Tim/PyCharmProjects/learning/Legends_Avatars/Nell.png')
# channels are inverted
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGBA2GRAY)
# img_gray = rgb2grey(img_rgb)       #so, all along the gray images produced are fine, but read incorrectly by plt
# cv2.imwrite('res.png',img_gray)

# TAKE HOME MESSAGE: USE ALL FROM 1 LIBRARY, I.E. SciKit-Image / SKIMAGE


# OK, SO NOW TEST RUN FOR MATCHING 2 HAIRSTYLES AGAINST NELL

matcher = imread('/Users/Tim/PyCharmProjects/learning/Legends_Avatars/soprano2.png', as_gray=True)
imshow(matcher)

from skimage.feature import match_template

result = match_template(img, matcher)

matcher2 = imread('/Users/Tim/PyCharmProjects/learning/Legends_Avatars/cute wave hair2.png', as_gray=True)
result2 = match_template(img, matcher2)
