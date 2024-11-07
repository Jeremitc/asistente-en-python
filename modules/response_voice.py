import pyttsx3

engine = pyttsx3.init()

def responder(texto):
    engine.say(texto)
    engine.runAndWait()
