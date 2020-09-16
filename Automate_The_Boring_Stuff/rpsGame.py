#Rock, Paper, Scissors Game

import os, sys, random, platform
from varname import nameof

def clear():
    if platform.system() == "Windows":
        #print("System:","\t",platform.system())
        os.system("cls")
    if platform.system() == "Linux":
        #print("System:", "\t", platform.system())
        os.system("clear")
#clear()

wins = 0
ties = 0
losses = 0
ties = 0
