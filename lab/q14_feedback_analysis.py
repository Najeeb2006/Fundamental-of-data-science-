import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

# Load dataset
df = pd.read_csv('data.csv')

# Preprocessing
stop_words = {'the','and','is','a','an','in','it','of','to','for',
              'on','with','as','by','at','from','this','that','was',
              'are','be','or','not','have','has','i','you','we','they'}

all_words = []
for review in df['feedback'].astype(str):
    # Lowercase and remove punctuation
    text = review.lower().translate(str.maketrans('', '', string.punctuation))
    words = [w for w in text.split() if w not in stop_words]
    all_words.extend(words)

freq = Counter(all_words)

# User input for N
N = int(input("Enter N (number of top words to display): "))
top_n = freq.most_common(N)
words_list, counts = zip(*top_n)

print(f"\nTop {N} most frequent words:")
for word, count in top_n:
    print(f"  {word}: {count}")

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar(words_list, counts, color='steelblue', edgecolor='black')
plt.title(f'Top {N} Most Frequent Words in Customer Feedback')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('q14_word_freq.png')
plt.show()
print("Bar chart saved as q14_word_freq.png")
