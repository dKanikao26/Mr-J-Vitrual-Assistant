
import speech_recognition as sr
import pyttsx3
import datetime


Assistant= pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print('    ')
    Assistant.say(audio)
    print('    ')
    Assistant.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("good morning!")
    elif hour>=12 and hour<18:
         Speak("good morning!") 
    else:
        Speak("good evening")
    Speak("i am alexa sir,please tell me how may i help you")


def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening................")
        command.pause_threshold=1
        audio = command.listen(source)

        try:
            print("Recognizing")
            query = command.recognise_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            print("say that again please")
            return "None"
            return query
          `
          
query= takecommand()





if __name__ == "__main__":
   Speak("HELLO")
   wishMe()
   takeCommand()







