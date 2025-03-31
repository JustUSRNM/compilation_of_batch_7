# enter a word and the suffix to be removed
word = input('Please enter a word: ')
parameter = input('Please enter a prefix that is in the word: ')
# check if the suffix is in the word
if word.endswith(parameter):
# get the len of the suffix and remove it to the word
    no_suffix = word[:-len(parameter)]
# print the word without the suffix
    print (no_suffix)