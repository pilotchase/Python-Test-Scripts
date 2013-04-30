# Demonstrates the "len()" function and the "in" operator

vowels = "a", "e", "i", "o", "u", "y"
message = input("Enter a message: ")

print("\nThe length of your message is", len(message), "characters")

print("\nYour message contains the following vowels:")
for letter in message:
	vowels == message.upper()
	if letter.lower() in vowels:
		print(letter.lower())
	if letter.lower() not in vowels:
		print("None")
