import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize recognizer & TTS engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    print(f"🤖 Bot: {text}")
    tts.say(text)
    tts.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            print("🎤 Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # Speech to text
        user_input = recognizer.recognize_google(audio)
        print(f"🗣 You: {user_input}")

        # Handle commands
        if user_input.lower() == "hello":
            speak("Hello there! How are you today?")
        
        elif user_input.lower() == "what's the time":
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif user_input.lower() == "exit":
            speak("Goodbye! Have a great day.")
            break

        else:
            speak(f"You said: {user_input}")

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
