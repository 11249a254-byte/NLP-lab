import re
from collections import Counter, defaultdict
corpus = """i am samhi
i like studying nlp
nlp is pretty interesting
the park is pretty
i movie was interesting"""
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)
tokens = tokenize(corpus)
bigrams = list(zip(tokens, tokens[1:]))
bigram_counts = Counter(bigrams)
unigram_counts = Counter(tokens)
probability_matrix = defaultdict(dict)
for (word1, word2), count in bigram_counts.items():
    probability_matrix[word1][word2] = count / unigram_counts[word1]
vocabulary = sorted(set(tokens))
print("\nBigram Probability Matrix:")
print(f"{'Word':<12}", end="")
for word in vocabulary:
    print(f"{word:<10}", end="")
print()
print("-" * (12 + 10 * len(vocabulary)))
for word1 in vocabulary:
    print(f"{word1:<12}", end="")
    for word2 in vocabulary:
        probability = probability_matrix[word1].get(word2, 0)
        print(f"{probability:<10.4f}", end="")
    print()