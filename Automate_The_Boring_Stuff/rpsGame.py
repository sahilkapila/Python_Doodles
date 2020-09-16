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

USERwins = 0
USERties = 0
USERlosses = 0
gamelabels = ["Rock","Paper","Scissor"]

optioncontinue = True
while(optioncontinue):
    clear()
    print("System:\t",platform.system())
    print(nameof(USERwins),":\t",USERwins," ",nameof(USERties),":\t",USERties," ",nameof(USERlosses),":\t",USERlosses)
    CPUchoice = random.randint(0,2)
    #print(nameof(CPUchoice),":\t",CPUchoice)
    print(nameof(CPUchoice),":\t",gamelabels[CPUchoice])
    print("Enter your choice (0: Rock, 1: Paper, 2: Scissor):")
    USERchoice = int(input())
    #print(nameof(USERchoice),":\t",USERchoice)
    print(nameof(USERchoice),":\t",gamelabels[USERchoice])
    if CPUchoice == USERchoice:
        USERties = USERties + 1

    if CPUchoice == 0 and USERchoice == 1:
        USERwins = USERwins + 1

    if CPUchoice == 0 and USERchoice == 2:
        USERlosses = USERlosses + 1

    if CPUchoice == 1 and USERchoice == 0:
        USERwins = USERwins + 1

    if CPUchoice == 1 and USERchoice == 2:
        USERlosses = USERlosses + 1

    if CPUchoice == 2 and USERchoice == 0:
        USERwins = USERwins + 1

    if CPUchoice == 2 and USERchoice == 1:
        USERlosses = USERlosses + 1

    print("Would you like to continue (Type yes), press enter if not : ")
    optioncontinue = bool(input())

print(nameof(USERwins),":\t",USERwins," ",nameof(USERties),":\t",USERties," ",nameof(USERlosses),":\t",USERlosses)
sys.exit(1)