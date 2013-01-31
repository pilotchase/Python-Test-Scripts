# Guess my number game
# The object of this game is to guess the correct number

import random

number = random.randint(1, 10)
tries = 1
# This line changes the variable "name" to whatever the users types
name = input("Hello, what\'s your name? ")
# This line prints the name the user entered earliar and adds a "." to it
print("\nHello,", name + ".")
# This is when the game starts
question = input("\nWould you like to play a game? [y/n] ")
if question == "y":
	print("\nI'm thinking of a number between 1 & 10")
	guess = int(input("Take a guess: "))
	if guess > number:
		print("Lower...")
	if guess < number:
		print("Higher...")
	# This line loops "guess" until the user enters the correct number
	while guess != number:
		guess = int(input("Wrong, try again: "))
		# This line adds a number to "tries" every time 
		# the user is wrong
		tries += 1
	if guess == number:
		print("\nYou\'re right! \n and it only took", tries, "tries!")
if question == "n":
	print("\nOh...okay")
