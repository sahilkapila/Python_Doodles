#These are the code snippets from chapter 4

list1 = ["hello","this","is","a","test"]

print(list1[-1],end="\t")
print(list1[2])

slice = list1[0:-2]

print(slice)
print("Length:", len(slice),sep="\t")
for i in slice:
    print(i)

slice[-2] = "another test"

print(slice)

del slice[-2]

print(slice)

slice = slice*3

print("New Length:",len(slice),sep="\t")
print(slice)

del slice[-1], slice[-2] # notice here it acts like two seperate statements first: -1 then -2 of the list post the -1 operation

print(slice)

from varname import nameof
for i in range(len(list1)):
    print("Position:",nameof(list1),"[",i,"]","Value:",list1[i],sep="\t")
    #i=i+1 Not needed the for loop increments itself

if "this" in list1:
    print("\"This\" is in ", nameof(list1),sep="\t")

if "in" not in list1:
    print("\"in\" is not in ",nameof(list1),sep="\t")

# Testing tuple unpacking
# this refers to multiple assignments

test, test1, test2 = list1[0:3] # slice not including the to ref
print(nameof(test),":",test,sep="\t")
print(nameof(test1),":",test1,sep="\t")
print(nameof(test2),":",test2,sep="\t")


#testing enumerate()
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

#testing the random choice and shuffle functions
import random

print(nameof(list1),"random choice",":",random.choice(list1),sep="\t")
print(nameof(list1),"random choice",":",random.choice(list1),sep="\t")

random.shuffle(list1)

print(list1)
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

#Testing augmented assignment operators
var = 1
print(nameof(var),":",var,sep="\t")
var += 1
print(nameof(var),":",var,sep="\t")
var -= 1
print(nameof(var),":",var,sep="\t")
var *= 2
print(nameof(var),":",var,sep="\t")
var /= 2
print(nameof(var),":",var,sep="\t")

random.shuffle(list1)
print("Index of this in ",nameof(list1),":",list1.index("this"),sep="\t")

random.shuffle(list1)
print("Index of this in ",nameof(list1),":",list1.index("this"),sep="\t")

#adding to a list using append and insert
print("Appending------")
list1.append("appended")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

print("Inserting--------")
list1.insert(0,"inserted")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

# using the remove method
list1.insert(0,"this")
print("Inserting this-----")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

list1.remove("this") # Removes first occurence
print("Removing this-----")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

#testing the sor()
list1.sort()
print("SORTED-----")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

#testing reverse
list1.reverse()
print("REVERSED-----")
for index, value in enumerate(list1):
    print("Position:",nameof(index),"[",index,"]",nameof(value),":",value,sep="\t")

# what you can do with lists you can do with strings
string1 = "this is a test"
print("Random choice (string): ",random.choice(string1),sep="\t")

print("This is for TUPLING")
tuple1 = ("this","is",12,13)
for index,value in enumerate(tuple1):
    print(nameof(index),":",index,sep="\t")
    print(nameof(value),":",value,sep="\t")

list2 = list(("cat","dog"))
tuple2 = tuple(("cat","dog",32))

print(nameof(list2),":",sep="\t")
for index,value in enumerate(list2):
    print(nameof(index),":",index,sep="\t")
    print(nameof(value),":",value,sep="\t")

print(nameof(tuple2),":",sep="\t")
for index,value in enumerate(tuple2):
    print(nameof(index),":",index,sep="\t")
    print(nameof(value),":",value,sep="\t")

#testing the ID function
print(id(list1))

import copy
spam = ["test","test1"]
print(id(spam))
spam1 = copy.copy(spam)
print(id(spam1),spam1)

spam = [
    [1,2,3],
    "this",
    "is"
]
print(id(spam))
spam1 = copy.deepcopy(spam)
print(id(spam1),spam1)

