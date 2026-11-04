import nltk
sentence = "The students read their textbooks."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged)
print("POS Tags:", tagged)
print("\nUpdated Grammar:")
print(grammar)
print("\nChunk Tree:")
print(tree)
tree.draw()
print("\nNoun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))
