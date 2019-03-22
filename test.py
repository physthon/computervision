import numpy as np
from pylab import *
from PIL import Image
import json
from modules import function as fnc
from modules.classes import Flask
import sys
day = {
    'mon': "monday",
    'tue': "tuesday",
    'wed': "wednesday",
    'thu': "thursday",
    'fri': "friday",
    'sat': "saturday",
    'sun': "sunday"
}

a = type(day)
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
z = json.dumps(y)

str_day = json.dumps(day, indent=4)

# f = open('test2.py', 'w')
# sys.stdout = f
# sys.stdout.write("print('hello')")
# f.close()

# Duyệt mảng trong numpy siêu nhanh
"""
    array = np.arange(10) cái này là tạo mảng liên tục từ 1 tới 10-1
    sau đó
    array[3:10] là duyệt nhanh các dữ liệu trong khoảng từ 3 tới 10

"""

# from threading import Thread
# import time

# class myThread(Thread):
#  	"""docstring for myThread"""
#  	def __init__(self, name, counter, delay):
#  		super(myThread, self).__init__()
#  		self.name= name
#  		self.counter=counter
#  		self.delay=delay

#  	def run(self):
#  		print("san sang chay" + self.name)
#  		while self.counter:
#  			time.sleep(self.delay)
#  			print("%s: %s" % (self.name, time.ctime(time.time())) )
#  			self.counter-=1
#  		print( "ket thuc vong lap", self.name)

# try:
#  	thread1 = myThread("thread 1", 10, 2)
#  	thread2 = myThread("thread 2", 10, 3)
#  	thread1.start()
#  	thread2.start()
# except:
#  	print( "Error")


def return2value(a, b):
    return a, b


# Xử lý ảnh


# convert('L') giúp chỉnh cho hình ảnh chuyển sang màu đen

"""Ma trân biểu diễn màu sắc:
    +Dòng đầu tiên mô tả 

"""
rgb2xyz = (
    0.6, 0.437580, 0.680423, 0,
    0.212671, 0.715160, 0.672169, 0,
    0.119334, 0.139193, 0.350227, 0
)
im = Image.open('static/img/camgiang.jpg').convert('L')
im = array(im)
gray()
def findOriginalPixel(angle,rowIndex,colIndex,centerX,centerY):
    x0 = np.cos(angle)*(colIndex - centerX) - np.sin(angle)*(rowIndex - centerY) + centerX
    y0 = np.sin(angle)*(colIndex - centerX) + np.cos(angle)*(rowIndex - centerY) + centerY
    return x0,y0

def rotate(img,angle):
    row,col = img.shape;angle = -angle
    rowOut = row + 600
    colOut = col + 600
    centerX = np.round(col/2);centerY = np.round(row/2)
    # index = np.around(img)
    # index = imgOut.astype(int)

    # imgOut
    imgOut = np.empty((rowOut,colOut))
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            x0 ,y0 = findOriginalPixel(angle,i,j,centerX,centerY)
            x0 = np.round(x0).astype(int); y0 = np.round(y0).astype(int)
            # if(x0 < 0): imgOut[k,m] =0
            # elif(x0 > col-1): imgOut[k,m] = 0
            # elif(y0 < 0): imgOut[k,m] = 0
            # elif(y0 > row -1): imgOut[k,m] = 0
            # else:
            imgOut[x0+300,y0+300] = img[i,j]
    return imgOut

imgOut = rotate(im,45)
imshow(imgOut)
show()


"""
     Nguyên nhẫn nhiễu ảnh là do làm tròn các số hạng trong khi xoay.
     từ đó t chọn cách xoay ảnh ngược để tránh nhiễu.
     Hoặc không sử dụng các phương pháp lọc để lọc nhiễu.
"""