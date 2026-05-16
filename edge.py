import cv2 
import numpy as np
import matplotlib.pyplot as plt 

def show (title,img):
    plt.imshow(img,cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()

def edge_dectation(image_path):
    image=cv2.imread(image_path) 
    if image is None:
        print("image not found")
        return
    else :
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        while True:
            print("1.sobel edge detection")
            print("2.canny edge detection")
            print("3.gaussian blur")
            print("4.exit")

            choice=input("enter your choice")
            if (choice=="1"):
                sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
                sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
                sobel=cv2.bitwise_or(np.uint8(np.absolute(sobelx)),np.uint8(np.absolute(sobely)))
                show("sobel edge detetion",sobel)

            elif (choice=="2"):
                low=int(input("enter low value"))
                high=int(input("enter high value"))
                edges=cv2.Canny(gray,low,high)
                show("canny edge detection",edges)
            elif (choice=="3"):
                k=int(input("enter kernal value"))
                blur=cv2.GaussianBlur(gray,(k,k),0)
                show("gaussian blur",blur)

            elif (choice=="4"):
                print("exiting")

            else:
                print("invalid choice")
                break
edge_dectation(r"C:\Users\shubham\Desktop\ai\lesson 1.cv\m.jpeg")