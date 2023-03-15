# Sean A
# Login program
# Make a program that allows a user to login only if they have a valid username and password

users = {
	"popcornLVR84": "Butt3rS@uce",
	"thegr33nMILE": "1luvtr33$",
	"ceruleanfroggo123": "r1bb1t",
	"sunpioneer": "W1ldW3$t",
	"lightningSTORM": "thund3r123"
}

print("User authentication is required")
user = input("Username:")
pw = input("Password:")
print()

if user in users:
	if pw == users[user]:
		print("Success!")
		print("[ Rasberry Pi OS ]".center(50, "="))
		print()
		print("Welcome {}!".format(user).center(50))
		print()
		print("[ ]".center(50, "="))
	else:
		print("Invalid username or password")
else:
	print("Invalid username or password")
