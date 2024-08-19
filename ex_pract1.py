import re

text_to_search = """ phone numbers are 123-456-6937 \n
                      345.789.1345 \t Mr. robinson, Mr.michael, Mrs.Owleson"""

#pattern = re.compile('\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

regex = re.findall(r"([Mr|Ms|Mrs]*\.\w+)", text_to_search)
print(regex)
with open('data.txt','r', encoding='utf-8') as f:
    contents = f.read()
 
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
