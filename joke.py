import requests

def a():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        print("JSON RESPONSES",response.json())

        joke_data=response.json()

        return f"{joke_data['setup']} - {joke_data['punchline']}"
    
    else:
        return "error"
    

def main():
    print("welcome")
    
    while True:
        choice=input("press enter to get new joke,or q to quit or exit").strip().lower()

        if choice in ("q","exit"):
            print("bye")
            break
        else:
            z=a()
            print(z)

main()