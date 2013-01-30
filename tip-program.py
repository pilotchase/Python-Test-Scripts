# This script was written by GhostSquad57
# www.youtube.com/user/ghostsquad57

# Demonstrats treating a value as a condition

print("You're in a fancy restaurant.")
print("\nYou have finished your meal and you enjoyed it very much.", "\nYou request the bill from the waiter and he hands it to you")

print("\nThe waiter clears his throat while holding out his hand. it seems he would like a tip.")

question1 = input("\nWould you like to give the waiter a tip? [y/n] ")

if question1 == "y":
	question2 = int(input("How much will you give him? "))
if question1 == "n":
	print("\nYou tell the waiter you have no money to tip him \nand he walks away with a look of disappointment in his face")

elif question2 >= 1:
	print("\nThank you! \nThe waiter says with a smile on his face")
elif question2 <= 0:
	print("\nYou tell the waiter you have no money to tip him \nand he walks away with a look of disappointment in his face")
else:
	print("\nYou tell the waiter you have no money to tip him \nand he walks away with a look of disappointment in his face")
