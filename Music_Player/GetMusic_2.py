# -*- coding: utf-8 -*-
from os import listdir
import speech_recognition as sr
from pygame import mixer
from threading import Thread

musics = [f for f in listdir("C://Users//Alba//Music//Músicas")]

def playMusic(music):
    song = music_max_correlation(music)
    if (song != ''):
        print(song)
        song = "C://Users//Alba//Music//Músicas//{}".format(song)
        mixer.init()
        mixer.music.load(song)
        mixer.music.play()
        tr = StopThread(mixer.music)
        tr.start()
        tr.join()
    else:
        print ("This music doesn't exists")
    
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
    m1 = music1.lower().split(" ")
    m2 = music2.lower().replace(".", " ").replace(",", " ").replace(" - ", " ").split(" ")
    m2 = [e for e in m2 if e]
    corr = 0
    for w in m2:
        if (w in m1):
            corr += 1
        else:
            corr -= 0.2
    return corr
        
class StopThread(Thread):
    
    def __init__(self, music):
        Thread.__init__(self)
        self.music = music
        
    def run(self):
        mic = sr.Recognizer()
        while self.music.get_busy():
            with sr.Microphone(device_index=1) as source:
                mic.adjust_for_ambient_noise(source)
                audio = mic.listen(source)
                try:
                    command = mic.recognize_google(audio)
                    if command.lower() == 'stop':
                        self.music.stop()
                        break
                    else:
                        print("You must stop the music to make another request!")
                        continue
                except:
                    continue