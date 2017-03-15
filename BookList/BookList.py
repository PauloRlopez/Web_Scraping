
# Getting from Amazon a list of Web Scrapping book list
				

from bs4 import BeautifulSoup
from selenium import webdriver

class Scrapping_Book():
	def __init__(self):
		self.title = ""
		self.link = ""

def get_scrapping_book_list():	

	driver = webdriver.PhantomJS(executable_path = r'/Users/Create/WebScrapping/phantomjs/bin/phantomjs')

	url = 'https://www.amazon.com/s/ref=nb_sb_ss_sc_1_5?url=search-alias%3Dstripbooks&field-keywords=web+scraping+with+python&sprefix=websc%2Cundefined%2C202&crid=39ZJY8UEML8G3&rh=n%3A283155%2Ck%3Aweb+scraping+with+python'

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	ul = soup.find('ul', {'id':'s-results-list-atf'})

	book_list = []

	for li in ul.find_all('li', class_ = 's-result-item celwidget'):	

		all_a = li.find_all('a')
		# print(all_a[1].text)
		# print(all_a[1]['href'])

		new_book = Scrapping_Book()
		new_book.title = all_a[1].text
		new_book.link = all_a[1]['href']
		book_list.append(new_book)


	driver.quit()

	return book_list

sb = get_scrapping_book_list()

for book in sb:
	print(book.title)
	print(book.link)



# OUTPUT

"""

Web Scraping with Python: Collecting Data from the Modern Web
https://www.amazon.com/Web-Scraping-Python-Collecting-Modern/dp/1491910291
Amazon's Ryan Mitchell Page
/Ryan-Mitchell/e/B00MQI8TVQ/ref=sr_tc_2_0?qid=1481925993&sr=1-2-ent
Web Scraping with Python (Community Experience Distilled)
https://www.amazon.com/Scraping-Python-Community-Experience-Distilled/dp/1782164367
Learn Web Scraping With Python In A Day: The Ultimate Crash Course to Learning the Basics of Web Scraping With Python In No Time (Python,…
https://www.amazon.com/Learn-Web-Scraping-Python-Day/dp/151865987X
Mining the Social Web: Data Mining Facebook, Twitter, LinkedIn, Google+, GitHub, and More
https://www.amazon.com/Mining-Social-Web-Facebook-LinkedIn/dp/1449367615
Automate the Boring Stuff with Python: Practical Programming for Total Beginners
https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994
Python for Everybody: Exploring Data in Python 3
https://www.amazon.com/Python-Everybody-Exploring-Data/dp/1530051126
Data Science from Scratch: First Principles with Python
https://www.amazon.com/Data-Science-Scratch-Principles-Python/dp/149190142X
Python Machine Learning
https://www.amazon.com/Python-Machine-Learning-Sebastian-Raschka/dp/1783555130
Fluent Python: Clear, Concise, and Effective Programming
https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008
Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython
https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793
Python Crash Course: A Hands-On, Project-Based Introduction to Programming
https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036


"""



# ======= END
