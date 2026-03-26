import speech_recognition as sr
import pyttsx3
from googletrans import Translator
engine = pyttsx3.init()
translator = Translator()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return""
def get_lang():
        langs = {
            "1": "hi", "2": "ta", "3": "te", "4": "bn",
            "5": "mr", "6": "gu", "7": "ml", "8": "pa"
        }
        print("1.Hindi 2.Tamil 3.Telugu 4.Bengail 5.Marathi 6.Gujarati 7.Malayalm 8.Punjabi")
        return langs.get(input("Choose: "), "hi")
lang = get_lang()
text = listen()
if text:
     Translated = translator.translate(text, dest=lang).text
     print("Translated:", Translated)
     speak(Translated)

               
    
