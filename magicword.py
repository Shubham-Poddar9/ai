from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import ImageEnhance, ImageFilter

models = [
"black-forest-labs/FLUX.1-schnell",

"stabilityai/stable-diffusion-xl-base-1.0",

"stable-diffusion-v1-5/stable-diffusion-v1-5",

"CompVis/stable-diffusion-v1-4"
]

api=""
client=InferenceClient(api_key=api)
print("primary model",models[0])
print("type q to exit")

def post(image):
    image = ImageEnhance.Brightness(image).enhance(2.5)
    image = ImageEnhance.Contrast(image).enhance(1.7)
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return image
while True:
    prompt=input("enter your prompt").strip()
    if(prompt.lower()=='q'):
        print("exit")
        break

    if not prompt:
        continue

    print("generating images")
    image=None
    for model in models:
        try:
            image=client.text_to_image(prompt,model=model)
            break
        except Exception as e:
            print("error has occured",e)
            continue

    if image:
        print("applying image enhancement")
        image=post(image)
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        file=f"generated_{timestamp}.jpg"
        image.save(file)
        print("image is generated")
        image.show()

    else:
        print("there is an error")
