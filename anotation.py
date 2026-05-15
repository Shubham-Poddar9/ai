import cv2 
import matplotlib.pyplot as plt


image=cv2.imread(r'C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
h,w,_ = image.shape
cv2.rectangle(image,(20,20),(170,170),(243,67,78),-3)

c1=(95,95)
c2=(95,1335)

cv2.circle(image,c1,50,(54,69,87),-7)

cv2.circle(image,c2,50,(194,179,186),-5)

cv2.line(image,c1,c2,(255,0,0),8)

font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(image,"its meee",(515,1388),font,2.5,(67,33,18),5)

start,end=(w-50,20),(w-50,h-20)
cv2.arrowedLine(image,start,end,(0,0,255),8)
plt.figure(figsize=(10,6))
plt.imshow(image)
plt.axis("off")
plt.show()

