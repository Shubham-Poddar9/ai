import requests

url="https://uselessfacts.jsph.pl/random.json?language=en"

def a ():
    response=requests.get(url)
    if response.status_code ==200:
        fact_data=response.json()
        print(fact_data['text'])
    else:
        print("unable to genrate")

while True:
    s=input("press enter to get fact or type 'Q' to quit")
    if s.capitalize()=='Q':
        break

    a()