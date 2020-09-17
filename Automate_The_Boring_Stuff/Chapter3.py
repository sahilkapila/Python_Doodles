#Functions
from varname import nameof
import sys, random, platform

def hello():
    print("Inside:\tHello()")
    #sys.exit(1)

def hello1(name):
    print("Inside:\t",name)
    #sys.exit(2)

hello()
hello1("Test")

testvar = None

def checkvar(var):
    if var == None:
        print("None")
    else:
        print("NOT NONE")

checkvar(testvar)

testvar = "Hello"

checkvar(testvar)