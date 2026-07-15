import speech_recognition as sr

class Listener:

    def __init__(self):
        self.recognizer=sr.Recognizer()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""
        