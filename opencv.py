import cv2
import numpy as np

# print(cv2.getVersionString())#获取opencv版本号

# image=cv2.imread("3.jpg")#读取图像
# print(image.shape)#输出图像大小
#
# cv2.imshow("image",image)
# cv2.waitKey()

# cv2.imshow("blue",image[:,:,0])#读取指定颜色下的图像
# cv2.imshow("green",image[:,:,1])
# cv2.imshow("red",image[:,:,2])
#
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #灰度，三原色平均值
# crop=image[0:500,0:1000]
# cv2.imshow("crop",crop)

# image=np.zeros([300,300,3],np.uint8)
#
# cv2.line(image,(100,200),(250,250),(255,0,0),2)
# cv2.rectangle(image,(30,100),(60,150),(0,255,0),2)
# cv2.circle(image,(100,200),50,(0,0,255),2)
# cv2.putText(image,"hello",(100,50),0,1,(255,255,255),2,1)
# cv2.imshow('image',image)
image=cv2.imread('3.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,500,0.1,10)
for i in corners:
    x,y=i.ravel()
    cv2.circle(image,(int(x),int(y)),3,(255,0,255),-1)
cv2.imshow('corner',image)

cv2.waitKey()