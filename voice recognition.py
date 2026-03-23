import speech_recognition as sr
import pyttsx3
from  datetime import datetime
engine = pyttsx3.init()
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("you said:", command)
            return command.lower()
        except:
            print("sorry, didn't catch that.")
            return ""
def respond(cmd):
        if "hello" in cmd:
            speak("Hi!")
        elif "name" in cmd:
            speak("I am your assistant.")
def respond(cmd):
    if  "hello" in cmd: 
          speak("Hi")
    elif  "name" in cmd:
          speak("I am your assistant.")
    elif  "time" in cmd:
          speak("Time is " + datetime.now().strftime("%H:%M"))
    elif  "exit" in cmd:
         speak("Goodbye!")
         return False
    else:
         speak("Try again.")
    return True
def main():
     speak("Assistant started")
     while True:
          cmd = get_audio()
          if cmd and not respond(cmd):
               break
if __name__== "__main__":
    main()


