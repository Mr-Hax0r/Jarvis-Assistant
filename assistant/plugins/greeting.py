import re

def greeting(cmd):
    if re.search(r'hello',cmd):
        if re.search(r'jarvis',cmd):
            return 'Hello Im Jarvis !'

        elif cmd == 'hello':
            return 'Hello Im Jarvis !'

        else:
            return 'Hello , How are you?'

    
    elif re.search(r'hi ',cmd):
        if re.search(r'jarvis',cmd):
            return 'hi Im Jarvis !'

        elif cmd == 'hi':
            return 'hi Im Jarvis !'
            
        else:
            return 'Hello , How are you?'

    elif re.search(r'how are you',cmd):

        if re.search(r'jarvis',cmd):
            return 'I,m Fine Tanks , And you ?'

        else:
            return 'I,m Fine'

    elif re.search(r'fine',cmd):

        if re.search(r"i'm",cmd):
            return "Ok i'm happy for you"

        else:
            return "ok"

    elif re.search(r'bad',cmd):
        if re.search(r"i'm",cmd):
            return 'Why? You are the best admin in the world !'  
        else:
            return "I don't give a fuck."            

    else:
        pass          


