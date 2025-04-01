# input a word and the parameter
word = (input('Please enter a word: '))
parameter = (input('Enter the character or substring to be counted: '))
# using while loop, count the parameter in the word
count = 0
position = 0
while position <= len(word) - len(parameter):
    if word[position:position + len(parameter)] == parameter:
        count += 1
        position += len(parameter)
    else:
        position += 1
# print how many times the parameter appeared
print (count)