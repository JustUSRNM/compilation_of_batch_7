# input a number and the the parameter 
number = int(input('Please enter a number: '))
parameter = int(input('Enter how many digit: '))
# covert the number to a string
string_number = str(number) 
# subtract the parameter to the length of the number to get how many zeroes are added
zeroes = parameter - len(string_number)
# print the number with the zeroes
print (zeroes*"0" + string_number)