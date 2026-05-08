import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread(r'C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg')
a=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
(h,w)=image.shape[:2]

center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,270,0.7)
b=cv2.warpAffine(image,m,(w,h))
c=cv2.cvtColor(b,cv2.COLOR_BGR2RGB)
plt.imshow(c)
plt.show()

z=np.ones(image.shape,dtype="uint8")*100
s=cv2.add(image,z)
d=cv2.cvtColor(s,cv2.COLOR_BGR2RGB)
plt.imshow(d)
plt.show()