#question 2

user_input = print (input("Type anything:")) #get the user input

#the number of characters
characters = len(user_input)
print (characters)
def integer (s):
    return s == s[::-1]
#Initialize the number of uppercase letters in the string.
uppercase = sum(1 for char in user_input if char.isupper())
print (uppercase)

#Initialize lower case
lowercase_count = sum(1 for char in user_input if char.islower())
 
 #print
print("Total number of characters: {characters}")
print("Number of uppercase letters: {uppercase}")
print("Number of lowercase letters: {lowercase}")