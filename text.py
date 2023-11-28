import speech_recognition as sr
from gtts import gTTS
import pyttsx3

# Create a recognizer object
r = sr.Recognizer()
engine = pyttsx3.init()

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
    tts.save("output.mp3")
    engine.say(text)
    engine.runAndWait()

def book_room():
    speak("Welcome to the hotel booking system.")
    speak("What is your name?")
    user_name = listen()
    
    # Check if user_name is None and ask to repeat
    while user_name is None:
        speak("Sorry, I didn't hear your name. Can you please repeat?")
        user_name = listen()

    speak(f"Thank you, {user_name}.")

    speak("How many people will be staying?")
    num_people = listen()
    
    # Check if num_people is None and ask to repeat
    while num_people is None:
        speak("Sorry, I didn't hear the number of people. Can you please repeat?")
        num_people = listen()
        print(num_people)

    speak(f"Great! {num_people} people.")

    speak("For how many days would you like to book the room?")
    num_days = listen()
    
    # Check if num_days is None and ask to repeat
    while num_days is None:
        speak("Sorry, I didn't hear the number of days. Can you please repeat?")
        num_days = listen()

    speak(f"Thank you, {user_name}. Your booking for {num_people} people for {num_days} days is confirmed. Thank you for booking with us")
    exit()

if __name__ == "__main__":
    while True:
        speak("Do you want to book a hotel room? Yes or no.")
        response = "yes"
        print(response)

        if response and "yes" in response.lower():
            book_room()
        elif response and "no" in response.lower():
            speak("Okay, have a great day!")
            break
        else:
            speak("Sorry, I didn't understand. Can you please say 'yes' or 'no'?")
