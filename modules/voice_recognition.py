import speech_recognition as sr

def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="es-ES")
            print(f"Comando recibido: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("No entendí el comando")
            return ""
