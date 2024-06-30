import re

text = "The following  100example creates an Arraylist with a capacity of 50 elements with 3 categorized with 12 examples each."

for m in re.finditer("\d+",text):
    print(m.group(0))
    print("Index position:", m.start())
