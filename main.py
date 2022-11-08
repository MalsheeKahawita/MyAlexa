import speech_recognition as sr
import pyttsx3

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.getProperty('voices', voices[1])
engine.say('I am your alexa')
engine.say('What can I do for you')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening....')
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass