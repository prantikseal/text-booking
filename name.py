import tkinter as tk
import speech_recognition as sr
import pyttsx3

def get_name():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        name = recognizer.recognize_google(audio)
        output_label.config(text=f"Your name is {name}.")
        engine = pyttsx3.init()
        engine.say(f"Your name is {name}.")
        engine.runAndWait()
    except sr.UnknownValueError:
        output_label.config(text="Sorry, I didn't catch that.")
    except sr.RequestError:
        output_label.config(text="Sorry, I'm having trouble with speech recognition.")

# Create the GUI
window = tk.Tk()
window.title("Voice Input/Output")
window.geometry("400x200")

input_label = tk.Label(window, text="Click the button and say your name:")
input_label.pack(pady=20)

button = tk.Button(window, text="Ask", command=get_name)
button.pack()

output_label = tk.Label(window, text="")
output_label.pack(pady=20)

window.mainloop()
