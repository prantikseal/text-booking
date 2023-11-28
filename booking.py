import speech_recognition as sr 
import pyttsx3
import logging

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

r = sr.Recognizer()
engine = pyttsx3.init()

# Ask for user's name
engine.say("Could you please tell me your name?")
engine.runAndWait()

with sr.Microphone() as source:
   print("Please say your name:")
   try:
       audio = r.listen(source, timeout=10) # Listen for 10 seconds
       name = r.recognize_google(audio)
       print("You said: " + name)
       logging.info('User name: ' + name)
   except sr.WaitTimeoutError:
       print("Sorry, you didn't say anything.")
       logging.error('WaitTimeoutError: User didn\'t say anything')
   except:
       print("Sorry, could not recognize your voice")
       logging.error('Could not recognize user voice')

# Ask for item to order
engine.say("What item would you like to order today?") 
engine.runAndWait()

item = None # Initialize item variable

with sr.Microphone() as source:
   print("Please say the item name:") 
   try: 
       audio = r.listen(source, timeout=10) # Listen for 10 seconds
       item = r.recognize_google(audio)
       print("You said:", item)
       engine.say("You said:", item)
       logging.info('Item to order: ' + item)
   except sr.WaitTimeoutError:
       print("Sorry, you didn't say anything.")
       logging.error('WaitTimeoutError: User didn\'t say anything')
   except:
       print("Could not recognize audio")
       logging.error('Could not recognize audio')

if name and item: # Check if both name and item are defined
   print("Confirming order for", name, item)
else:
   print("Could not confirm order due to incomplete information.")
