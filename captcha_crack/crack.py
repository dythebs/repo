import numpy as np
import os
from PIL import Image, ImageFilter
import scipy.misc

class template:
	def __init__(self, fname):
		self.array = scipy.misc.imread(fname)
		fname = os.path.split(fname)[-1]
		self.real_num = fname[0]
		self.type = fname[2]
		self.white_num = 0
		h, w = self.array.shape
		for i in range(h):
			for j in range(w):
				if self.array[i, j] > 200:
					self.array[i, j] = 1
				else:
					self.array[i, j] = 0
				if self.array[i, j] == 1:
					self.white_num += 1
	#将一个模板和输入图像对比
	def check(self, testarray):
		h, w = self.array.shape
		cover = 0
		white_num = 0
		for i in range(h):
			for j in range(w):
				if self.array[i, j] == 1 and testarray[i, j] == 1:
					cover += 1
				if testarray[i, j] == 1:
					white_num += 1
		#如果数字面积差太多直接抛弃
		if abs(white_num - self.white_num) > 20:
			return -1
		#数字部分的重合度和面积差加权
		return cover / self.white_num - 2*(abs(white_num - self.white_num) / self.white_num )
#读取模板
templates = []
for root, dirs, files in os.walk('.\\template'):
	for file in files:
		templates.append(template(os.path.join(root, file)))
#找出最匹配的模板
def get_num(array):
	target = templates[0].real_num
	score = 0
	for t in templates:
		new_score = t.check(array)
		if new_score > score:
			score = new_score
			target = t.real_num
	return target

def crack(content):
	#将图像二值化
	with open('code.jpg','wb') as f:
		f.write(content)
	image = Image.open('code.jpg').filter(ImageFilter.MedianFilter).filter(ImageFilter.MedianFilter).convert('L')
	image = np.array(image)
	width, height = image.shape
	#这里写反了，和另一个地方的二值化刚好相反
	for i in range(width):
		for  j in range(height):
			if image[i,j] > 200 :
				image[i,j] = 0
			else:
				image[i,j] = 1

	ans = ''
	for i in range(4):
		subarray = image[:,i*44:(i+1)*44]
		ans += str(get_num(subarray))
	return ans
