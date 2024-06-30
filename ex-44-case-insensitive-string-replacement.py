import re

text = "PHP PythonTutorialAndExercise"
reg1 = re.findall(r'[A-Z]+\W',text)
regex = re.sub(r'([A-Z]+\W)',reg1[0].lower(),text)
print(regex)
