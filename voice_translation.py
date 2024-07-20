import pyttsx3
import datetime
import speech_recognition as sr
from googletrans import Translator

def speak(audio, voice='male'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice == 'female':
        engine.setProperty('voice', voices[1].id)  # Index 1 for female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Index 0 for male voice
    engine.say(audio)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio, language='en-IN')
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))
        return None

def translate_text(text, target_language='en'):
    if target_language == 'haryanvi':
        # You can add your own translation logic for Haryanvi here
        translated_text = "This is a Haryanvi translation placeholder."
    else:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        translated_text = translated_text.text
    return translated_text

def detect_language(text):
    translator = Translator()
    detected_language = translator.detect(text).lang
    return detected_language

def select_language():
    print("Which language would you like to translate into?")
    print("1. Hindi (hi)")
    print("2. Bengali (bn)")
    print("3. Telugu (te)")
    print("4. Marathi (mr)")
    print("5. Tamil (ta)")
    print("6. Urdu (ur)")
    print("7. Gujarati (gu)")
    print("8. Kannada (kn)")
    print("9. Odia (or)")
    print("10. Malayalam (ml)")
    print("11. Punjabi (pa)")
    print("12. Assamese (as)")
    print("13. Maithili (mai)")
    print("14. Santali (sat)")
    print("15. Kashmiri (ks)")
    print("16. Nepali (ne)")
    print("17. Haryanvi (hr)")
    target_language = input("Enter language code: ").strip().lower()
    return target_language

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I assist you today?", voice='female')
    speak("Please provide your command.", voice='female')
    

    while True:
        user_input = recognize_speech()
        
        if not user_input:
            continue
        
        speak(f"You said: {user_input}", voice='female')
        
        target_language = select_language()
        
        translated_text = str(translate_text(user_input, target_language))
        print(translated_text)
        speak(f"The translated text is ", voice='female')
        speak(translated_text,voice='female')
        # speak(, voice='female')  # Speak the translated text
        
        response = input("Do you want to continue? (yes/no): ").lower()
        if response != 'yes':
            speak("Goodbye!", voice='female')
            break
