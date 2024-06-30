import re
inp1 = input("enter the string to get parsed\n")
pat = r"\b\w{4}\b"

sp = re.findall(pat,inp1)

print(sp)
for i in (1,len(sp)):
    print(i)
