import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from scrapy.selector import Selector
# from bs4 import BeautifulSoup
import csv
import re


browser = Chrome('/Users/Tim/PyCharmProjects/learning/chromedriver')
browser.get('https://forum.maplelegends.com/index.php?threads/guide-beauty-parlor-hair-face-skin.7651/')
html = Selector(text=browser.execute_script("return document.documentElement.outerHTML;"))
# face_url = browser.find_elements_by_xpath('//tr/td/img[contains(@class, "avatar")]')

hair_url = html.xpath('//tr/td/img/@src').extract()     # gets imgur urls
html.xpath('//tr/td/img/preceding::*[1]/text()').extract()       # gets hair / eye names

browser.get(hair_url[400])
html.xpath('//button/span/span/text()').extract_first()

# Hair Sublists
male_hair_url = html.xpath('//button/span/span[contains(., "Male Hair")]/following::*[1]//tr/td/img/@src').extract()
female_hair_url = html.xpath('//button/span/span[contains(., "Female Hair")]/following::*[1]//tr/td/img/@src').extract()

male_hair_name = html.xpath('//button/span/span[contains(., "Male Hair")]/following::*[1]//tr/td/img/preceding::*[1]/text()').extract()
female_hair_name = html.xpath('//button/span/span[contains(., "Female Hair")]/following::*[1]//tr/td/img/preceding::*[1]/text()').extract()


with open('Male Hair URL.txt', 'a', newline='') as file:
    for x in range(len(male_hair_url)):
        file.write(male_hair_url[x] + '\n')

with open('Male Hair Name.txt', 'a', newline='') as file:
    for x in range(len(male_hair_name)):
        file.write(male_hair_name[x] + '\n')

with open('Female Hair URL.txt', 'a', newline='') as file:
    for x in range(len(female_hair_url)):
        file.write(female_hair_url[x] + '\n')

with open('Female Hair Name.txt', 'a', newline='') as file:
    for x in range(len(female_hair_name)):
        file.write(female_hair_name[x] + '\n')


def return_line(line_number, file_name):
    with open(file_name, 'r') as file:
        for x in range(line_number-1):
            file.readline()
        return re.split('\n', file.readline())[0]


def beforeBlank(line):
    return re.split(' ', line)[0]


def beforeSlash(line):
    return re.split('/', line)[0]


def replaceSlash(line):
    return line.replace('/', ':')


# for all male hair
# should find dynamic method to find the 141...

for x in range(141):
    browser.get(return_line(x+1, '/Users/Tim/PycharmProjects/learning/Male Hair URL.txt'))
    time.sleep(2)
    pyautogui.moveTo(500, 60)
    pyautogui.click(interval=1)
    time.sleep(2)
    pyautogui.keyDown('command')
    pyautogui.keyDown('s')
    pyautogui.keyUp('command')
    pyautogui.keyUp('s')
    time.sleep(2)
    pyautogui.typewrite(return_line(x+1, '/Users/Tim/PycharmProjects/learning/Male Hair Name.txt'), interval=.5)
    pyautogui.typewrite(['enter'])
    time.sleep(5)

# now to open each saved hair file and re-save just 1 grayscale copy

pyautogui.click(40, 150)
for x in range(141):
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('w')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('w')
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('o')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('o')
    time.sleep(5)
    pyautogui.typewrite(beforeBlank(return_line(x+1, '/Users/Tim/PycharmProjects/learning/Male Hair Name.txt')),
                        interval=.5)
    pyautogui.typewrite(['enter'])
    time.sleep(5)

    pyautogui.moveTo(40, 150)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(100, 250, 1, button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(5)

    pyautogui.keyDown('command')
    pyautogui.keyDown('c')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('c')
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('n')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('n')
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('s')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('s')
    time.sleep(5)
    pyautogui.typewrite(return_line(x+1, '/Users/Tim/PycharmProjects/learning/Male Hair Name.txt') + 's', interval=.2)
    pyautogui.typewrite(['enter'])
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('w')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('w')
    time.sleep(5)
    pyautogui.keyDown('command')
    pyautogui.keyDown('w')
    time.sleep(.5)
    pyautogui.keyUp('command')
    pyautogui.keyUp('w')
    time.sleep(5)

# to be used in future!
import subprocess
# FileName = return_line(6, '/Users/Tim/PycharmProjects/learning/Male Hair Name.txt')
subprocess.call(['open', '/Users/Tim/PycharmProjects/learning/Legends_Avatars/Male_Hair/' +
                 return_line(111, '/Users/Tim/PycharmProjects/learning/Male Hair Name.txt') + '.png'])

# a much more generalized alternative! Warning that this can be ugly with .txt files in MacOS
