import re
from collections import Counter
corpus = """i am samhi
i like studying nlp
nlp is pretty interesting
the park is pretty
i movie was interesting"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>", "<s>", "<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
bigram_counts = Counter()
trigram_counts = Counter()
quadgram_counts = Counter()
vocab = set()
for sent in sentences:
    vocab.update(sent)
    for i in range(len(sent) - 3):
        bigram_counts[(sent[i], sent[i + 1])] += 1
        trigram_counts[(sent[i], sent[i + 1], sent[i + 2])] += 1
        quadgram_counts[
            (sent[i], sent[i + 1], sent[i + 2], sent[i + 3])
        ] += 1
V = len(vocab)
def quadgram_prob(w1, w2, w3, w4, smoothing=True):
    if smoothing:
        return (
            quadgram_counts[(w1, w2, w3, w4)] + 1
        ) / (
            trigram_counts[(w1, w2, w3)] + V
        )
    denom = trigram_counts[(w1, w2, w3)]
    return (
        quadgram_counts[(w1, w2, w3, w4)] / denom
        if denom else 0
    )
print(f"{'Quadgram':<40}{'Count':<8}{'P(w4|w1,w2,w3)':<20}")
print("-" * 68)
for (w1, w2, w3, w4), c in quadgram_counts.most_common(6):
    print(
        f"({w1}, {w2}, {w3}, {w4})"
        f"{'':<6}{c:<8}"
        f"{quadgram_prob(w1, w2, w3, w4):<20.4f}"
    )
def sentence_probability(sentence):
    tokens = tokenize(sentence)
    prob = 1.0
    for i in range(len(tokens) - 3):
        prob *= quadgram_prob(
            tokens[i],
            tokens[i + 1],
            tokens[i + 2],
            tokens[i + 3]
        )
    return prob
test = "i like studying"
print(f"\nP(\"{test}\") = {sentence_probability(test):.10f}")