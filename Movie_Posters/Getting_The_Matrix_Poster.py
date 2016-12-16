"""
one of my favorite movies is the "The Matrix" that's why I decided to 

get the movie poster from the IMDB website.

"""


# Getting our libraries

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# input the original url 

url = 'http://www.imdb.com/title/tt0133093/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2398042102&pf_rd_r=0R5N8F1YHDB2C1ZRVZXZ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_18'

driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div', class_ = 'poster')  # This is where the poster first is located

a = div.find('a') # get the a['href']

print('http://www.imdb.com' + a['href'])   # This is the absolute link plus the new link

url = 'http://www.imdb.com' + a['href']  

driver.get(url)  # driver get the new link 

# State a new soup

soup = BeautifulSoup(driver.page_source, 'lxml')

# Get all div

all_div = soup.find_all('div', class_ = 'pswp__zoom-wrap') # This is where our second class is located 

all_img = all_div[1].find_all('img')  # since is on the second position img[1]['src']

print(all_img[1]['src'])

# To download this to my desktop let's use requests

f = open('The_Matrix_poster_image.jpg', 'wb')
f.write(requests.get(all_img[1]['src']).content)
f.close()

driver.quit()


# output
"""
http://www.imdb.com/title/tt0133093/mediaviewer/rm2882537984?ref_=tt_ov_i
https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg

"""

# ====  end


