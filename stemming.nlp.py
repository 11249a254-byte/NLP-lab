from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_text= "It is important to be pythonly while you are pythoning with python . All pythoners are have poorly pythoned atleast once"
ex_words = word_tokenize(new_text)
for w in ex_words:
    print(ps.stem(w))