# Sean A
# User Login
# Make a program using if statements to allow a user to login to their accoount with a username

users = ["popcornLVR84", "thegr33nMILE", "ceruleanfroggo123", "sunpioneer", "lightningSTORM"]

usernameInput = input("What is your username?:")

if usernameInput in users:
    print()
    print("[ Python ]".center(50, "="))
    print()
    print("Welcome to Python {}!".format(usernameInput).center(50))
    print()
    print("[  ]".center(50, "="))
