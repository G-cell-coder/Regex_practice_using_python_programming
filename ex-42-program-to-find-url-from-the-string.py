import re

str1 = input("ENter the URL along with string attached\n")
regex = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str1)
print(regex)
