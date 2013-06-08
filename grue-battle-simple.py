# Using the "while" statment to simulate a encounter with a army of Grues
import random

input("\nGASP! a army of Grues have appeared! \nPress enter to fight them!")
# health for both the player and grues
health = 10
grue = 0
damage = random.randint(1, 10)
# while the player's health is greater than or equal to 0
# add a grue and inflict damage onto him
# the damage variable decides how much damage gets inflicted on both the player and enemies
while health >=0:
	grue += 1
	health -= damage

	print("\nYou have slain a Grue, " \
"but you took", damage, "damage points.\n")

print("You fought well and slain", grue, "Grues.")
print("But alas, you were defeated")

input("\nThis is the end of this script. Press the enter key to close")
