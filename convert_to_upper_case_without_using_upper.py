# enter a word
word = input('Please enter a word: ')
# translate the word to it's upper case counter part
reference = str.maketrans("abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")
upper_cased = word.translate(reference)
# print the upper cased word
print (upper_cased)