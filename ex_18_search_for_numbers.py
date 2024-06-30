import re
results = re.finditer(r"([0-9]{1,3})","Excercises number 1,12,13 and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
