import requests
from bs4 import BeautifulSoup
import time


gs_id = 'ArV74ZMAAAAJ'


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


def gs_praser(html, article_list):
	html = html.replace('&lt;','<')
	html = html.replace('&gt;','>')
	html = html.replace('\\','')
	soup = BeautifulSoup(html, "html.parser")
	articles = soup.find_all('tr',class_='gsc_a_tr')
	for article in articles:
		article_list.append(Article(article.span.text[2:], article.a.text,
				article.div.text.split(', '), article.find('a',class_='gsc_a_ac gs_ibl').text))


def get_gs_articles():
	start = 0
	url = 'https://scholar.google.com/citations?user='+gs_id+'&hl=en&cstart='+str(start)+'&pagesize=100'
	headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'cache-control': 'no-cache',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://scholar.google.com',
		'pragma': 'no-cache',
		'referer': 'https://scholar.google.com/citations?user='+gs_id+'&hl=en',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'x-requested-with': 'XHR',
	}
	data = {
		'json': '1'
	}
	article_list = []
	json = requests.post(url,headers=headers,data=data).json()
	gs_praser(json['B'], article_list)
	while 'N' in json:
		time.sleep(1)
		start += 100
		url = 'https://scholar.google.com/citations?user='+gs_id+'&hl=en&cstart='+str(start)+'&pagesize=100'
		json = requests.post(url,headers=headers,data=data).json()
		gs_praser(json['B'], article_list)
	return article_list


get_gs_articles()
