import nltk
sentences = [
    "The students attend lectures in the auditorium.",
    "The professor explains the topic in the classroom.",
    "The librarian organizes books on the shelves.",
    "The researchers develop a new project in the laboratory.",
    "The university provides accommodation for students."
]
grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<VB.*><DT|PRP\$>?<JJ.*>*<NN.*>*}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged)
    print("\nSentence:", sentence)
    print("Chunk Tree:", tree)
    tree.draw()
    print("Recognized phrases:")
    for subtree in tree.subtrees():
        if subtree.label() in ("NP", "VP", "PP"):
            phrase = " ".join(word for word, tag in subtree.leaves())
            print(subtree.label(), ":", phrase)
