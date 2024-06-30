import re

text = "PythonTutorialAndExercise"
regex = re.findall('[A-Z][^A-Z]*',text)
print(regex)
