#list item are in ordered changeable and allow duplicate one
#python list 
my_list=[1,2,3,4,5]
my_list=[1,True,"abdullah"]
fruits=["apple","pomegranate","mango"]

#access list items
print(fruits[1])
print(fruits[-1])
print(fruits[0:3])
print(fruits[-1:-3])

#Change list item
fruits[1]="leeche"
print(fruits)

fruits[1:3]=["Gava","Dates"]
print(fruits)

#insert
fruits.insert(1,"peach")
print(fruits)

#append
fruits.append("red grapes")
print(fruits)

#extend
vegitables=["Avocado","Beet","Broccoli","Cabbage","Coliflower"]
fruits.extend(vegitables)
print(fruits)

#remove

#remove -it remove specific value
fruits.remove("apple")
print(fruits)
#pop -remove by giving specific index
fruits.pop(1)
print(fruits)

#del completely delete the list
del(vegitables)

#clear remover all the values from the list
print(f"fruits {fruits}")
fruits.clear()
print(fruits)

#loop on list
a=[1,2,3,4,5]
for i in a:
    print(i)
    
#list comprehension
a=[1,2,3,4,5]
count=0
for i in range(len(a)):
    count+=1
print(count)
programming_language=["C++","Python","java"]
for i in programming_language:
    if "P" in i:
        print(i)
#sort list

a=[5,4,3,2,1]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("sorted list", a)

d=[43,33,43,1,13]
d.sort()
print(d)

