#Arthmetic Operators
a=2
b=5
print(a*b)
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Assignment Operators

x=1
x+=3
print(x)
x-=3
print(x)

x/=3
print(x)
x=1
x*=3
print(f"{x}")

x&=3
print(x)
x|=3
print(x)

x^=3
print(x)
x>>=3
print(x)

#Right shift assignment
#in which in each shift we divide by 2
x=40
x>>=3
print(x)

#left shift addignment 
#in which in each shift we  multiply by 2
x=2
x<<=3
print(x)

#warlus operator - assign and used at same time
print(a:=1)

#Comparison operator
x=5
y=3
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x>y)
print(x<y)

#logical operators
#and
a=5
print(f"and operator {a>0 and x<10}")

#or
print(f"or operator {a==1 or a>0}")
#not
print(not(a==1))


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is y) # is operator true when both var point to the same obj
print(x==y) # check the values of each other

#Membership operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

print("pomegranate" not in fruits)

