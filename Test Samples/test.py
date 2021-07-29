import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests, json


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening.....")
        audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understand your audio")
        except sr.RequestError as e:
            print("Request Failed: {0}".format(e))
        return data


def respond(audiostring):
    print(audiostring)
    tts = gTTS(text=audiostring, lang="ta")

