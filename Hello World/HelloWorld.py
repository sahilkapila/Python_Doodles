print("Hello World")
age = 20
sentence = "this is a test"

print("Hello, "+sentence)

print("Just so you know Age: "+str(age))

print("Hello World..\nHello, "+sentence+"\nJust so you know Age: "+str(age))

import os

script_dir = os.path.dirname("Hello World")
rel_path = "Testfile.txt"
abs_file_path = os.path.join(script_dir, rel_path)

passwordfile = open(abs_file_path,"r+")
# passwordfile = open("Testfile.txt")

secretPassword = passwordfile.read()

if secretPassword == "":
    print("Password not set please enter it :")
    newpassword = input()
    passwordfile.write(newpassword)
    passwordfile.close()
    exit(0)
else:
    print("fetching password....")
    passwordfile.close()

print("Enter Password: ")
typedPassword = input()

if typedPassword == secretPassword:
    print("Success!!!")
else:
    print("Failed")

sam, john, martin = 17,12,"Test"

print(str(sam)+"\n"+str(john)+"\n"+martin)
print("Test splicing: \n"+secretPassword[0:2])

