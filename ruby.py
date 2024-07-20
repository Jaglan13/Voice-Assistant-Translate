import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import urllib.parse

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I am Ruby. How can I assist you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any relevant information.")

        elif "thank you" in query:
            speak("You're welcome!")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            speak(f"The time is {current_time}")

        elif 'music' in query:
            music_dir = "E:/E_drive files/pendrive/song"
            songs = os.listdir(music_dir)
            if songs:
                random_song = os.path.join(music_dir, random.choice(songs))
                os.startfile(random_song)
            else:
                speak("No music files found in the directory.")

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'open browser' in query:
            webbrowser.open("https://www.mozilla.org/firefox/")

        elif 'open notepad' in query:
            os.system("start notepad")

        elif 'open calculator' in query:
            os.system("start calc")

        elif 'open file explorer' in query:
            os.system("explorer")

        elif 'open control panel' in query:
            os.system("control")

        elif 'shutdown' in query:
            speak("Shutting down...")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("Restarting...")
            os.system("shutdown /r /t 1")

        elif 'play music on youtube' in query:
            query = query.replace('play music on youtube', '')
            query = urllib.parse.quote(query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'search in google' in query:
            query = query.replace('search in google', '')
            query = urllib.parse.quote(query)
            webbrowser.open(f"https://www.google.com/search?q={query}")
            
        elif 'open ms word' in query:
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")

        elif 'open powerpoint' in query:
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")

        elif 'open visual studio code' in query:
            os.system("code")

        elif 'bye' in query:
            speak("Goodbye!")
            break
