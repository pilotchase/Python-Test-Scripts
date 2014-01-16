# Hero's Inventory
# Demonstrates tuple creation

# To create a tuple, you just surround a sequence of values, seperated by commas,
# with parentheses.
# Even a pair of lone parentheses is a valid (but empty) tuple.

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are currently empty-handed.")

input("\nA chest lies in front of you.\nPress enter to open it.")

# Create a tuple with some items
inventory = ("sword",
        "armor",
        "shield",
        "healing potion",
        "food")

# Print the tuple
print("\nThe chest contained:")
print(inventory)

# concatenate two tuples
riches = ("gold", "gems")
print("\nYou also find:", riches)
inventory += riches
print("\nYou now have", len(inventory), "items in your possession.\nIncluding:")

# Print each element in the tuple
for item in inventory:
    print(item)

# Test for membership with "in"
if "food" in inventory:
    print("\nYou have food in your inventory.\
            \nYou will live to fight another day")

input("\n\nPress enter to open your inventory.")

print(
"""
(0)   (1)   (2)    (3)            (4)  (5)  (6)
|sword|armor|shield|healing potion|food|gold|gems|
(-7)  (-6)  (-5)   (-4)           (-3) (-2) (-1)
"""
)
# Display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("You have selected:", inventory[index], "[", "num", index, "]")

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index begin to finish a slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])
