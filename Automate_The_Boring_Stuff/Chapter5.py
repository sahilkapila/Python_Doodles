import sys,random,os,platform,time, copy
from varname import nameof

mydictionary ={
    "attr1":"val1",
    "attr2":"val2"
}

for index,atrr in enumerate(mydictionary):
    value  = mydictionary[atrr] #Cannot refer to dictionary with index only attr name
    print(nameof(index),":",index,nameof(atrr),":",atrr,nameof(value),":",value,sep="\t")

mydictionary.pop("attr2")

for index,atrr in enumerate(mydictionary):
    value  = mydictionary[atrr] #Cannot refer to dictionary with index only attr name
    print(nameof(index),":",index,nameof(atrr),":",atrr,nameof(value),":",value,sep="\t")

mydictionary2 ={
    "attr2":"val2",
    "attr1":"val1"
}

# comparing prior to pop = not equal
print(mydictionary == mydictionary2)

mydictionary2.pop("attr2")
#Equal
print(mydictionary2 == mydictionary)

try:
    print(mydictionary["attr3"])
except KeyError:
    print("Item not found!")

# Now we leverage the keys(), values() and items() methods for dictionaries

dict1 = {
    "First":"value1",
    "Second":"value2",
    "Third":"value3"
}
try:
    print(dict1["third"])
except KeyError:
    print("NOTE: the key-value pairs are case sensitive!!")

for keys in dict1.keys():
    print(nameof(keys),":",keys,sep="\t", end="\n")
    print(nameof(dict1),"[",keys,"]",":", dict1[keys], sep="\t", end="\n")

for values in dict1.values():
    print(nameof(values),":", values,sep="\t",end="\n")

# You cannot get an index from a value in dictionary

for keys,values in dict1.items():
    print(nameof(keys),":",keys, sep="\t")
    print(nameof(values),":",values, sep="\t")

#check if the value exists in a dictionary

if "value3" in dict1.values():
    print("Value 3 Found!")

if "Third" not in dict1.keys():
    print("Value not found!")
else:
    print("Third is found!")


print("hello")
#checking if the key exists in the diction
sys.exit(1)