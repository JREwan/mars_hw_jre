import time
#from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests



def mars_news():
    # Scrape NASA Mars News
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    listings = {}
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
    listings["title"] = soup.find('div', class_="content_title").text
    listings["mn_para"] = soup.find('div', class_="article_teaser_body").text
    
    return listings


    
    
def scrape():
    browser = webdriver.Chrome('chromedriver.exe')
    listings = {}

    url = "https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
    browser.get(url)
    time.sleep(1)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    listings["headline"] = soup.find("a", class_="result-title").get_text()
    listings["price"] = soup.find("span", class_="result-price").get_text()
    listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings
