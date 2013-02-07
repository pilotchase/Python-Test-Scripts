# Demonstrates using the "for" loop with strings

word = input("Enter a word: ")
# "for" being used to print each character from the variable "word"
# in individual order 
print("\nHere's each letter in your word:")
for letter in word:
	print(letter)
# Getting the users' first and last name and then printing both
# using "for" 
firstname = input("\nWhat's your first name? ")
lastname = input("\nWhat's your last name? ")

print("\nSo your name is:")
for wholename in firstname, lastname:
	print(wholename)
question = input("\n[y/n] ")

if question == 'y':
	print("\nI'm glad I got it right")
if question == 'n':
	print("\nOh, I'm sorry. Please re-enter your name: ")
	firstname = input("\nWhat's your first name? ")
	lastname = input("\nWhat's your last name? ")
	print("\nOkay, so your name is:")
	print(firstname, lastname)
else:
	print("\nI'll take that as a yes!")

input("\nThis is the end of this script. Press enter to close")
