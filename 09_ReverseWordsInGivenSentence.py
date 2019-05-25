def rev_words(sentence):
    return " ".join(sentence.split()[::-1])

your_sentence = str(input("Enter your sentence: "))
print("\nGiven sentence in reverse format: ")
print (rev_words(your_sentence))





