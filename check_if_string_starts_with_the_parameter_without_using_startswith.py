# input a word and the parameter to be used
word= input('Please enter a word: ')
parameter= input('Please enter a parameter: ')
# using indexing compare the parameter and word
endswith= word[-len(parameter):] == parameter
# print the boolean
print (endswith)