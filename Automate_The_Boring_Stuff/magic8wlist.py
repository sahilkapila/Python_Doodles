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