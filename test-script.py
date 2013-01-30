# Python test script made for learning purposes
# Note that this script was made to be executed with Python version 3.2
# Creating a "variable"
name = "GhostSquad57"

# Examples of the "print" function being used to print a string of text:
print("This script was created by", name)
input("   www.youtube.com/user/ghostsquad57")

# You can print multiple values with a single call to the "print()" function-just list multiple arguments values, seperated by commas.
# I print multiple values with the following line:
print("\nLinux is", "a \"Kernal\"", "NOT a Operating System!")

# Using "Triple-Quote Strings" to print ASCII art:
print('''
\t\t\t _______________
\t\t\t|  ___________  |
\t\t\t| |           | |
\t\t\t| |   0   0   | |
\t\t\t| |     -     | |
\t\t\t| |   \___/   | |
\t\t\t| |___________| |
\t\t\t|_______________|
''')

# Joining two strings together to make one long string
# Using the "+" operator:
input("GNU" + "/" + "Linux")

# Repeating a string of text with the "*" operator:
print("I bet you can\'t say that 10x fast!")
print("\nGNU/Linux" * 10)

# Using Python to solve math problems
input("\nPython knows math!")
# Two "//" translates to "divide". "%" translates to "a remainder of"
print("1337/337 =", 1337 // 337, "with a remainder of", 1337 % 337)
# Creating questions with the "if" and "while" statements
mathquestion = ""
while mathquestion != "2":
	mathquestion = input("\nWhat\'s 1+1? ")
print("Correct!")

print("\nHow much money the average person spends on a 2-liter of soda daily (with taxes)")
soda = 1.07
print(soda)
soda *= 365
print("So that's...", soda, "a year")

question = input("\nQuestion: Who created the Linux Kernal? ")
if question == "Linus Torvalds":
	print("Correct!")
elif question == "linus torvalds":
	print("Correct!")
elif question == "some guy from sweden":
	print("That works too...")
else:
	print("Wrong!")
input("Press enter to continue")

# Manipulating strings with "string methods":
print("\nAnd since we're talking about Linus Torvalds, I might as well share one of his", "\nquotes:")
quote = "\"Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.\""
print(quote.title())
print("\nWhat he would've said if he worked for Microsoft:")
print(quote.replace("not", "mainly" ,1))

# Getting users' input via the "int()" function
# Also, notice that "int()" and "input()" are "nested"
# "nesting" is the act of combining two functions together to perform complex tasks
weight = int(input("\nHow many pounds do you weigh? "))
moon_weight = weight / 6
sun_weight = weight * 27.1
print("Did you know on the moon you would weigh only", moon_weight, "pounds?")
print("And on the sun you would weigh", sun_weight, "pounds")

# Using the "import" function to load a module
import random
# Generating random numbers using the "random" module
input("\nPress enter to roll dice!")
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2
print("You rolled a", dice1, "and a", dice2, "for a total of", total)

# Demonstrats the "continue" and "break" statment
count = 0
while True:
	count += 1
	if count > 10:
		break
	if count == 5:
		continue
	print(count)

input("\nThis is the end of this script. Press the enter key to close")
