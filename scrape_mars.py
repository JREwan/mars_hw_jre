import time
#from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests


# Mars news
def mars_news():
    mars_junk = []
    # Scrape NASA Mars News
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    mars_stuff = {}
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
    headline_txt = soup.find('div', class_="content_title").text
    first_para_txt = soup.find('div', class_="article_teaser_body").text
    mars_junk.append(headline_txt)
    mars_junk.append(first_para_txt)
        
    return mars_junk

# JPL Featured Image
def mars_feat_image():
    # Scrape JPL Mars Space Images - Featured Image
    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    feat_image_link = ""
    browser = webdriver.Chrome('chromedriver.exe')
    #listings = {}
    # get the page
    browser.get(url)
    #Wait a few seconds
    time.sleep(3)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # get the first result
    feature_img = soup.find('a', class_="button fancybox")
    #turn it into a string and split it on the item that hold the link value
    splitsville = str(feature_img).split("data-fancybox-href=")
    # grab the first part of the splitsville[1] (i.e. the 2nd part of the link)
    url_part2 = splitsville[1].split(" ")
    # trim off the quotes
    part2 = url_part2[0].replace('"','')
    feat_image_link = "https://www.jpl.nasa.gov" + part2

    return feat_image_link

# Weather
def mars_weather():
    # Scrape twitter mars weather
    # URL of page to be scraped
    url = "http://twitter.com/marswxreport?lang=en"
    weather_junk = ""
    browser = webdriver.Chrome('chromedriver.exe')
    # get the page
    browser.get(url)
    #Wait a few seconds
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # get the first result
    weathertweet = soup.find('div', class_="js-tweet-test-container")
    #return the tweet
    weather_junk = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    return weather_junk

# Mars facts
def mars_facts():
    mars_facts_list = []
    # Mars facts
    # url of page to be scraped
    url = "http://space-facts.com/mars/"


    return mars_facts_list

# Mars Hemispheres    
def mars_hemi1():
    mars_hemi1 = []
    base_url = "https://astrogeology.usgs.gov"
    url_valles = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    # Valles Marineris Hemisphere
    browser = webdriver.Chrome('chromedriver.exe')
    # get the page
    browser.get(url_valles)
    #Wait a few seconds
    time.sleep(7)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # Valles Marineris Hemisphere 2 - get the big image
    valles_speclink = soup.find('img', class_="wide-image")
    #turn it into a string and split it on the item that hold the link value
    splitsville = str(valles_speclink).split("src=")
    url_part2 = splitsville[1].split("/>")
    # trim off the quotes
    part2 = url_part2[0].replace('"','')
    valles_full_img = base_url + part2
    valles_title = "Valles Marineris Hemisphere"
    mars_hemi1.append(valles_title)
    mars_hemi1.append(valles_full_img)

    return mars_hemi1

def mars_hemi2():
    mars_hemi2 = []
    base_url = "https://astrogeology.usgs.gov"
    url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    # Cerberus Marineris Hemisphere
    browser = webdriver.Chrome('chromedriver.exe')
    # get the page
    browser.get(url_cerberus)
    #Wait a few seconds
    time.sleep(7)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # Cerberus Hemisphere 2 - get the big image
    cerberus_speclink = soup.find('img', class_="wide-image")
    #turn it into a string and split it on the item that hold the link value
    splitsville = str(cerberus_speclink).split("src=")
    url_part2 = splitsville[1].split("/>")
    # trim off the quotes
    part2 = url_part2[0].replace('"','')
    cerberus_full_img = base_url + part2
    cerberus_title = "Cerberus Hemisphere"
    mars_hemi2.append(cerberus_title)
    mars_hemi2.append(cerberus_full_img)

    return mars_hemi2

def mars_hemi3():
    mars_hemi3 = []
    base_url = "https://astrogeology.usgs.gov"
    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    # Schiaparelli Hemisphere
    browser = webdriver.Chrome('chromedriver.exe')
    # get the page
    browser.get(url_schiaparelli)
    #Wait a few seconds
    time.sleep(7)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # Schiaparelli Hemisphere 2 - get the big image
    schia_speclink = soup.find('img', class_="wide-image")
    #turn it into a string and split it on the item that hold the link value
    splitsville = str(schia_speclink).split("src=")
    url_part2 = splitsville[1].split("/>")
    # trim off the quotes
    part2 = url_part2[0].replace('"','')
    schia_full_img = base_url + part2
    schia_title = "Schiaparelli Hemisphere"
    mars_hemi3.append(schia_title)
    mars_hemi3.append(schia_full_img)

    return mars_hemi3
    
def mars_hemi4():
    mars_hemi4 = []
    base_url = "https://astrogeology.usgs.gov"
    url_syrtis = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    
    # Syrtis Major Hemisphere
    browser = webdriver.Chrome('chromedriver.exe')
    # get the page
    browser.get(url_syrtis)
    #Wait a few seconds
    time.sleep(7)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    # Syrtis Major Hemisphere 2 - get the big image
    syrtis_speclink = soup.find('img', class_="wide-image")
    #turn it into a string and split it on the item that hold the link value
    splitsville = str(syrtis_speclink).split("src=")
    url_part2 = splitsville[1].split("/>")
    # trim off the quotes
    part2 = url_part2[0].replace('"','')
    syrtis_full_img = base_url + part2
    syrtis_title = "Syrtis Major Hemisphere"
    mars_hemi4.append(syrtis_title)
    mars_hemi4.append(syrtis_full_img)

    return mars_hemi4


    
    
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
