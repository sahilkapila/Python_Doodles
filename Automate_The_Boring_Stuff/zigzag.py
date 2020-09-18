#My rendition of the zig zag game
import sys,random,os,platform,time
from varname import nameof

def zigzag():
    global indent
    indentincreasing = True

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
    except KeyboardInterrupt:
        print("END!!")
        sys.exit(1)

indent = 0
print("System",platform.system(),sep=" : ",end="\n")
zigzag()
