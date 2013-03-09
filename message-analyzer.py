# Demonstrates the "len()" function and the "in" operator

message = input("Enter a message: ")

print("\nThe length of your message is", len(message), "characters")

print("\nYour message contains the following vowels:")
if "" in message:
	print("")
	if "a" in message:
		print("a")
	if "e" in message:
		print("e")
	if "i" in message:
		print("i")
	if "o" in message:
		print("o")
	if "u" in message:
		print("u")
	if "y" in message:
		print("y")
