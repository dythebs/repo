import cv2
import numpy as np
import matplotlib.pyplot as plt 
import imageio

cap = cv2.VideoCapture("v_CricketShot_g04_c01.avi")
plt.ion() 
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
p_flow = cv2.DualTVL1OpticalFlow_create()
gif = []
while True:
	ret, frame2 = cap.read()
	if frame2 is None:
		break
	next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
	
	flow = p_flow.calc(prvs, next, None)
	flow[flow > 20] = 20
	flow[flow < -20] = -20
	flow = flow / 20.
	flow = np.c_[flow, np.zeros((240, 320, 1))] + 0.5
	gif.append(flow)
	prvs = next

cap.release()

imageio.mimsave('1.gif', gif)