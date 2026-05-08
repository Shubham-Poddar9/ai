import cv2
import matplotlib.pyplot as plt

image=cv2.imread(r'C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg')
a=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(a)
plt.show()
b=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(b)
plt.show()

crop=image[200:800,100:800]
c=cv2.cvtColor(crop,cv2.COLOR_BGR2RGB)
plt.imshow(c)
plt.show()