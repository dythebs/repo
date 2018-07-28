import input_data
import tensorflow as tf
import numpy as np  
import os
np.set_printoptions(threshold=np.inf)  
#进行一次卷积操作
def conv2d(x, W):
	return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


#读入数据
mnist = mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
sess = tf.Session()
Saver = tf.train.import_meta_graph('./model/model.meta')
Saver.restore(sess,tf.train.latest_checkpoint('./model/'))
batch_xs,batch_ys = mnist.train.next_batch(1)
#计算精度
accuracy,a2,W1,b1,x_image,x = sess.run(['Mean:0','Relu:0','Variable:0','Variable_1:0','Reshape:0','Placeholder:0'],feed_dict={'Placeholder:0':batch_xs,'Placeholder_2:0':batch_ys,'Placeholder_1:0':1.0})
z2_tmp = conv2d(x_image,W1) + b1
z2_tmp = sess.run(z2_tmp)
################################
#半成品，只能搞1维的
#O(m*n^2)效率贼低
#搞了半天就跟我说不干了，难过
def check(base,target):
	for i in range(-2,3) :
		for j in range(-2,3) :
			if base + i*28 + j == target :
				return True,i+2,j+2
	return False,-100,-100
bias = b1.flatten()
for i in range(784-1):
	bias = np.hstack((bias,b1))

left_mat = np.array(np.zeros([784*32,784]))

kernels = W1[:,:,0,:]
list = []
last_zero = -100
for i in range(784):
	for j in range(784):
		valid, m, n = check(i,j)
		if not valid:
			for k in range(32):
				left_mat[i*32+k,j] = 0
		else:
			for k in range(32):
				left_mat[i*32+k,j] = kernels[:,:,k][m][n]


################################



hh = np.dot(left_mat,x.T).flatten()
print(hh.shape)
print(bias.shape)
hh = hh + bias
print(hh.shape)
#最后这俩相减约等于0，说明Wx+b和卷积运算是等价的
print(z2_tmp.flatten()-hh.flatten())