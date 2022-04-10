import random


c1=["hello","wake up jarvis","hi","utho jarvis","hey","jarvis","namaste","helpme",""
]
reply=["always for you sir","hi sir!any work for me","hello!how are you sir","how can i help you","hope you mess me sir!how can i help you","nice metting you sir again","hello sir! how are you"
"batao kasa ana hua","i love you sir.. how can i entertain you"]

c2=["go and sleep","byee","so jao","sleep"]
reply_2=["ok sir ","bye sir","good day sir","have a nice sleep  sir","have a nice day sir"]
def chatterbot(text):
    for word in text.split():
        if word in c1:
            return random.choice(reply)+"."



hk=chatterbot("wake up jarvis")
print(hk)