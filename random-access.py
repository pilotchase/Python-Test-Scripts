# Demonstrates string indexing

import random

word = input("Enter a word: ")
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
	position = random.randrange(low, high)
	print("word[", position, "]\t", word[position])

# Printing a string backwards using string indexing
word = input("\nNow enter a five letter word: ")
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
