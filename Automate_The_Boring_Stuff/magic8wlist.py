from varname import nameof
import random, sys

eightball =[
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is No",
    "Outlook not so good",
    "Very doubtful"
]

debugmode = {
    "Status":"Active"
}
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

choice = True
try:
    while(choice):
        print(nameof(eightball),":",random.choice(eightball),sep="\t")
        print("Roll again (yes or no):")
        input1 = input()
        if input1 == "yes":
            choice = True
        elif input1 == "no":
            choice = False
    sys.exit(1)
except KeyboardInterrupt:
    print("END!!")
    sys.exit(1)