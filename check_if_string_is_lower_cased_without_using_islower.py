# input a word
word = input('Please enter a word: ')
# using for loop, check if all is lowwer cased then break when an upper case is found
is_lower = True
for char in word:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
# print the boolean
print (is_lower)