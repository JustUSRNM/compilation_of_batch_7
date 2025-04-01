# input a word and the width parameter of rjust
word= input('Please enter a word: ')
parameter= int(input('Enter what width the word be in: '))
# the difference between the width and the word is the amount of spaces added
if parameter > len(word):
    spaces= parameter - len(word)
elif parameter <= len(word):
    spaces = 0
# print the word that justified to the right
print (word+ spaces*" ")