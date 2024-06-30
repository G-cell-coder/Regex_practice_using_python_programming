import re
text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
print("Original Text: ",text)
new_text = re.sub(r'\x1b[^m]*m','', text)
print("New Text: ",new_text)

