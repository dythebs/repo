import requests
from bs4 import BeautifulSoup
import time


aminer_id = '53f459c4dabfaee2a1d80cdf'


class Article:
	def __init__(self, year, title, authors, cite_num):
		self._year = year
		self._title = title
		self._authors = authors
		self._cite_num = cite_num

	@property
	def year(self):
		return self._year

	@property
	def title(self):
		return self._title

	@property
	def authors(self):
		return self._authors

	@property
	def cite_num(self):
		return self._cite_num


def get_aminer_articles():
	stats_url = 'https://api.aminer.cn/api/person/pubs/'+aminer_id+'/stats'
	headers = {
	'Accept': 'application/json, text/plain, */*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'Host': 'api.aminer.cn',
	'Origin': 'https://www.aminer.cn',
	'Pragma': 'no-cache',
	'Referer': 'https://www.aminer.cn/profile/w-bruce-croft/'+aminer_id,
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}
	article_list = []
	years = requests.get(stats_url,headers=headers).json()['years']
	for year in years:
		time.sleep(0.5)
		year = year['year']
		year_url = 'https://api.aminer.cn/api/person/pubs/'+aminer_id+'/range/year/'+str(year)+'/0/20'
		articles = requests.get(year_url,headers=headers).json()
		for article in articles:
			author_list = []
			authors = article['authors']
			for author in authors:
				author_list.append(author['name'])
			article_list.append(Article(year, article['title'], author_list, article['num_citation']))
	return article_list


get_aminer_articles()
