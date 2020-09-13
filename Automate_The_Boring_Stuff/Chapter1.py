#Math operators

a = 3
b = 2

names = ["Exponent", "Modulus", "Integer Division", "Division", "Multiplication","Subtraction","Addition"]

print(a**b,"\t",names[0]," ",a," ",b)
print(a%b,"\t",names[1]," ",a," ",b)
print(a//b,"\t",names[2]," ",a," ",b)
print(a/b,"\t",names[3]," ",a," ",b)
print(a*b,"\t",names[4]," ",a," ",b)
print(a-b,"\t",names[5]," ",a," ",b)
print(a+b,"\t",names[6]," ",a," ",b)

print("The String replicator\t"*2)

print("Hello world!!!\nWhat is your name? ")
myname = input()
print("Ah ACK!! ",myname)

from varname import nameof

print("Length of variable ",nameof(myname)," : ",len(myname))