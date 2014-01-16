# Demonstrates the "len()" function and the "in" operator

vowels = ("a", "e", "i", "o", "u", "y")
message = input("Enter a message: ")

print("\nThe length of your message is", len(message), "characters")

print("\nNow, let's see what characters are vowels and which ones are not:")
for letter in message:
	# line #12 converts all the values of the variable "vowels" to uppercase
	# line #13 & #15 then prints them in lowercase form
	vowels == message.upper()
	if letter.lower() in vowels:
		print(letter.lower(), "[✓]")
	elif letter.lower() not in vowels:
		print(letter.lower(), "[x]")
