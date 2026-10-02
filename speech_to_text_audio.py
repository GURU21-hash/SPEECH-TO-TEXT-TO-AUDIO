import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)

    print("You said:", text)

    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Could not understand your speech.")

except sr.RequestError:
    print("Speech recognition service is unavailable.")
