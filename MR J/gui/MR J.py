

from JarvisUI import Ui_Dialog
from PyQt5 import QtCore,QtWidgets,QtGui,uic
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from cgitb import text
import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import wikipedia
import webbrowser
import datetime
from playsound import playsound
import pyjokes
import pyautogui
import keyword
import smtplib
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import sys
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 150)
def Speak(audio):
        print('  ')
        Assistant.say(audio)
        print(f":{audio}")
        Assistant.runAndWait()


Speak('hello kanika....I am Mr j... your Personal assistant')
Speak('how may i help you')
Speak('lets start')
def takecommand():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening................")
        
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
            print("Recognizing")
            query = command.recognize_google(audio, language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "None"
        return query.lower()
query = takecommand()
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self
       





   


    


    
    def closeapps():
        Speak("ok....wait for a second")
        if "code" in query:
            os.system("TASKKILL / F / im code.exe")
        elif "maps" in query:
            os.startfile("TASKKILL/F/im maps.exe ")    
        elif "word" in query:
            os.system( "TASKKILL/F/im word.exe ") 
    Speak("done sir")
    def openapps():
        Speak("ok.. wait for a second")

        if "code" in query:
            os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "word" in query:
            os.startfile( "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE") 
        
        elif "maps" in query:
            webbrowser.open("https://www.google.com//maps//@30.9618341,74.6283312,15z")
    Speak("your command has been executed")




    if __name__=="__main__" :
    
        while True:
            query = takecommand().lower()
       
           
            if 'wikipedia' in query:
                Speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                Speak("According to Wikipedia")
                print(results)
                Speak(results)

            elif 'youtube' in query:
                Speak("ok... this is what i found on youtube")
                query = query.replace("jarvis", "")
                query = query.replace("youtube", "")
                web = "https://www.youtube.com/results?search_query="+query
                webbrowser.open(web)
                Speak("done sir")

            elif ' google' in query:
                Speak("ok... this is what i found on google")
                query = query.replace("jarvis", "")
                query = query.replace("google", "")
                pywhatkit.search(query)

                Speak("done sir")
                webbrowser.open("google.com")

            elif ' website' in query:
                Speak("ok... found your searched website")
                query = query.replace("jarvis", "")
                query = query.replace("website", "")
                web1 = query.replace("open", "")
                web2 = "https://www"+web1+".com"
                webbrowser.open(web2)
                Speak("launched....")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(f"Sir, the time is {strTime}")
        
            elif 'open instagram' in query:
                Speak("Done sir")
                webbrowser.open("https://www.instagram.com/")
            elif 'open snapchat' in query:
                Speak("Done sir")
                webbrowser.open("https://www.snapchat.com/")
       

            elif 'alarm' in query:
                Speak("tell me the time")
                Time = eval(input("enter the time"))
                while True:
                    Time_a = datetime.datetime.now()
                    now = Time_a.strftime("%H:%M:%S")
                    if now == Time:
                        Speak("wake up sir.. do your work")
                        playsound(
                            "C:\\Users\\hp\\jarvis\\jarvis\\Alarm-Fast-A1-www.fesliyanstudios.com.mp3")
                        Speak("alarm ended..hope you have a good sleep")
                    elif now > Time:
                        break
            elif "screenshot" in query :
                k= pyautogui.screenshot()
                k.save("F:\\eng books\\BEEE")
            elif " openword" in query :
                openapps()
            elif " open maps" in query :
                openapps()
            elif "code" in query :
                openapps()
            elif "closemaps" in query:
                closeapps()
            elif "closecode" in query:
                closeapps()    
            elif "closeword" in query:
                closeapps()  
            elif "joke" in query:
                get= pyjokes.get_joke()
                Speak(get)
            elif " repeat my words" in query:
                Speak("tell me what you want to repeat")
                ll=takecommand()
                Speak(f"you said:{ll}")
            """else:
                reply=chatbot.chatterbot(query)
                Speak(reply)"""

startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):  
        super().__init__()
        self.jarvis_ui = Ui_Dialog
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.jarvis_ui.movies_label_2= QtGui.QMovie("base.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_label_2)
        self.jarvis_ui.movies_label_2.start()

        startFunctions.start()   

    def Task_gui(self):
        os.startfile("project(1).py")  

    gui_app =QApplication(sys.argv)
    gui_jarvis= Gui_Start( )
    gui_jarvis.show()
    exit(gui_app.exec_())


