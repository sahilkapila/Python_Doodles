print("Hello World")
age = 20
sentence = "this is a test"

print("Hello, "+sentence)

print("Just so you know Age: "+str(age))

print("Hello World..\nHello, "+sentence+"\nJust so you know Age: "+str(age))

passwordfile = open('Testfile.txt')

secretPassword = passwordfile.read()

print("Enter Password: ")
typedPassword = input()

if typedPassword == secretPassword:
    print("Success!!!")
else:
    print("Failed")

sam, john, martin = 17,12,"Test"

print(str(sam)+"\n"+str(john)+"\n"+martin)

