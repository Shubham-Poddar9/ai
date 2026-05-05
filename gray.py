import cv2
image=cv2.imread(r"C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
a=cv2.resize(gray,(224,224))
cv2.imshow("grey scale image",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(a.shape)