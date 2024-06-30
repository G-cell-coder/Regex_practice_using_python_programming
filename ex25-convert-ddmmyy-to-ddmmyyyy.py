'''
import re
ip1 = input("Enter the date and time in yyyy-mm-dd format")
fip1 = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})',ip1)
print("Displaying the date and time is dd-mm-yyyy format:{0}-{1}-{2}".format(fip1.group(3),fip1.group(2),fip1.group(1)))
'''
import re

text = 'The quick brown fox jumps overthrownbuddy  the lazy dogma'
pattern = r'\b(\w{3})\b|\b(\w{4})\b|\b(\w{5})\b'
matches = re.finditer(pattern, text)

counts = {3: 0, 4: 0, 5: 0}

for match in matches:
    for i in range(1, 4):
        if match.group(i):
            counts[len(match.group(i))] += 1

print("Number of 3 character words:", counts.get(3))
print("Number of 4 character words:", counts.get(4))
print("Number of 5 character words:", counts.get(5))
