import re
text = 'The quick brown fox jumps overthrownbuddy  the lazy dogma'
print(re.findall(r"\b\w{5}\b", text))

