# -*- coding: utf-8 -*-
from os import listdir
from jproperties import Properties
import speech_recognition as sr
from pygame import mixer
from threading import Thread

configs = Properties()
with open('./app.properties', 'rb') as config_file:
    configs.load(config_file)

musics_path = configs.get("musics_path").data
musics = [f for f in listdir(musics_path)]

def play_music(music):
    song = music_max_correlation(music)
    if (song != ''):
        print(song)
        song = "{}{}".format(musics_path, song)
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
        print("Say 'STOP' to stop the the music")
        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            while self.music.get_busy():
                try:
                    audio = mic.listen(source)
                    command = mic.recognize_google(audio)
                    command = command.split(' ')[1]
                    if command.lower() == 'stop music':
                        self.music.stop()
                        break
                    else:
                        print("You must stop the music to make another request!")
                        continue
                except:
                    continue