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