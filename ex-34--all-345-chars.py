import re

text = 'The quick brown fox jumps overthrownbuddy  the lazy dogma'
matches = re.findall(r'\b\w{3}\b|\b\w{4}\b|\b\w{5}\b', text)

counts = {3: 0, 4: 0, 5: 0}

for word in matches:
    counts[len(word)] += 1

print("Number of 3 character words:", counts.get(3))
print("Number of 4 character words:", counts.get(4))
print("Number of 5 character words:", counts.get(5))

