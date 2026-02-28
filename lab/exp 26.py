# 26. Simple English to French Translator (No libraries required)

def translate_to_french(text):
    dictionary = {
        "hello": "bonjour",
        "how": "comment",
        "are": "êtes",
        "you": "vous",
        "machine": "machine",
        "learning": "apprentissage",
        "is": "est",
        "very": "très",
        "interesting": "intéressant",
        "good": "bon",
        "morning": "matin"
    }

    words = text.lower().split()
    translated_words = []

    for word in words:
        translated_words.append(dictionary.get(word, word))

    return " ".join(translated_words)


# Test
text = input("Enter English sentence: ")
print("French Translation:")
print(translate_to_french(text))
