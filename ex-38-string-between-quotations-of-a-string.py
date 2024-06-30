import re

str1 = input("Enter the quotation\n")
pattern = "[a-z A-Z \w]+"
regex1 = re.findall(pattern,str1)
print(regex1)
