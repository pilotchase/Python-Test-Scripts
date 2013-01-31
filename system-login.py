# Demonstrats logical "operators" and "compound" operators
# Simulates logging into a private network

print("\n\tThis network is only accessible by exclusive members")
print("\n\t\tPlease enter your login information\n")

security = 0

username = ""

while not username:
	username = input("Username: ")

password = ""

while not password:
	password = input("Password ")

if username == "keifers" and password == "577500":
	print("\nWelcome, Keifers")
	security = 10
elif username == "timothy" and password == "timdaking":
	print("\nWelcome, King Tim")
	security = 7
elif username == "guest" or password == "guest":
	print("\nWelcome, Guest")
	security = 1
else:
	print("\nSorry, the login information you provided is not valid")
	input("Press enter to disconnect")

input("\nThis is the end of this script. \nPress enter to close")
