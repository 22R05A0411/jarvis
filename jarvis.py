import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import pywhatkit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        return query.lower()
        #speak(query)

    except Exception as e:
        speak("Sorry sir!, I didn't get that. Can you repeat?")
        return "none"
    

#to wish 
def wish():
    hour = datetime.datetime.now().hour
    if hour>0 and hour<12:
        speak("good morning!")
    elif hour>12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am jarvis, How may I assist you")

if __name__=="__main__":
    #wish()
    #takecommand()
    while True:
    #if 1:

        query = takecommand().lower()
        if "hi jarvis" in query or "hello jarvis" in query:
            speak("Hello! How can I assist you today?")
        elif "thank you jarvis" in query or "thank you" in query:
            speak("You're welcome!")
        elif "bye jarvis" in query or "bye" in query:
            speak("It was good to assist you! Thank you! Have a great day!")
    # to open and close notepad
        elif "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
    # to open cmd promt
        elif "open command prompt" in query:
            path = "C:\\windows\\system32\\cmd.exe"
            os.startfile(path)
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
    # to search in wikipedia
        elif "wikipedia" in query:
            try:
                speak("browsing")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple matching results. Can you be more specific?")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I could not find any results for your query.")
            except Exception as e:
                speak("An error occurred while fetching results. Please try again later.")
    # to open youtube
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
    #to open facebook 
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
    # to open instagram
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
    #to close chrome
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "open whatsapp" in query:
            whatsapp_path = "C:\\Users\\Sai Prasad\\AppData\\Local\\Packages"
            os.startfile(whatsapp_path)
        elif "you can sleep" in query:
            speak("thank you! sleeping.......!")
            sys.exit()

        
        


