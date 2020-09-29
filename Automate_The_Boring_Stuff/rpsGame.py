#Rock, Paper, Scissors Game

import os, sys, random, platform
from varname import nameof

def clear():
    if platform.system() == "Windows":
        if "Active" in debugmode.values():
            print("System:",platform.system(), sep="\t")
        os.system("cls")
    if platform.system() == "Linux":
        if "Active" in debugmode.values():
            print("System:", platform.system(), sep="\t")
        os.system("clear")
#clear()

USERwins = 0
USERties = 0
USERlosses = 0
gamelabels = ["Rock","Paper","Scissor"]

debugmode = {
    "Status":"Active"
}

def debug():
    print("Enter Y for DEBUG Mode N for Normal (Default: Active):",end=" ")
    try:
        inputvar1 = input()
    except KeyboardInterrupt:
        print("Ending due to Interrupt!")
        sys.exit(2)

    if inputvar1 == "Y" or inputvar1 == "y":
        debugmode["Status"] = "Active"
    elif inputvar1 == "N" or inputvar1 == "n":
        debugmode["Status"] = "Off"
    else:
        print("BAD Choice.... Ending")
        sys.exit(2)

optioncontinue = True
while(optioncontinue):
    debug()
    clear()

    if "Active" in debugmode.values():
        print(nameof(optioncontinue),":",optioncontinue,sep="\t")
        print("System:\t",platform.system())

    print(nameof(USERwins),":\t",USERwins," ",nameof(USERties),":\t",USERties," ",nameof(USERlosses),":\t",USERlosses)
    CPUchoice = random.randint(0,2)
    if "Active" in debugmode.values():
        print(nameof(CPUchoice),":\t",CPUchoice)
        print(nameof(CPUchoice),":\t",gamelabels[CPUchoice])
    print("Enter your choice (0: Rock, 1: Paper, 2: Scissor):")
    USERchoice = int(input())
    #print(nameof(USERchoice),":\t",gamelabels[USERchoice])

    if "Active" in debugmode.values():
        print(nameof(USERchoice),":\t",USERchoice)

    print(nameof(USERchoice),":\t",gamelabels[USERchoice])

    if CPUchoice == USERchoice:
        USERties = USERties + 1

    if CPUchoice == 0 and USERchoice == 1:
        USERlosses = USERlosses + 1

    if CPUchoice == 0 and USERchoice == 2:
        USERlosses = USERlosses + 1

    if CPUchoice == 1 and USERchoice == 0:
        USERwins = USERwins + 1

    if CPUchoice == 1 and USERchoice == 2:
        USERwins = USERwins + 1

    if CPUchoice == 2 and USERchoice == 0:
        USERwins = USERwins + 1

    if CPUchoice == 2 and USERchoice == 1:
        USERlosses = USERlosses + 1
    print(nameof(USERwins), ":\t", USERwins, " ", nameof(USERties), ":\t", USERties, " ", nameof(USERlosses), ":\t",
          USERlosses)
    print("Would you like to continue (Type yes), press enter if not : ")
    optioncontinue = bool(input())
    if "Active" in debugmode.values():
        print(nameof(optioncontinue),":",optioncontinue,sep="\t")
#print(nameof(USERwins),":\t",USERwins," ",nameof(USERties),":\t",USERties," ",nameof(USERlosses),":\t",USERlosses)
sys.exit(1)