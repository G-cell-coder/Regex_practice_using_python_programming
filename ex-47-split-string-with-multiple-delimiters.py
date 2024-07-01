import re
text = input("Enter the sentence for which the text to be splitted\n")
s_text = re.split(';|,| \*|\n',text)
print(s_text)

