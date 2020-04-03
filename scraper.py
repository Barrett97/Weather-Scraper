#!/usr/bin/env python3
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import urllib.request
import pprint
import time

# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS(executable_path = 'C:\Programming\phantomjs-2.1.1-windows\bin')

url = "https://www.theweathernetwork.com/ca/monthly/ontario/toronto"
driver = webdriver.Chrome()
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
# results = soup.find_all('td', attrs={'class': 'day-sunday cal -sq'})
time.sleep(10)

results = driver.find_elements_by_class_name('actual')
print(len(results))

for i in results:
	text = i.text
	print(text)