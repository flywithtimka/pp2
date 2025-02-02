 def reverse_words(sentence):
    words=sentence.split()  
    reversed_sent=" ".join(reversed(words))
    return reversed_sent
input=input("write the text: ")
print(reverse_words(input))