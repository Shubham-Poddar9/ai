import pyaudio
import wave, speech_recognition as sr, numpy as np,threading, matplotlib.pyplot as plt

rate=16000
chunk=1024
format=pyaudio.paInt16
channels=1
filename=input("enter desired file name ")
filename=filename+".wav"
print("recording... press enter to stop")
p=pyaudio.PyAudio()


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

o=b"".join(frames)
s=np.frombuffer(o,dtype=np.int16)
max1=np.max(s)
min1=np.min(s)
peak=np.max(np.abs(s))
avg=np.mean(np.abs(s))
print("\naudio amplitude")
print("maximum",max1)
print("minmun",min1)
print("peak amplitude ",peak)
print("average amplitude ", round(avg,2))

time=np.arange(len(s))/rate
plt.figure(figsize=(12,5))
plt.plot(time,s)
plt.title("time (seconds)")
plt.xlabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()