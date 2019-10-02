try:
	import urllib.request as urllib2
except ImportError:
	import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import json

class News:

	@staticmethod
	def getNews () :
		'''
		Return a dictionary of top 30 news and their links
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/news.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ol', attrs={'class': 'rectlist'})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			news = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': news, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response

	@staticmethod
	def getEvents () :
		'''
		Return a dictionary of all listed upcoming events
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/events.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ul', attrs={'class': 'orangearrow'})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			event = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': event, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response


	@staticmethod
	def getNotices () :
		'''
		Return a dictionary of all listed Notices
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/notices.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ul', attrs={'class': ''})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			notice = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': notice, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response

	@staticmethod
	def getBusSchedule ():
		response = {}
		url = 'http://www.iitbbs.ac.in/transportation.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		div = soup.find('div', attrs={'class': 'col-md-4'})
		anchors = div.find('p').find_all('a')

		for anchor in anchors:
			ftype = 'pdf' if anchor['href'][-3:] == 'pdf' else 'xls' 
			response[ftype] = 'www.iitbbs.ac.in/' + anchors[0]['href'][3:]

		return response

	@staticmethod
	def getTimeTable(roll):
		year = str(min((datetime.now().year- int(roll[0:2]) + 1), 4))
		today = str(datetime.today().weekday())
		branch = str(roll[2:4])
		dual_or_single = str(roll[5:6])
		dest = "res/" + year + "/" + branch + "/"\
				+ dual_or_single + "/" + today + ".json"
		print(dest)
		try:
			with open (dest, "r") as f:
				data = json.loads(f.read())
			return data
		except Exception as e:
			return {'status':'404','data':[]}
# if __name__ == "__main__":
# 	print News.getNews()
# 	print News.getNotices()
# 	print News.getEvents()
	# print News.getBusSchedule()