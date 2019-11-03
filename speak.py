import pyttsx3
import datetime
import speech_recognition as sr             # IMPORTING THE LIBRARIES
import wikipedia
import webbrowser
import os


# PHASE ONE
engine = pyttsx3.init('sapi5')                    # microsoft speech API provided by microsoft
voices = engine.getProperty('voices')             #setting the voice we want
engine.setProperty('voices', voices[0].id)

# PHASE TWO
def speak(audio):                     #defining the speak function 
    engine.say(audio)
    engine.runAndWait()

#PHASE THREE
def wishMe():                       #startup wishing function by the assistant
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak(" Good Morning Sir")
    elif hour > 12 and hour < 17:
        speak("Good afternoon Sir")
    else:
        speak("Good evening sir")
    speak("hello sir.I am zira. Please tell me how may i help you  ")


# PHASE FOUR
def takeCommands():              #function to recognize speech and take commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"you said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


# PHASE FIVE (LOGICAL BODY)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommands().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia for that")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'google' in query:
            webbrowser.open('google.com')
            
        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query:
            music = 'E:\\Music\\English'   # path of music folder
            songs = os.listdir(music)      #making list of songs in music folder
            print(songs)                   
            os.startfile(os.path.join(music, songs[0]))   #can play any song from list by passing index
            
        elif 'the time' in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(t)
            speak(f"Sir,the time is {t}")
                                               
        elif 'how are you' in query:                     #just random queries :)
            speak("I am good sir. what about you. I hope you are having a great day ?")
            print("I am good sir, what about you ?")
            
        elif 'what the hell' in query:
            speak('I am sorry sir but I do not think I deserve that. Tell me how may I help you? ')
            print('I am sorry sir but I do not think I deserve that. Tell me how may I help you?')
            
        elif 'goodbye' in query:
            speak("going offline Sir. Have a great day")
            break
            
        elif 'what is your name' in query:
            speak(" hello sir I am zira. Your personal assistant. What would you like me to for you today?")
            print(" hello sir I am zira. Your personal assistant. What would you like me to for you today?")
            
        elif 'where do you live' in query:
            speak("I believe that this computer is my home. what about you ? ")
            
        elif 'do you have a girlfriend' in query:
            speak("No sir I do not. ")
            
        elif 'you happy' in query:
            speak("your happiness is my happiness sir.")

