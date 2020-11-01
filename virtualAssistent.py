# -*- coding: utf-8 -*-

import speech_recognition as sr
from music_player.getMusic import playMusic

def hear_mic():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("What do you want?")
        audio = mic.listen(source)
        try:
            request = mic.recognize_google(audio)
            print("You said: " + request)
            return request
        except:
            return "I didn't understand... Repeat, please!"

while True:
    try:
        phrase = hear_mic()
        if ('music' in phrase.lower()):
            music = phrase.split(" ", 1)[1]
            playMusic(music)
        elif phrase.lower() == 'exit':
            break
    except:
        print ("I didn't understand... Repeat, please!")
