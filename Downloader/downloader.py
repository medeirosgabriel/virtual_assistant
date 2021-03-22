import youtube_dl
import os

link = input("Insert URL: ")
name = input("Name URL: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': name,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    if __name__ == "__main__":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filenames = [link]
            ydl.download(filenames)
except:
    os.system("clear")