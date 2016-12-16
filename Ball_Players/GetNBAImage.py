# This file will grab a picture of an NBA player.

from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests



class Player():
	
	def __init__(self):
		self.name = ""
		self.link = ""
		
def get_player_list():
	# create driver
	driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

	url = 'http://www.nba.com/players'  

	# download html page
	driver.get(url)

	# print driver.page_source

	# create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_= 'row players-wrapper')

	# print div

	player_list = []


	for a in div.find_all('a'):
		# print a.text
		# print a['href']
		new_play = Player()
		new_play.name = a.text
		new_play.link = a['href']
		player_list.append(new_play)


	for one_player in player_list:

		print(one_player.name)
		print(one_player.link)

	driver.quit()

	return player_list



driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

url = 'http://www.nba.com/players/stephen/curry/201939'

driver.get(url)

#print(driver.page_source)

# nba-player-header__item nba-player-header__headshot (our class)

soup = BeautifulSoup(driver.page_source, 'lxml')

sec = soup.find('section', class_ = 'nba-player-header__item nba-player-header__headshot')

img = sec.find('img')

print(img['src'])  # soure

# This is what gives back
#http://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/201939.png

f = open('Stephen_Curry.jpg','wb')

f.write(requests.get(img['src']).content)  # it will download to your folder

f.close()

driver.quit()



