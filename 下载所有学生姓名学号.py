import requests 
import os
from bs4 import BeautifulSoup
url = 'http://csujwc.its.csu.edu.cn/common/user_student_all.jsp'
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Content-Length': '4269',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': 'pgv_pvi=2969248768; _ga=GA1.3.1968776485.1498125951; _gid=GA1.3.1970267151.1522855404; JSESSIONID=69AB41032D567ACA4BFBB9BC4D89F8C8; BIGipServerpool_jwctest=2017969610.20480.0000',
	'Host': 'csujwc.its.csu.edu.cn',
	'Origin': 'http://csujwc.its.csu.edu.cn',
	'Referer': 'http://csujwc.its.csu.edu.cn/common/user_student_all.jsp',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

fp = open('E:\\info.txt','w',encoding='utf-8')
for i in range(1,8804) :
	data = {
	'PageNum': str(i)
	}
	bs = BeautifulSoup(requests.post(url,headers=headers,data=data).text,"lxml")
	bs1 = bs.find_all('div')[1].find('form').find_all('div')[3].find('tbody')
	for tr in bs1 :
		tds = tr.find_all('td')
		fp.write(tds[2].text+'\n')
		fp.write(tds[3].text+'\n')
		fp.write(tds[5].text+'\n')
		fp.write(tds[6].text+'\n')
		fp.write(tds[7].text+'\n')
		fp.write('\n')
	print('第'+str(i)+'页爬取完毕')