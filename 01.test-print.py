print("hello World")
# import Image
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# 使用这个绘制出现界面，just like cv

import time


i = Image.open('images/dotndot.png')
iar = np.asarray(i) # 将i作为数组赋值给ia
print(iar) # 打印iar

print(iar[0])
print(iar[0,0])
print(iar[0,0,0])


'''print("start cv2")
import cv2
img = cv2.imread('images/sentdex.png')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("end cv2")

plt.imshow(iar)
plt.show();

print("start show figure")'''

# image recognition

from functools import reduce

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            # print(eachPix)
            # time.sleep(5)
            avgNum = reduce(lambda x, y: x + y, eachPix[:3])/ len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr)/ len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
             if reduce(lambda x, y: x + y, eachPix[:3])/ len(eachPix[:3]) > balance:
                 eachPix[0] = 255
                 eachPix[1] = 255
                 eachPix[2] = 255
                 eachPix[3] = 255
             else:
                 # read only... this can't change
                 eachPix[0] = 0
                 eachPix[1] = 0
                 eachPix[2] = 0
                 eachPix[3] = 255
                
            
threshold(iar)
plt.imshow(iar)
plt.show()

'''print("finish function")

i1 = Image.open('images/dot.png')
iar1 = np.asarray(i1) # 将i作为数组赋值给ia

i2 = Image.open('images/dotndot.png')
iar2 = np.asarray(i2) # 将i作为数组赋值给ia

i3 = Image.open('images/sentdex.png')
iar3 = np.asarray(i3) # 将i作为数组赋值给ia

i4 = Image.open('images/blank.png')
iar4 = np.asarray(i4) # 将i作为数组赋值给ia

print("start show")

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4,colspan=3)
# 第一个参数表示将其划分为8*6的网格，其中处于位置0,0处，行占4格，列占3格
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4,colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4,colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4,colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''


