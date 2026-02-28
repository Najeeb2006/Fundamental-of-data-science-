import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLP is very interesting"
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

print("POS Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)
