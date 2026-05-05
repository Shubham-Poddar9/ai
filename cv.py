import cv2 
image=cv2.imread(r"C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg")
cv2.namedWindow('loaded image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('loaded image',800,500)
cv2.imshow('loaded image',image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
print(image.shape)