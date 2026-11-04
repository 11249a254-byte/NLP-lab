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

vocab = list(word_freq.keys())
V = len(vocab)

bigrams = []

for sentence in sentences:
    tokens = sentence.split()
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))

bigram_freq = Counter(bigrams)

def smoothed_probability(sentence):
    tokens = sentence.split()
    probability = 1

    for i in range(len(tokens) - 1):
        c1 = bigram_freq[(tokens[i], tokens[i + 1])]
        c2 = word_freq[tokens[i]]
        probability *= (c1 + 1) / (c2 + V)

    return probability

print("I like NLP :", smoothed_probability("I like NLP"))
print("Python like I :", smoothed_probability("Python like I"))