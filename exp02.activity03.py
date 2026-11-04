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

bigrams = []

for sentence in sentences:
    tokens = sentence.split()
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))

bigram_freq = Counter(bigrams)

def sentence_probability(sentence):
    tokens = sentence.split()
    probability = 1

    for i in range(len(tokens) - 1):
        if (tokens[i], tokens[i + 1]) in bigram_freq:
            probability *= bigram_freq[(tokens[i], tokens[i + 1])] / word_freq[tokens[i]]
        else:
            probability = 0

    return probability

s1 = "I like NLP"
s2 = "Python like I"

p1 = sentence_probability(s1)
p2 = sentence_probability(s2)

print(s1, ":", p1)
print(s2, ":", p2)

if p1 > p2:
    print("More probable sentence:", s1)
else:
    print("More probable sentence:", s2)