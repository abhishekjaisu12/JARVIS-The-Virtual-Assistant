import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit as kit#This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"
import time
import wikipedia
from googletrans import Translator
import os
import pyautogui
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import random
import pyperclip
from urllib.request import urlopen
import cv2
import numpy as np
from PIL import Image #pillow package






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        Speak(f"Good morning,and welcome back..  Time is {tt}")
    elif hour >= 12 and hour <= 18:
        Speak(f"Good afternoon,and welcome back..  Time is {tt}")
    else:
        Speak(f"Good evening, and welcome back..  Time is {tt}")

    assname = ("Jarvis here")
    Speak("I am your Assistant")
    Speak(assname)

    Speak("How can i Help you, Sir")

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()



def OpenApps():
      
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'command prompt' in query:
            os.system('start cmd')  

        Speak("Your Command Has Been Completed Sir!")



def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")
        
def DownloadYouTube():
        from pytube import YouTube
        from pyautogui import click
        from pyautogui import hotkey
        import pyperclip
        from time import sleep
        

        sleep(2)
        click(x=1087, y=66)
        hotkey('ctrl', 'c')
        value = pyperclip.paste()
        Link = str(value)  # Important

        def Download(link):

            url = YouTube(link)

            video = url.streams.first()

            video.download(
                'E:\\Jarvis final project\\DataBase-20210621T173720Z-001\\DataBase\\youtube\\')

        Download(Link)

        Speak("Done Sir , I Have Downloaded The Video .")

        Speak("You Can Go And Check It Out.")

        os.startfile(
            'E:\\Jarvis final project\\DataBase-20210621T173720Z-001\DataBase\youtube\\')




def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")

        
def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "E:\\Jarvis final project\screenshots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile(f"E:\\Jarvis final project\screenshots\\")
        Speak("Here Is Your ScreenShot") 

def TaskExe():
    def clear(): return os.system('cls')
    clear()
    pyautogui.press('esc')
    Speak('Face Verification succesfull')
    wishMe()

    

  

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Jarvis .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")
            
        elif "also good" in query or "fine" in query:
            Speak("That's great sir")
            
        elif 'not good' in query or 'not fine' in query:
            Speak("sorry to hear that sir")
            Speak("WhaAT I CAN DO FOR YOU")
            
            
        
        elif "don't listen" in query or "stop listening" in query  or "you can sleep" in query or "sleep now" in query or "sleep" in query:
                Speak("ok sir,  I am going to sleep , you can call me anytime ")
                Speak("Just Say Wake Up Jarvis!")
                break
                



        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis!")
            break




        
        elif 'corona ' in query:
            Speak("Which Country's Information ?")
            cccc = TakeCommand()
            CoronaVirus(cccc)
            
        elif 'open youtube' in query:
               Speak("Ok Sir , Wait A second!")
               Speak("about what you want to search on youtube")
               s = takecommand()
            # play on yt if it is kit.search then i will search on google
               kit.playonyt(s)

    

        elif 'open website' in query or 'open a website' in query or 'open the website' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()
        elif 'command prompt' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
    
        elif 'download' in query:
            DownloadYouTube()
        elif 'open chrome' in query:
            OpenApps()

        elif 'play music' in query or "play song" in query:
                music_dir ="C:\\musics"
                files = os.listdir(music_dir)
                music = random.choice(files)
                os.startfile(os.path.join(music_dir, music))

        elif "song on youtube" in query:
            kit.playonyt("faded")
        
        elif ' time' in query:
                strTime = datetime.datetime.now().strftime("%I:""%M:""%S") 
                Speak(f"Sir, the time is {strTime}")
                print(strTime)
        elif 'close chrome' in query:
            CloseAPPS()
            
        elif 'close youtube' in query:
            CloseAPPS()



        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()
       


       
       

#if __name__ == '__main__':
     #while True:
         #permission=takecommand()
         #if"wake up" in permission or "makeup":
             #TaskExe()
         #elif"Goodbye " in permission:
            #Speak("Thanks for using me sir,")
           #sys.exit()



TaskExe()
