#Functions

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

# Testing the optional parameters with print() .... end and sep

print("this","is","a","test",sep="\t|")
print("this")
print("is", end="\t")
print("a", end="\t")
print("test")

# Testing the global statement

import random
def coinTOSS():
    global side
    side = random.randint(0,1)
    return side

side = random.randint(0,1)
print(side)
print(coinTOSS())
print(coinTOSS())

#Try except test

def func1():
    global num
    try:
        print(num,(1/num),sep="\t")
        num = random.randint(0, 1)
    except ZeroDivisionError:
        print("Divide by zero!")
        num = random.randint(0, 1)

num = random.randint(0,1) #Initiated the global variable
func1()
func1()
func1()
func1()
func1()
func1()
func1()
func1()
func1()
