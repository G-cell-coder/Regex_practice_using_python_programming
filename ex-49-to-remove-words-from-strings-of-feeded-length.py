import re
inptext = input("Enter the string")
c =int(input("Enter the boundary length till that string will be stored\n"))

pattern = re.compile(r"\W*\b\w{1,%s}\b" % c)
regex = pattern.sub('', inptext)
print(regex)
