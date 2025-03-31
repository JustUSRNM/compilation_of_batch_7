# input a word with leading spaces
word= input('Please enter a word with mutiple starting spaces:')
# count number of spaces at the end
number_of_spaces= 0
while word[number_of_spaces] == " ":
    number_of_spaces += 1
# remove the spaces
word_no_spaces= word[number_of_spaces:]
#print the word without the spaces
print (word_no_spaces)