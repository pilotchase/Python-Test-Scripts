# Demonstrates the "len()" function and the "in" operator

message = input("Enter a message: ")
VOWELS = "a", "e", "i", "o", "u", "y",

print("\nThe length of your message is", len(message), "characters")

print("\nYour message contains the following vowels:")
for VOWELS in message:
	print(VOWELS)
