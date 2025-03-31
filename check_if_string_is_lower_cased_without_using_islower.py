# input a word
word= input('Please enter a word: ')
# using for loop, check if all is lowwer cased then break when an upper case is found
is_upper= True
for char in word:
    if 'a' <= char <= 'z':
        is_upper= False
        break
# print the boolean
print (is_upper)