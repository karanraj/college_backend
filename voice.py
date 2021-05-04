#!/usr/bin/python3
import cgi
import subprocess as sb
import speech_recognition as sr

print("content-type: text/html\n")
print("Hello")
r=sr.Recognizer()
with sr.Microphone() as source:
 print('start saying....')
 audio=r.listen(source)
 print('got it..')
 data=r.recognize_google(audio)
 print('did you just sayid {0}'.format(data))

