from __future__ import unicode_literals
import os, shutil, subprocess
from turtle import color
from termcolor import colored
import colorama
from colorama import Fore
from pathlib import Path

path = str(Path(__file__).parent.absolute())


print("| -------------------------------------------- CONVERT TO MP3 -------------------------------------------- ")
print("|   Insert the URLs :                  ")
print("|                                      ")


# GETTING THE SONGS LINKS 

links = []
link = input ("| >> ")
while(link!=""):
    if("&" in link):
        id = link.index("&")
        link = link[:id]  # removing the wrong parts of the link ("&index=..." and "&list=...")
    links.append(link)
    link = input ("| >> ")
   


# DOWNLOADING THE SONGS 

for l in links: 
    print("| --------------------------------------------------------------------------------------------------------")
    title = (subprocess.check_output("youtube-dl --get-title "+str(l)).decode("latin-1")[:-1])
    colorama.init()
    print(Fore.BLUE + "| Downloading " + title + " ... ")
    os.system('youtube-dl -q --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + str(l))   # -o to get a proper name of file
    print(Fore.GREEN + "| " + title + " downloaded !")


# MOVING THE MUSICS IN THE DOWNLOAD FOLDER

musics = [f for f in os.listdir(path) if f.endswith('.mp3')]
for m in musics:
    shutil.move( path + "/" + str(m), path + "/downloads/" + str(m) )

