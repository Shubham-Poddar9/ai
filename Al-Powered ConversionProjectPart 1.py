from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import torch
import requests
from PIL import Image
from io import BytesIO
import os
device = 'cuda' if torch.cuda.is_available() else 'cpu'
processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
pipe = pipeline('text-generation',model='gpt2', tokenizer = 'gpt2', device = 0 if device == 'cuda' else -1 , return_full_text= True)

def generate(path):
    image = Image.open(path).convert('RGB')
    p = processor(images = image, return_tensors = 'pt').to(device)
    out = model.generate(**p,max_new_tokens = 50)
    caption = processor.decode(out[0], skip_special_tokens = True)
    return caption

def fun(prompt,new_tokens):
    result = pipe(prompt, max_new_tokens = new_tokens, num_return_sequences = 1, truncation = True)
    if isinstance(result,list):
        if 'generated_text' in result[0]:
            return result[0]['generated_text']
        elif 'text' in result[0]:
            return result[0]['text']
    else:
        return 'Failed'

def truncate(words, word_limit):
    word = words.strip().split()
    return " ".join(word[:word_limit])
print("Select your choice")
print('1. caption 5 words')
print("2. Description 50 words")
print("3.Summary 100 words")
print('4. Exit')

inp = input("Enter your image: ")
if not os.path.exists(inp):
    print("Invalid image")
    exit()
try:
    g = generate(inp)
    print(g)

except Exception as e:
    print("Error Occured", e)

choice = input("Enter your choice: ")
if(choice == '1'):
    a = truncate(g,5)
    print(a)

elif choice == '2':
    des = fun(g,50)
    print(truncate(des,50))

elif( choice == '3'):
    de = fun(g,100)
    print(truncate(de,100))

else:
    exit()