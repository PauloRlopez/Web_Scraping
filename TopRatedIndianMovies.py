
# This script will find the top rated Indian movies according to the IMDB website

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

url = 'http://www.imdb.com/chart/top-indian-movies?ref_=nv_mv_250_in_7'

driver.get(url)

#print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

table = soup.find('table', class_ = 'chart full-width')

#for a in table.find_all('a'):
#	print(a.text)

for td in table.find_all('td', class_ = 'titleColumn'):
	print(td.text.strip().replace('\n','').replace('      ',''))



