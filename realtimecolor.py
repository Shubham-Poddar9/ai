import cv2

def color_filter(img,f):
    if f=="red":
        img[:,:,0]=0
        img[:,:,1]=0

    elif f=="blue":
        img[:,:,1]=0
        img[:,:,2]=0

    elif f=="green":
        img[:,:,0]=0
        img[:,:,2]=0

    elif f=="yellow":
        img[:,:,0]=0

    elif f=="sobel":
        g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        sx=cv2.Sobel(g,cv2.CV_64F,1,0)
        sy=cv2.Sobel(g,cv2.CV_64F,0,1)
        img=cv2.cvtColor(cv2.bitwise_or(sx.astype("uint8"),sy.astype("uint8")),cv2.COLOR_GRAY2BGR)

    elif f=="canny":
        g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img=cv2.cvtColor(cv2.Canny(g,100,200),cv2.COLOR_GRAY2BGR)
    return img

cap=cv2.VideoCapture(0)
f="orignal"

print("r for red ,g for green, b for blue ,y for yellow,s for sobel,c for canny q for quit")

while True:
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("filters",color_filter(frame.copy(),f))

    k=cv2.waitKey(1) & 0xFF
    if k==ord("r"): f="red"
    elif k==ord("b"): f="blue"
    elif k==ord("g"): f="green"
    elif k==ord("y"): f="yellow"
    elif k==ord("s"): f="sobel"
    elif k==ord("c"): f="canny"
    elif k==ord("q"): break

cap.release()
cv2.destroyAllWindows()