probabilities = {
    "the": {"DT": 0.9},
    "dog": {"NN": 0.8},
    "barks": {"VB": 0.7},
    "loudly": {"RB": 0.9}
}

sentence = ["the", "dog", "barks", "loudly"]

tagged_sentence = []

for word in sentence:
    if word in probabilities:
        tag = max(probabilities[word], key=probabilities[word].get)
    else:
        tag = "NN"
    tagged_sentence.append((word, tag))

print("Stochastic POS Tagged Sentence:")
print(tagged_sentence)
