# These are the libraries I need to import for this.
import os
from gtts import gTTS

# This asks you for your name, and adds it to a variable.
text = input("Enter the text you want to read.")

# This produces and plays the text you want to read.
os.remove("Python\TextToScream\LatestReadout.wav")
tts = gTTS(text, tld='com')
tts.save("Python\TextToScream\LatestReadout.wav")
os.system("Python\TextToScream\LatestReadout.wav")