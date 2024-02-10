def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence ="I am learning python "
word_count = count_words(sentence)
print("Number of words in the sentence : ",word_count)