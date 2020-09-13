# Flow Control

a = True
b = False

from varname import nameof

print("The value of \t",nameof(a),"\t",a)
print("The value of \t",nameof(b),"\t",b)

print("Now we will evaluate conditions....")

operations = ["Equal to","Not Equal to","Less than","Greater than","Less than or equal to","Greater than or equal to"]

print(operations[0],"\t",a==b)
print(operations[1],"\t",a!=b)
print(operations[2],"\t",a<b)
print(operations[3],"\t",a>b)
print(operations[4],"\t",a<=b)
print(operations[5],"\t",a>=b)

booleanoperations = ["and","or","not"]

print(booleanoperations)
#ERROR: Does not evaluate the or and not conditions
for x in booleanoperations:
#    print(x)
    if (x == "and"):
        print(x,"\t",a and b)
    if (x == "or"):
        (x,"\t",a or b)
    if (x == "not"):
        (x,"\t",not a," ",not b)
else:
    print("Finally finished....")

x = 0
repeat = 5
print("In a while loop: ",nameof(repeat)," = ",repeat)
while x < repeat:
    print("In a while")
    x = x +1


