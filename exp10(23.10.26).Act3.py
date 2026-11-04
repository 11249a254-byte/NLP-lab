import nltk
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar_np = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
grammar_all = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*><DT>?<JJ.*>*<NN.*>*}
    PP: {<IN><NP>}
"""
parser_np = nltk.RegexpParser(grammar_np)
parser_all = nltk.RegexpParser(grammar_all)
tree_np = parser_np.parse(tagged)
tree_all = parser_all.parse(tagged)
print("POS Tags:")
print(tagged)
print("\nNP Only Tree:")
print(tree_np)
tree_np.draw()
print("\nNP + VP + PP Tree:")
print(tree_all)
tree_all.draw()
