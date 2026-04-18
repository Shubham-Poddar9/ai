print("Welcome to chat bot")
name = input("please enter your name?")
print(f"Nice to meet you {name}")
mood = input ("how are you feeling today? (good or bad)")
if (mood== "good"):
    print("nice to hear that you are feeling",mood)
elif (mood=="bad"):
    print("sorry to hear that you are",mood)
else:
    print("Invalid! please enter good or bad")
print("Thankyou nice chatting with you ",name)
