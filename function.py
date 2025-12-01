def func():  #a fuction with no argument and no return value
    print("hello bro")

func()
 
#a function with argument and no return values
def sum(a , b):
    c=a+b
    print(c)

sum(1,2)

#a function with argument and return values

def add(a,b): #the declared a and b is parameters
    c=a+b
    return c

d=add(3,1) #these passing values in arguments
print(d)

#*args - when we want to pass multiple argument than we use arg it return a tuple

def sum(*args):
    sum1=0
    for i in args:
        sum1=sum1+i
    return sum1

a=sum(1,2,3,4,5,6)
print(a)

#**kwargs  when you want to pass unlimited key value args it returns dict

def func(**kwargs):
    return kwargs

a = func(name="Ali", age=30, specialization="Data Science")
print(a)

#Recursion
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)

a=fac(5)
print(a)

#fibonacci
def fab(n):
    if n==1 or n==0:
        return n
    else:
        return fab(n-1)+fab(n-2)

a=fab(3)
print(a)

#lambda function
square=lambda x: x**2
a=square(2)
print(a)

#if i want to pass function as argument
def function(square,value):
    return 2+square(value)

a=function(square,2)
print(a)
