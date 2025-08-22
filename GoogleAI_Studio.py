import speech_recognition as sr
import subprocess
import os

def listen_for_command():
    """Listens for a voice command and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def open_file_explorer():
    """Opens the default file explorer for the current operating system."""
    if os.name == 'nt':  # For Windows
        subprocess.run(['explorer'])
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.run(['open', '.'] if 'darwin' in os.sys.platform else ['xdg-open', '.'])
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    while True:
        command = listen_for_command()
        if "open file explorer" in command:
            print("Opening file explorer...")
            open_file_explorer()
        elif "exit" in command or "quit" in command:
            print("Exiting the program.")
            break