import speech_recognition as sr
import pyttsx3
from googletrans import Translator
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setproperty('rate', 150) 
    voices = engine.getproperty('voices')
    if language == "en":
        engine.setproperty('voices', voices[0].id)
    else:
        engine.setproperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWaiit()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source: 
        print("pls speak now in english")
        audio = recognizer.listen(source)
        try:
           print("???? Recognizing speech...")
    
           text = recognizer.recognize_google(audio, language="en-US")
           print(f"you said: {text}")
           return text
        except sr.UnknownValueError:
          print("Could not understand the audio.")
        except sr.UnknownValueError:
            print("could not understand the audio")
        except sr.RequestError as e:
            print(f"API Error: {e}")
            return ""
def translate_text(text, target_languages="os"):
    translator = Trueranslator()
    translation = translator.translate(text, dest=target_language)
    print(f"???? Translated text: {translation.text}")
    return translation.text
def display_language_options():
    print("")

           
            