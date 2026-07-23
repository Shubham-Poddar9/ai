import requests
from colorama import Fore,init

init(autoreset=True)
url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
api=""

def summarize(x):
    r=requests.post(url,headers={"Authorization":f"Bearer {api}"},json={"inputs":f"{x}"})
    
    try:
        return r.json()[0]['summary_text']
    except:
        return "error"

print(Fore.MAGENTA+"Welcome to the text summarizier")
name = input(Fore.GREEN+"Enter your name: ").strip().title()
text=input(Fore.CYAN+"enter your text: ").strip()
if not text:
    print(Fore.RED+"no text entered!!!!!!!!!!!!!!")

else:
    s=summarize(text)
    if s:
        print(Fore.LIGHTGREEN_EX+s)
    else:
        print(Fore.LIGHTRED_EX+"could not genrate ")