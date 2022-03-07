# -*- coding: utf-8 -*-

import speech_recognition as sr
from request_router import router

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


continue_ = True

while continue_:
    try:
        request = hear_mic()
        print(request)
        continue_ = router(request)
    except:
        print ("I didn't understand... Repeat, please!")
