import time
#from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests



# Scrape NASA Mars News
# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
mars_news_dict = {}
# scrape & fire up the BS!
browser = webdriver.Chrome('chromedriver.exe')
# get the page
browser.get(url)
#Wait a few seconds
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
# Examine the results, then determine element that contains sought info
# get the first result
headline = soup.find('div', class_="content_title")
first_para = soup.find('div', class_="article_teaser_body")
# grab the title & print it!
mars_news_dict["title"] = soup.find('div', class_="content_title").text
mars_news_dict["mn_para"] = soup.find('div', class_="article_teaser_body").text
    
print(mars_news_dict)

