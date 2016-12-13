
"""
This script will get all the NBA information such as name, number, position,
name of the team and will extract the link in a list.


"""

from selenium import webdriver
from bs4 import BeautifulSoup

# creating a class named Palyer

class Player():
	""" The Player class will obtain a player's name, the link  
        and the placed the results on a list """
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

	div = soup.find('div', class_= 'small-12 columns')

	# creating an empty player list

	player_list = []

    # creating a for loop and then append the list
	for a in div.find_all('a'):
		new_play = Player()
		new_play.name = a.text
		new_play.link = a['href']
		player_list.append(new_play)


	for one_player in player_list:

		print(one_player.name)
		print(one_player.link)

	driver.quit()

	return player_list


get_player_list()

