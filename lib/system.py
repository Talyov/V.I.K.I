"""
toute les opérations système (tri fichier, backup, enregistrer fichier ...)
"""
import random
import os
import subprocess
import webbrowser
import lib.viki_voice as viki

def salut():
    hello = ["salut", "bonjour", "yo"]
    viki.talk(random.choice(hello))

def launch_webbrower():
    webbrowser.open("http://www.google.fr")


if __name__ == "__main__":
    print("test classe system...")
