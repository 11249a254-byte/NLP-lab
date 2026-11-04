from collections import Counter

sentences = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]

words = []

for sentence in sentences:
    words.extend(sentence.split())

word_freq = Counter(words)
total_words = len(words)

print("Unigram Probabilities")
for word in word_freq:
    print(f"P({word}) = {word_freq[word] / total_words:.4f}")

bigrams = []

for sentence in sentences:
    tokens = sentence.split()
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))

bigram_freq = Counter(bigrams)

print("\nBigram Probabilities")
for (w1, w2), count in bigram_freq.items():
    print(f"P({w2}|{w1}) = {count / word_freq[w1]:.4f}")