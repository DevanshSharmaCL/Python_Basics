import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    speak("Hello, I am listening to you.")
    print("🎤 Listening...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    speak(f"You said: {text}")
    print("You said:", text)
except sr.UnknownValueError:
    speak("Sorry, I did not understand.")
except sr.RequestError:
    speak("Speech service is down.")
