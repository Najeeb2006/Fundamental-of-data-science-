import re

sentence = "The cats are running"
words = sentence.split()

for w in words:
    if re.match(r'.*ing$', w):
        tag = "VBG"
    elif re.match(r'.*s$', w):
        tag = "NNS"
    elif w.lower() in ["the", "a", "an"]:
        tag = "DT"
    else:
        tag = "NN"
    print(w, tag)
