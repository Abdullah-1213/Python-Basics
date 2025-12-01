#print statment show output
print("Hello world")
print("hye bro learning python is fun ");print("are you crazy i love java only")
print("hye bro learning python is fun "),print("are you crazy i love java only")

#the two print statment in one line cause errors
#print("hye bro learning python is fun ")print("are you crazy i love java only")

#printing output numbers
print(2*4)
print(222)
print(22/22)

print("i am",35,"years old")

#Variable 
#variable created when a value assign in it there is no need to declare a type of value in pythn
a=1
b="abdullah"
c=1.6
d="2000"

var_arr=[1,"abdullah",1.6,True,20000]
for i in var_arr:
    print(type(i)) # type is used to find the data type of variable

#type casting 
print(float(a))
print(int(d))

#variable names
#there are many technique to assign a name
#camelcase-in which first letter of word in lower case only
my_Values=1

#PascalCase every letter of word is capital
My_Games=2

#Every word seperated by underscores

my_toys=2

#Local vs Global variables

#local varaible defined in a function and created and deleted when a function start
#cant access outside of function
a=[1,2,3,4,5]

def func(a):
    for i in a:
        count=0#local variable 
        count+=1
        print(count)


# print(f"count  {count} ") it cause error because it access a local var