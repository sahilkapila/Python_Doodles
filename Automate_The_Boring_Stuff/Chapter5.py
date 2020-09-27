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

