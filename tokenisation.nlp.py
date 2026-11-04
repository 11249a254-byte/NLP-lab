from nltk.tokenize import sent_tokenize, word_tokenize
input = ("i am going to college")
sent_tokenize(input)
print(sent_tokenize(input))
word_tokenize(input)
print(word_tokenize(input))
for i in word_tokenize(input):
    print(i)