import random
destination={
    "beaches":["bali","phuket","maldives"],
    "mountains":["everest","k2","himalayas"],
    "cites":["goa","kathmandu","pokhara"]
}
jokes=["What do you call a magic dog? A labracadabrador",
"What do you call a cow with no legs? Ground beef",
"How do you make an octopus laugh? With ten-tickles"]

def recomend():
    pre=input("enter beaches, mountains or cites")
    if (pre in destination):
        place=random.choice(destination[pre])
        print("try this",place)
    else:
        print('invalid choice')

def packing():
    days=input("enter the no days")
    place=input("enter the place ")
    print(f"enjoy your holidays at this {place} for these {days}")

def chat():
 while True:
    msg=input("enter from recomend, packing or joke")
    if "recomend"in msg:
        recomend()
    elif "joke" in msg:
        print(random.choice(jokes))
    elif "packing" in msg:
        packing()
    elif msg in ["exit","bye"]:
        print("good bye")
        break
    else:
        print("enter from recomend, packing or joke ")
chat()

       

    