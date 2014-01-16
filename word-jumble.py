# Word Jumble

# The computer picks a random word and then "jumbles" it
# The object is to guess what the orignal word was

import random

# create a sequence of words to choose from
WORDS = ("python", "ruby", "c++", "pearl", "java", "lisp", "haskell")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the player was right
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# TIME TO PLAY THE GAAAAME!
print(
"""
\t\t\tWelcome to Word Jumble!

\t\tUnscramble the letters to make a word.
\t     (Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble, "\n(type \"Hint\" for a hint)")

guess = input("\nYour Guess: ")
while guess == "hint":
    print("\nIt's a programming language...")
    guess = input("\nYour Guess: ")
while guess != correct and guess != "":
    print("Sorry,", guess, "is wrong")
    guess = input("\nYour Guess: ")

if guess == correct:
    print("""\n\n
    ##################
    #CONGRATULATIONS!#
    ##################
    You answered right!
    """)

print("\nThanks for playing!")
input("\n\nPress enter to exit")
