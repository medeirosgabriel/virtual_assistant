# -*- coding: utf-8 -*-
from os import listdir
import speech_recognition as sr
from pygame import mixer
from threading import Thread

musics = [f for f in listdir("C://Users//Alba//Music//Músicas")]

def playMusic(music):
    song = music_max_correlation(music)
    print(song)
    song = "C://Users//Alba//Music//Músicas//{}".format(song)
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    tr = StopThread(mixer.music)
    tr.start()
    tr.join()
    
def music_max_correlation(music):
    max_correlation = 0
    song = ''
    for m in musics:
        corr = correlation(music, m)
        if (corr > max_correlation):
            song = m
            max_correlation = corr
    return song
            
def correlation(music1, music2):
    m1 = music1
    m2 = music2.lower().split(".")[0]
    corr = 0
    i = 0
    while i < len(m1) and i < len(m2):
        if (m1[i] == m2[i]):
            corr += 1
        i += 1
    return corr
        
class StopThread(Thread):
    
    def __init__(self, music):
        Thread.__init__(self)
        self.music = music
        
    def run(self):
        mic = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            mic.adjust_for_ambient_noise(source)
            print("...")
            audio = mic.listen(source)
        try:
            command = mic.recognize_google(audio,language='pt-br')
            if command.lower() == 'stop':
                self.music.stop()
            else:
                print("Repeat, please")
        except:
            print("StopThreadError...")
