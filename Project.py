# This Program based on Mac-OS-X operating 

import os
import pyttsx3

pyttsx3.speak('How May I help you sir?')
flag=True
while flag:
    print('----------------------------------------------------------------')
    pyttsx3.speak('Enter your requirement:')
    print("\n\nHow May I help you Sir: ",end="")
    uin=input()
    if 'dont' in uin or 'do not' in uin:
        pyttsx3.speak('What else you want to do:')
        continue
    elif 'run' in uin or 'execute' in uin or 'open' in uin or 'start' in uin or 'launch' in uin:
        if 'editor' in uin or 'textedit' in uin: 
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a textedit')
                pyttsx3.speak('Program Launched in background sir')
            else:
                os.system('open -a textedit')
                pyttsx3.speak('Here is what I found:')
        elif 'safari' in uin or 'browser' in uin:
            if 'background' in uin or 'bg' in uin:
                pyttsx3.speak("What do you want to search:")
                print("What do you want to search:",end="")
                search=input()
                os.system('open -g -a safari https://{}.com'.format(search))
                pyttsx3.speak('Your result launched in Background sir')
            else:
                pyttsx3.speak("What do you want to search:")
                print("What do you want to search:",end="")
                search=input()
                os.system('open -a safari https://{}.com'.format(search))
                pyttsx3.speak('Here is the result')
        elif 'notes' in uin or 'note' in uin:
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a notes')
                pyttsx3.speak('Notes Launched in background sir')
            else:
                os.system('open -a notes')
                pyttsx3.speak('Here is the result')
        elif 'vlc' in uin or 'video player' in uin:
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a vlc')
                pyttsx3.speak('VLC launched in background')
            else:
                os.system('open -a vlc')
                pyttsx3.speak('Here is the result')
        elif 'terminal' in uin or 'cli' in uin:
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a terminal')
                pyttsx3.speak('Terminal launched in background')
            else:
                os.system('open -a terminal')
                pyttsx3.speak('Here is what I found:')
        elif 'whatsapp' in uin:
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a whatsapp')
                pyttsx3.speak('Whatsapp launched in background')
            else:
                os.system('open -a whatsapp')
                pyttsx3.speak('here is the result')
        elif 'music player' in uin or 'iTunes' in uin:
            if 'background' in uin or 'bg' in uin:
                os.system('open -g -a music')
                pyttsx3.speak('iTunes launched in background')
            else:
                os.system('open -a music')
                pyttsx3.speak('here is the result')

        else:
            pyttsx3.speak('Software not installed ')

    elif 'close' in uin or 'quit' in uin:
        if 'editor' in uin or 'textedit' in uin: 
            os.system('sudo killall TextEdit')
            pyttsx3.speak('Program closed')
        elif 'safari' in uin or 'browser' in uin:
            os.system('sudo killall Safari')
            pyttsx3.speak('Program closed')
        elif 'notes' in uin or 'note' in uin:
            os.system('sudo killall Notes')
            pyttsx3.speak('Program closed')
        elif 'vlc' in uin or 'video player' in uin:
            os.system('sudo killall vlc')
            pyttsx3.speak('Program closed')
        elif 'terminal' in uin or 'cli' in uin:
            os.system('sudo killall Terminal')
            pyttsx3.speak('Program closed')
        else:
            pyttsx3.speak('No running program found:')

    elif 'exit' in uin or 'offline'in uin:
        flag=False
else:
    pyttsx3.speak('Have a good day sir,See you soon')


