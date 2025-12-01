#creating
mydict={
    "name":"Abdullah Javed",
    "occupation":"Conputer Sceintist",
    "Reg no": 22
}
print(mydict)

#Access
print(mydict["name"])
print(mydict.values())
print(mydict.keys())

#add and update

mydict["name"]="usman javed"
print(mydict)

mydict.update({"name":"Javed"})
print(mydict)

#Loop dictionaries
for i in mydict:
    print(i) #it print the keys
for i in mydict:
    print(mydict[i]) # print values

for x ,y in mydict.items():
    print(x,y)

#nested dictionary

myfamily={
    "child1":{
        "name":"Abdullah"
    },
    "child2":{
        "name":"usman"
    }
}
for x ,ohb in myfamily.items():
    print(x)
    for y in ohb:
        print(y ,ohb[y])
print(myfamily["child1"]["name"])

for child in myfamily.values():
    for value in child.values():
        print(value)
