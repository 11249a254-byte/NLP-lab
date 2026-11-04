dataset = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]

print("Dataset")
for sentence in dataset:
    print(sentence)

print("\nGrammar-Based Model")
print("I like NLP -> Grammatically Correct")
print("Python like I -> Grammatically Incorrect")

print("\nStatistical Model")
print("I like NLP -> High Probability")
print("Python like I -> Low Probability")

print("\nComparison")
print("Grammar-Based Model uses grammar rules.")
print("Statistical Model uses probabilities learned from data.")