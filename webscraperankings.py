# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from scrapy.selector import Selector
# from bs4 import BeautifulSoup
import csv
# import re


browser = Chrome('/Users/Tim/PyCharmProjects/learning/chromedriver')
browser.get('https://maplelegends.com/ranking/monsterbook?page=1&search=')

with open('MonsterbookRanking.csv', 'w', newline='') as file:
    filewriter = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Rank', 'IGN', 'Fame', 'Level', 'Cards', 'Class'])
    for y in range(500):
        time.sleep(5)
        html = Selector(text=browser.execute_script("return document.documentElement.outerHTML;"))
        for x in range(5):
            filewriter.writerow(list((html.xpath('//tr/td/b/text()').extract()[5 * x],
                                      html.xpath('//tr/td/b/text()').extract()[5 * x + 1],
                                      html.xpath('//tr/td/b/text()').extract()[5 * x + 2],
                                      html.xpath('//tr/td/b/text()').extract()[5 * x + 3],
                                      html.xpath('//tr/td/b/text()').extract()[5 * x + 4],
                                      html.xpath('//tr/comment()[contains(., "job")]/following-sibling::*[1]/text()')
                                      .extract()[x]
                                      )))
        browser.find_element_by_xpath('//li/a[contains(.,"Next")]').click()
browser.quit()



browser = Chrome('/Users/Tim/PyCharmProjects/learning/chromedriver')
browser.get('https://maplelegends.com/ranking/all?page=1&search=')

with open('OverallRanking.csv', 'w', newline='') as file:
    filewriter = csv.writer(file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Rank', 'IGN', 'Fame', 'Level', 'Class'])
    for y in range(500):
        time.sleep(5)
        html = Selector(text=browser.execute_script("return document.documentElement.outerHTML;"))
        for x in range(5):
            filewriter.writerow(list((html.xpath('//tr/td/b/text()').extract()[4 * x],
                                      html.xpath('//tr/td/b/text()').extract()[4 * x + 1],
                                      html.xpath('//tr/td/b/text()').extract()[4 * x + 2],
                                      html.xpath('//tr/td/b/text()').extract()[4 * x + 3],
                                      html.xpath('//tr/comment()[contains(., "job")]/following-sibling::*[1]/text()')
                                      .extract()[x]
                                      )))
        browser.find_element_by_xpath('//li/a[contains(.,"Next")]').click()
browser.quit()