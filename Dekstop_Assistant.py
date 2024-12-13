import pyttsx3
import speech_recognition as sr
import os
import webbrowser
from datetime import datetime

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio from the microphone and recognize it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("There seems to be an issue with the speech recognition service.")
        return ""

def open_application(app_name):
    """Open a specified application."""
    try:
        if "notepad" in app_name:
            os.system("notepad")
        elif "calculator" in app_name:
            os.system("calc")
        elif "calender" in app_name:
            os.system("calender")
        elif "chrome" in app_name:
            # Open Google Chrome
            webbrowser.open("https://www.google.com/chrome/")
        elif "youtube" in app_name:
            # Open YouTube in the default web browser
            webbrowser.open("https://www.youtube.com/")
        elif "spotify" in app_name:
            # Open Spotify (requires Spotify app installed)
            os.system("start spotify")    
        else:
            speak(f"Sorry, I can't open {app_name} right now.")
    except Exception as e:
        speak("An error occurred while trying to open the application.")

def announce_date_time():
    """Announce the current date and time."""
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}, and the time is {current_time}.")


if __name__ == "__main__":
    while True:
        speak("Would you like to do? Say 'speak', 'listen', 'open', , 'date and time'. Say 'exit' to quit.")
        choice = listen()

        if "exit" in choice:
            speak("Goodbye!")
            break

        elif "speak" in choice:
            speak("Please type the text you want me to say.")
            text = input("Enter text: ")
            speak(text)

        elif "listen" in choice:
            speak("Please say something, and I will repeat it back.")
            command = listen()
            if command:
                speak(f"You said: {command}")

        elif "open" in choice:
            speak("Please say the name of the application to open. For example, Notepad or Calculator.")
            app_name = listen()
            open_application(app_name)

        elif "date" in choice or "time" in choice:
            announce_date_time() 

       

        else:
            speak("I did not understand your choice. Please try again.")
