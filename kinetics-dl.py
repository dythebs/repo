import youtube_dl
import pandas as pd 
import requests
import os
import zipfile
from threading import Thread

url = 'https://deepmind.com/documents/66/kinetics_train.zip'
meta_path = 'meta'
video_path = 'video'
thread_num = 5
ydl_opts = ({'format': '18/134/135',
		'proxy': '127.0.0.1:1080', # 默认HTTP代理
		'outtmpl': os.path.join(video_path,'%(id)s.%(ext)s')})

def maybedownload():
	if not os.path.exists(meta_path):
		os.mkdir(meta_path)
	filename = url.split('/')[-1]
	if not os.path.exists(os.path.join(meta_path, filename)):
		with open(os.path.join(meta_path, filename), 'wb') as fp:
			fp.write(requests.get(url).content)
	else:
		pass

	with zipfile.ZipFile(os.path.join(meta_path, filename), 'r') as fp:
		fp.extractall(path=meta_path)

def read_csv():
	filename = url.split('/')[-1].split('.')[0]
	df = pd.read_csv(os.path.join(meta_path, filename, filename+'.csv'))['youtube_id']
	id_list = list(df)
	return id_list




def download(vid):
	# retrieve video information
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		video = ydl.download(['https://www.youtube.com/watch?v='+vid])


def task(vids):
	for vid in vids:
		try:
			download(vid)
		except Exception as e:
			pass
		else:
			pass
		finally:
			pass

maybedownload()
id_list = read_csv()
threads = []

for i in range(thread_num):
	total = len(id_list)
	deal_num = total // thread_num
	if i != thread_num -1:
		start = i*deal_num
		end = (i+1)*deal_num
	else:
		start = i*deal_num
		end = total
	t = Thread(target=task, args=(id_list[start:end],))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

