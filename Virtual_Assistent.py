# -*- coding: utf-8 -*-

#Imports

import speech_recognition as sr
from Music_Player.GetMusic_2 import playMusic

def hear_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Say something...")
        audio = mic.listen(source)
    try:
        phrase = mic.recognize_google(audio,language='pt-br')
        print("You said: " + phrase)
        return phrase
    except:
        return "I didn't understand..."

while True:
    phrase = hear_mic()
    print(phrase)
    if ('música' in phrase.lower()):
        music = phrase.split(" ")[1:]
        music = " ".join(music)
        playMusic(music)