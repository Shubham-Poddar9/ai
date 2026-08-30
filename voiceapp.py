import speech_recognition as sr
from googletrans import Translator

def stt():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("speak in english ")
        audio=r.listen(source)


    try:
        text=r.recognize_google(audio,language="en-US")
        print("you said: ",text)
        return text

    except:
        print("could not understand ")
        return""


def tt(text):
    translator = Translator()
    result=translator.translate(text,src="en",dest="zh-cn")
    print("china",result.text)

text=stt()

if text:
    tt(text)