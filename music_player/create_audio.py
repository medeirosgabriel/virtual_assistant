# -*- coding: utf-8 -*-

#Imports

from gtts import gTTS
from playsound import playsound
import os

def createAudio(audio):
    tts = gTTS(audio)
    tts.save('data/audio.mp3')
    filename = 'data/audio.mp3'
    playsound(filename)
    os.remove("data/audio.mp3")