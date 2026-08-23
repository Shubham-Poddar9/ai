import pyaudio
import speech_recognition as sr
import wave
import threading

rate=16000
chunk=1024
format=pyaudio.paInt16
channels=1
filename=input ("enter a file name:- ")
filename=filename+".wav"
print("press enter to spot recording")

p=pyaudio.PyAudio()
stream=p.open(format=format,channels=channels,rate=rate,input=True,frames_per_buffer=chunk)
frames=[]
stop=False

def stopRecording():
    global stop
    input()
    stop=True

threading.Thread(target=stopRecording).start()

while not stop:
    frames.append(stream.read(chunk))
stream.stop_stream()
stream.close()
p.terminate()
print("recording has stopped ")

with wave.open(filename,"wb")as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))

print("recording stopped")

recogniser =sr.Recognizer()
with sr.AudioFile(filename) as src:
    audio=recogniser.record(src)

try:
    text=recogniser.recognize_google(audio)
    print(f"transcription : {text}")

except:
    print("could not transcribe!")