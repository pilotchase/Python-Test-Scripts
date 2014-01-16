# Cake Cutter
# Demonstrates string slicing
word = "HAPPY BIRTH DAY "

print(
"""
Slicing 'Cheat Sheet'

 +---+---+---+---+---+
 | H | A | P | P | Y |
 0                   |
 |(1)|(2)|(3)|(4)|(5)|
 +---+---+---+---+---+
 | B | I | R | T | H |
 6                   |
 |(7) (8) (9) (10) (11)
 +---+---+---+---+---+
 |   | D | A | Y |   |
 12                  16
 |   |(13)(14)(15)   |
 +---+---+---+---+---+

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
		# converts value of "start" to an integer
		start = int(start)
		# does the same as line #28 but "finish" is the variable that is converted
		finish = int(input("Finish: "))

		print("word[", start, ":", finish, "] is", end=" ")
		print(word[start:finish])

input("\n\nPress the enter key to exit")
