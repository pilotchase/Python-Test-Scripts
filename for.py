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

# Using the "range()" function with "for" to count numbers
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
else:
	print("I'll take that as a yes!")
# Keep asking name until the user says "y"
while question == 'n':
	wholename = input("\n\nAlright, let's give this another shot.\nWhat's your whole name? ")
	print("\n", wholename)
	question = input("\nSo this is your name? [y/n] ")
	if question == 'y':
		print("\nI knew that!")
	elif question == 'n':
		# Calls back to line #42 if the user says "n"
		wholename
	else:
		print("\nAlright, I give up!")

input("\nThis is the end of this script. Press enter to close")
