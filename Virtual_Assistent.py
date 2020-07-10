# -*- coding: utf-8 -*-

#Imports

import speech_recognition as sr
from Music_Player.getMusic_2 import playMusic

def hear_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Say something...")
        audio = mic.listen(source)
    try:
        request = mic.recognize_google(audio)
        print("You said: " + request)
        return request
    except:
        return "I didn't understand..."

while True:
    phrase = hear_mic()
    if ('music' in phrase.lower()):
        music = phrase.split(" ", 1)[1]
        playMusic(music)