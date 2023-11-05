from flask import Flask, jsonify
import speech_recognition as sr
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

@app.route('/book', methods=['GET'])
def book():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    # Ask for name
    engine.say("Give me your name")
    engine.runAndWait()
    with sr.Microphone() as source:
        try:
            name_audio = r.listen(source, timeout=5, phrase_time_limit=5)
            name = r.recognize_google(name_audio)
        except sr.WaitTimeoutError:
            engine.say("Sorry, I didn't hear your name. Please try again.")
            engine.runAndWait()
            return jsonify({'status': 'Error', 'message': 'No input detected for name.'}), 400

    # Ask for item to book
    engine.say("What do you want to book? We have grapes, apple, mango, banana.")
    engine.runAndWait()
    with sr.Microphone() as source:
        try:
            item_audio = r.listen(source, timeout=5, phrase_time_limit=5)
            item = r.recognize_google(item_audio)
        except sr.WaitTimeoutError:
            engine.say("Sorry, I didn't hear your item choice. Please try again.")
            engine.runAndWait()
            return jsonify({'status': 'Error', 'message': 'No input detected for item.'}), 400

    # Ask for address
    engine.say("Give me the address please")
    engine.runAndWait()
    with sr.Microphone() as source:
        try:
            address_audio = r.listen(source, timeout=5, phrase_time_limit=5)
            address = r.recognize_google(address_audio)
        except sr.WaitTimeoutError:
            engine.say("Sorry, I didn't hear your address. Please try again.")
            engine.runAndWait()
            return jsonify({'status': 'Error', 'message': 'No input detected for address.'}), 400

    # Confirm order
    engine.say(f"Your order is: {item} for {name} to be delivered at {address}. Do you want to change anything?")
    engine.runAndWait()
    with sr.Microphone() as source:
        try:
            confirm_audio = r.listen(source, timeout=5, phrase_time_limit=5)
            confirm = r.recognize_google(confirm_audio)
        except sr.WaitTimeoutError:
            engine.say("Sorry, I didn't hear your confirmation. Please try again.")
            engine.runAndWait()
            return jsonify({'status': 'Error', 'message': 'No input detected for confirmation.'}), 400

    if confirm.lower() == 'no':
        engine.say("Your order is confirmed. Your order number is one.")
        engine.runAndWait()
        return jsonify({'status': 'Order confirmed', 'order_number': 1, 'message': 'Your order is confirmed. Your order number is one.'}), 200
    else:
        return jsonify({'status': 'Order not confirmed', 'message': 'Order not confirmed.'}), 200

if __name__ == '__main__':
    app.run(port=5000)
