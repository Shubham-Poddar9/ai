from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image

models = [

"ByteDance/SDXL-Lightning",

"stabilityai/stable-diffusion-xl-base-1.0",

"stabilityai/sdxl-turbo",

"runwayml/stable-diffusion-v1-5"

]

api="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"
client=InferenceClient(api_key=api)
print("primary model",models[0])
print("type q to exit")

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
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        file=f"generated_{timestamp}.jpg"
        image.save(file)
        print("image is generated")
        image.show()

    else:
        print("there is an error")
