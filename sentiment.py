from textblob import TextBlob
import colorama
from colorama import Fore
colorama.init()
text=input("please enter your text")
a = TextBlob(text)
b= a.sentiment.polarity
if (b>0):
    print(Fore.GREEN,"sentence is positive",b)
elif (b<0):
    print(Fore.RED,"sentence is negative",b)
else:
    print("neutral",b)

