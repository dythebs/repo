import requests
from bs4 import BeautifulSoup
import os
import threading
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI'
}
dir = 'Content'


def get_filename_from_href(href) :
    return href.split('/')[-1]


def get_a_pic(href,dirname):
    content = requests.get(href).content
    with open(os.path.join(dir,dirname,get_filename_from_href(href)), 'wb') as fp:
        fp.write(content)


def check_exists(dirname):
    return os.path.exists(os.path.join(dir,dirname))


def trim(title) :
    start = 0
    end = len(title)
    while title[start] == ' ' or title[start] == '\n' or title[start] == '\r':
        start += 1
    while title[end-1] == ' ' or title[end-1] == '\n' or title[end-1] == '\r':
        end -= 1
    return title[start:end].replace('\t','').replace('/','')


def get_a_set_of_images(href):
    baseurl = 'http://www.iyuanqi.com'
    url = baseurl + href
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    title = trim(soup.html.head.title.text)
    if check_exists(title) :
        return
    os.mkdir(os.path.join(dir, title))
    print('Downloading', title)
    images = soup.find('div',class_='post-content from-pc').find_all('img')
    threads = []
    for image in images :
        t = threading.Thread(target=get_a_pic,args=(image['src'],title))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if not os.path.exists(dir):
    os.mkdir(dir)
for i in range(8) :
    baseurl = 'http://www.iyuanqi.com/home/funimg/fun_list/m/Home/cp_uid/18976/p/'
    url = baseurl + str(i+1) + '.html'
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find('div',class_='clearfix crop-margin module-compere').find_all('figure')
    threads = []
    for link in links :
        get_a_set_of_images(link.a['href'])
