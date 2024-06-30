import re

str1 = input("Enter the string with exceeed spaces with the words")

regex = re.sub('\s+',' ', str1)
print(regex)


