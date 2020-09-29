#My rendition of the zig zag game
import sys,random,os,platform,time
from varname import nameof

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


def zigzag():
    global indent
    indentincreasing = True
    if "Active" in debugmode.values():
        print(nameof(indent),":",indent,sep="\t")
        print(nameof(indentincreasing),":",sep="\t")

    try:
        while True:
            print((" "*indent),end="")
            print("*********")
            time.sleep(0.1)
            if indentincreasing:
                indent = indent + 1
                if indent == 20:
                    indentincreasing = False
            else:
                indent = indent - 1
                if  indent == 0:
                    indentincreasing = True
            if "Active" in debugmode.values():
                print(nameof(indent),":",indent,sep="\t")
                print(nameof(indentincreasing),":",indentincreasing, sep="\t")
    except KeyboardInterrupt:
        print("END!!")
        sys.exit(1)

indent = 0
debug()
if "Active" in debugmode.values():
    print("System",platform.system(),sep=" : ",end="\n")
zigzag()
