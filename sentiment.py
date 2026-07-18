import requests

api ="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"

url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

headers ={ "Authorization": f"Bearer {api}"}

while True:
    a=input("enter your sentance 1")
    if a.lower()== "exit":
        break

    b=input("enter your sentance 2")
    if b.lower()=="exit":
        break

    payload ={ "inputs":{"source_sentence":a, "sentences":[b]}}

    r= requests.post(url,headers=headers,json=payload)

    if r.ok:
        score=r.json()[0]
        print("score similarity is ",score,"%")

        if score >= 0.72:
            print("its duplicate")

        else:
            print("its diffrent")


    else:
        print("error",r.text)