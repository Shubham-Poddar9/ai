
import requests
from PIL import Image,ImageDraw

model = "facebook/detr-resnet-101"

url = f"https://router.huggingface.co/hf-inference/models/{model}"

api=""

path = input("enter the path of the image")

with open(path,'rb') as file:
    image=file.read()

headers={
    "Authorization":f'Bearer {api}',
    "Content-Type":'image/png'
}

response=requests.post(url,headers=headers , data=image)

if response.status_code != 200:
    print ("error",response.text)
    exit()

detections =response.json()
image1=Image.open(path)
draw=ImageDraw.Draw(image1)

for obj in detections:
    if obj["score"]>0.1:
        box=obj["box"]
        x1=box["xmin"]
        y1=box["ymin"]
        x2=box["xmax"]
        y2=box["ymax"]

        draw.rectangle([x1,y1,x2,y2],outline="green",width=4)
        draw.text([x1+30,y1+30],obj['label'],fill="blue")

print("do you want to save the image")
choice=input("y or n").strip().lower()
if choice=="y":
    out="image.jpg"
    image1.save(out)
    print("image is saved")

for obj in detections:
    score=obj.get("score",0)
    if (score>0.1):
        print(obj["label"])

image1.show()