sentences=["I like NLP",
           "I like Python",
           "I study NLP"]
word_frequency={}
bigram_frequency={}
for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
    for i in range(len(words)-1):
        bigram=words[i]+""+words[i+1]
        if bigram in bigram_frequency:
            bigram_frequency[bigram]+=1
        else:
            bigram_frequency[bigram]=1
print("word frequency:")
for word in word_frequency:
    print(word,":",word_frequency[word])
print("bigram frequency:")
for bigram in bigram_frequency:
    print(bigram,":",bigram_frequency[bigram])
