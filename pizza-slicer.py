# Pizza Slicer
# Demonstrates string slicing
word = "pizza"

print(
"""
Slicing 'Cheat Sheet'

 0   1   2   3   4   5
 +---+---+---+---+---+
 | p | i | z | z | a |
 +---+---+---+---+---+
-5  -4  -3  -2  -1

"""
)
print("Enter the beginning and ending index for your slice of 'pizza'.\n \
Type 'random' for a random slice.")
print("\nPress the enter key at 'Start' to exit")
# using 'None' to initialize a variable
# Note that 'None', condition wise, is always 'False'
start = None

while start != "":
	start = (input("\nStart: "))
	if start:
		start = int(start)
		
		finish = int(input("Finish: "))
		
		print("word[", start, ":", finish, "] is", end=" ")
		print(word[start:finish])

input("\n\nPress the enter key to exit")
