# input a word and the parameter to find
word = (input('Please enter a word: '))
parameter = (input('Enter the character or substring to be searched: '))
# using for loop, search the rightmost parameter then break when the parameter is found
for position in range(len(word) - len(parameter), -1, -1):
    if word[position:position + len(parameter)] == parameter:
        break
# print the postion of the parameter
print (position)