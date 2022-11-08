import speech_recognition as sr
import pyttsx3

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.getProperty('voices', voices[1])

def talk (text):
    engine.say('text')
    engine.runAndWait()

def take_command:
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                talk(command)
    except:
        pass
    return command