# Demonstrates using the "for" operator with strings

word = input("Enter a word: ")
# "for" being used to print each character from the variable "word"
# in individual order 
print("\nHere's each letter in your word:")
for letter in word:
	print(letter)
# Using the "for" operator and "range()" function to print "word" 5 times
for i in range(5):
	print(word, "\nHuh. You ever get the feeling of Deja Vu?")

# Using the "range()" function with loop to count numbers
print("\nCounting:")
for i in range(11):
	print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(0, 55, 5):
	print(i, end=" ")

print("\n\nCounting backwards")
for i in range(10, 0, -1):
	print(i, end=" ")

# Getting the users' first and last name and then printing both
# using "for" 
firstname = input("\n\nWhat's your first name? ")
lastname = input("\n\nWhat's your last name? ")

print("\nSo your name is:")
for wholename in firstname, lastname:
	print(wholename)
question = input("\n[y/n] ")

if question == 'y':
	print("\nI'm glad I got it right")
elif question == 'n':
	print("\nOh, I'm sorry. Please re-enter your name: ")
	firstname = input("\nWhat's your first name? ")
	lastname = input("\nWhat's your last name? ")
	print("\nOkay, so your name is:")
	print(firstname, lastname)
else:
	print("I'll take that as a yes!")

input("\nThis is the end of this script. Press enter to close")
