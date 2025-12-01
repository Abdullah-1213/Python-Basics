import re
text="my phone number is 03010000000"
#make a pattern that help us to find 
patter=r"\d+"
result=re.findall(patter,text)
print(result)


email="abdullah134@gmail.com"
pattern=r"^[\w]+@\w+\.\w+$"

result=re.findall(pattern,email)
print(result)