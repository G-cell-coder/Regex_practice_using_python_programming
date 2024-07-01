import re
text = "Clearly, he has no excuse for such behaviour to happen intermittently"
for m in re.finditer(r"\w+ly", text):
    print("adverb is the sentence:{0}\n position of occurance in sentence:{1}-{2}".format(m.group(0),m.start(),m.end()))
