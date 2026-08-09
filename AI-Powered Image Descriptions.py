import base64, requests 


api=""

url = "https://router.huggingface.co/v1/chat/completions"

models = [

"zai-org/GLM-4.5V",

"Qwen/Qwen2.5-VL-72B-Instruct",

"Qwen/Qwen2.5-VL-32B-Instruct"

]

img=input("give name of image")or "o.jpg"

with open(img,"rb")as f:
    b64 = base64.b64encode(f.read()).decode()


headers={
    "Authorization": f"Bearer {api}",
    "Content-Type": "application/json"

}

for model in models:
    print("\n Trying this ", model)

    payload={
        "model":model,
        "messages":[{
            "role":"user",
            "content":[
                {"type":"text","text":"give a short caption "},
                {"type":"image_url",
                 "image_url":{"url":f"data:image/png;base64,{b64}"}}
            ]
        }]
    }

    r=requests.post(url,headers=headers, json=payload ,timeout=120)
    if r.status_code ==200:
        print(r.json()["choices"][0]["message"]["content"])
        break
    else:
        print ("it failed",r.status_code,r.text)

