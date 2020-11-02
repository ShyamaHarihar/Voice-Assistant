import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(len(voices))
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Goodevening")
    speak("I am your personal voice assistant Please tell me how may I help You ?") 

def takeUserAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising..")
        query=r.recognize_google(audio,language='en-in')
        print("User said"+ query)
    except Exception as e:
        #print(e)
        print("Please repeat....Say that again")
        return "None"
    return query

if __name__=="__main__":
    speak("Welcome")
    greet()
    while True:
        query=takeUserAudio().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\harik\\OneDrive\\Desktop\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is"+strTime) 
        elif 'open code' in query:
            codePath="C:\\Users\\harik\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'who are you' in query:
            speak("I am your personal Voice Assistant I can do simple things like opening youtube,google,stackoverflow,visual studio code,tell you the time,play music etc")            
        elif 'quit' in query:
            speak("Thankyou")
            exit() 
        
       


