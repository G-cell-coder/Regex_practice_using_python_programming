import re
def match_num(string):
    text = re.compile(r"^" + inpat)
    if text.match(string):
        return True
    else:
        return False

inpat = input("Enter the specific number to get parsed at the start of the string:\n")
print(match_num('5-2345861'))
print(match_num('6-2345861'))

