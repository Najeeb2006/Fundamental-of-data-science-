import pandas as pd
from collections import Counter

df = pd.read_csv('q13_reviews.csv')

# Combine all reviews into one text
all_text = ' '.join(df['feedback'].astype(str).str.lower())

# Tokenize
words = all_text.split()

# Count frequency
freq = Counter(words)
freq_df = pd.DataFrame(freq.most_common(), columns=['Word', 'Frequency'])

print("Word Frequency Distribution:")
print(freq_df.to_string(index=False))
print(f"\nTotal unique words: {len(freq)}")
print(f"Most common word: '{freq_df.iloc[0]['Word']}' ({freq_df.iloc[0]['Frequency']} times)")
