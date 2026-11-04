import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The young scientist is developing a new application."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
print("POS Tagged Words:")
print(tagged)
grammar1 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*><RB.*>*}
    PP: {<IN><NP>}
"""
parser1 = nltk.RegexpParser(grammar1)
tree1 = parser1.parse(tagged)
print("\nOriginal Chunk Tree:")
print(tree1)
tree1.draw()
grammar2 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*><VB.*><RB.*>*}
    VP: {<VB.*><RB.*>*}
    PP: {<IN><NP>}
"""
parser2 = nltk.RegexpParser(grammar2)
tree2 = parser2.parse(tagged)
print("\nImproved Chunk Tree:")
print(tree2)
tree2.draw()
print("\nError Analysis:")
print("Original grammar may miss the complete phrase 'is developing'.")
print("Improved grammar attempts to group auxiliary and main verbs.")
print("Regular-expression chunking depends on POS tags and grammar rules.")
