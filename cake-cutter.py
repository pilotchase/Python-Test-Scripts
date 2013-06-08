# Cake Cutter
# Demonstrates string slicing
word = "HAPPY BIRTH DAY "

print(
"""
Slicing 'Cheat Sheet'

 0   1   2   3   4   5
 +---+---+---+---+---+
 | H | A | P | P | Y |
 | B | I | R | T | H |
 |   | D | A | Y |   |
 +---+---+---+---+---+
-5  -4  -3  -2  -1

"""
)
print("Enter the beginning and ending index for your slice of 'cake'")
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
