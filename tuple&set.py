mytuple=("apple","mango","grapes")
mytuple1=(True,False,True)
mytuple2=(1,2,3,4,1)

print(mytuple)
print(mytuple1)
print(mytuple2[3])

# mytuple2[3]="apple" #gives an error because tuple is unchangeable
# print(mytuple2)
#one way to update in a tuple by casting it in a list and then back to tuple

#loop over tuple
num=(1,2,3,4,5)
for i in num:
    print(i)
tuple3=mytuple2+mytuple1
print(tuple3)


#Sets
#A set is a collection which is unordered, unchangeable*, and unindexed.
set={1,2,3,4,6,1}
for i in set:
    print(i)

#add 
set.add(10)
set.update({"apple"})
print(set)

#remove-it remove an item but gives an error if item is not present
# set.remove(11)

set.remove(10)
print(set)

#discard it remove an item bu never throw an error if
#  it is not present
set.discard(11)
print(set)
#clear it completely clear all the elements
set.clear()
print(set)
#del -completely delete a set
del set
print(set)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3 ,"a"}

set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set1.difference(set2)

A = {1, 2, 3}
B = {1, 2}

print(B.issubset(A))   # True

#Unlike sets, elements cannot be added or removed from a frozenset.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#while loop
x=0
while(x<=5):
    print(x)
    x=x+1
