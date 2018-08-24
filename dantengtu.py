import requests
from bs4 import BeautifulSoup
import os


url = 'http://www.91guohuaw.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
images = soup.find_all('div', class_='img-holder')
for image in images:
	image_url = image.a.img['src']
	with open(image_url.split('/')[-1],'wb') as fp:
		image_content = requests.get(image_url).content
		fp.write(image_content)