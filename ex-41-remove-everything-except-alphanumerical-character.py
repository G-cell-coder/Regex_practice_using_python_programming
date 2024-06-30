import re

str1 = input("Enter the string with alphanumeric and character mixed\n")

regex = re.sub("\W", '', str1)
print(regex)
