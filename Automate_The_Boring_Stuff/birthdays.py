from varname import nameof
import random,sys

birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}

choice = True

while choice:
    try:
        print("Enter Name (Enter quit to Quit):",end="\t")
        inputvar = input()

        print(nameof(inputvar),":",inputvar,sep="\t")
    except KeyboardInterrupt:
        print("Ending!!!")

    if inputvar == "quit" or inputvar == "Quit" or inputvar == "QUIT":
        choice = False
        break
    else:
        choice = True
    try:
        print(nameof(birthdays),"[",inputvar,"]",":",birthdays[inputvar],sep="\t")
    except KeyError:
        print("I donot have that value! \n Enter Now (y or n):")
        inputvar2 = input()
        print(nameof(inputvar2), ":", inputvar2, sep="\t")

        if inputvar2 == "y" or inputvar2 == "Y":
            try:
                print("Enter the name:")
                ipname = input()
                print("Enter the Birthday MMM DD:")
                ipdate = input()
                birthdays[ipname] = ipdate
                print("Birthdays Updated!!")
            except KeyboardInterrupt:
                print("Exiting!...")
        else:
            print("Exiting!!")
sys.exit(1)