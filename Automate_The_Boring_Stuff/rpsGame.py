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
gamelabels = ["Rock","Paper","Scissor"]

optioncontinue = True
while(optioncontinue):
    #clear()
    print(nameof(wins),":\t",wins," ",nameof(ties),":\t",ties," ",nameof(losses),":\t",losses)
    CPUchoice = random.randint(0,2)
    print(nameof(CPUchoice),":\t",CPUchoice)
    print("Enter your choice (0: Rock, 1: Paper, 2: Scissor):")
    USERchoice = int(input())
    print(nameof(USERchoice),":\t",USERchoice)
    if CPUchoice == USERchoice:
        wins = wins + 1
    else:
        losses = losses + 1

    print("Would you like to continue (Type yes), press enter if not : ")
    optioncontinue = bool(input())
sys.exit(1)