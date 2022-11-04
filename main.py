import speech_recognition as sr

listner = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening....')
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        print(command)
except:
    pass