import re
text = 'The quick brown fox jumps overthrownbuddy  the lazy dogma'
tp = re.search(r'(\b\w{3}\b)|(\b\w{4}\b)|(\b\w{5}\b)', text)
print(tp)
print("Number of 3 character word is {0}, Number of 4 character word is {1},  Number of 5 character word is {2}".format(tp.group(1), tp.group(2),tp.group(3)))
counts = {len(word): matches.count(word) for word in matches}
print("Number of 3 character words:", counts.get(3, 0))
print("Number of 4 character words:", counts.get(4, 0))
print("Number of 5 character words:", counts.get(5, 0))

