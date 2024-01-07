# personal voice assistent

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishing function
def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning mam!!")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon mam!!")
        
    elif hour >= 18 and hour < 24:
        speak("Good Evening mam!!")

    speak("siri at your service mam, please tell me how may I help you.")


#take microphone input from user and return string output
def takeommand():    
#taking input
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
#printing string   
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except Exception:
        text = ""
        print("Sorry, I didn't understand that.")
    
    return text
   


if __name__ == "__main__":
    speak("Welcome you all! ")
    wishme()
    i=1
    while i<8:

        query=takeommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        
        elif 'play music' in query:
            mus_dir="D:\\music"
            songs=os.listdir(mus_dir)
            print(songs)
            os.startfile(os.path.join(mus_dir,songs[0]))

        elif 'what is the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:&S")
            speak(f"the time is {strtime}")
        
        elif 'open code' in query:
            codepath="C:\\Users\\kajal\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codepath)

    i+=1




    
