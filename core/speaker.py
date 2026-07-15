import pyttsx3

class Speaker:

    def __init__(self):
        self.engine=pyttsx3.init()
        self.engine.setProperty('rate',170)
        self.engine.setProperty('volume',1.0)
    
    def say(self,text):
        print(f"Gappi: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

import speech_recognition as sr

class Listener:

    def __init__(self):
        self.listen = sr.init()
        self.listen.Recognizer()
        
