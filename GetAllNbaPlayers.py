"""

Fun Project that will scrape the all the NBA player's name.

This script will obtain all the nba players who are 
currently active for the year 2016.

December 10th, 2016

"""

from selenium import webdriver
from bs4 import BeautifulSoup

# create driver and also locate the phantom executable file (this will be unique to your computer)
driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

# the url to use.  NBA.com (As of December 10th, 2016)

url = 'http://www.nba.com/players'

# download html page source (phantomjs will do this)
driver.get(url)

# print the page url (looking at the page)
#print driver.page_source


# create soup object
soup = BeautifulSoup(driver.page_source, 'lxml')

# obtaining the div object in the class below (where all the names of the players will be)
div = soup.find('div', class_= 'row players-wrapper')

# print div and each name of the players

for a in div.find_all('a'):
	print(a.text)

