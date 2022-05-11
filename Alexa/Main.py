import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner= sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listning...")
            voice= listner.listen(source)
            command = listner.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
        
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("the time is "+ time)
        print(time)
    elif 'date' in command:
        talk('nope')
    elif 'are you single' in command:
        talk('yes i am single')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('i am fine, how are you')
    elif 'i am good' in command:
        talk('good to know')
    elif 'thank you' in command:
        talk('your welcome!')
    elif 'how' in command:
        how = command
        pywhatkit.playonyt(how)
    elif 'who' or 'what' in command:
        person=command
        info = wikipedia.summary(person,3)
        print(info)
        talk(info)
    else:
        talk('please tell the command again, please')


while True:
    run_alexa()

print("this is it, this was the project!")