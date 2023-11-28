import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os

# Create a recognizer object
r = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Could you please tell me your name?")
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from the Google Speech Recognition service; {0}".format(e))

def speak(text):
    
    tts = gTTS(text=text, lang='en')
    engine.say(tts)
    tts.save("output.mp3")
    # os.system("mpg321 output.mp3")  

# Example usage
while True:
    input_text = listen()
    if input_text:
        print("User: ", input_text)
        speak("Okay, so your name is " + input_text)
        engine.runAndWait()
    else:
        speak("Sorry, I didn't hear anything. Can you please repeat?")
