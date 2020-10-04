import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import webbrowser
import time 
import random

engine = pyttsx3.init()

#speaking part of JD
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#time 
def hour():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

#greeting
def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("Good morning sir!")
    elif hour >=12 and hour <= 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <=24:
        speak("Good evening sir!")
    else:
        speak("Good nigth sir!")

#recognizes speech
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        return query
    except Exception as e:
        print(e)
        speak("Say that again please!")
        return "None"
    return query      

def respond():
    myCommand = takeCommand()
    print(myCommand)
    if ('hey' in myCommand) or ('hi' in myCommand) or ('hello' in myCommand):
        greetings = ["hey, how can I help you","hi, what's up","I'm listenning to you","hi"]
        speak(random.choice(greetings))
    if ('what is your name' in myCommand) or ('what\'s your name' in myCommand) or ('who are you' in myCommand):
        speak("My name is JD, nice to meet you sir!")
    if ('what time is it' in myCommand) or ('what\'s the time' in myCommand) or ('tell me the time' in myCommand):
        hour()
    if 'search' in myCommand:
        speak("What do you want search for?")
        search = takeCommand()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak("Here is what I found for" + search)
    if ('exit' in myCommand) or ('quit' in myCommand) or ('good bye' in myCommand) or ('bye' in myCommand): 
        speak('Going offline, bye-bye!')
        exit()

greeting()
speak("How can I help you?")
    
time.sleep(1)
while 1:
    respond()
