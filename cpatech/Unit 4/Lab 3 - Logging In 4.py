# Sean A
# Logging into a program
# Using the usernames and password given, create a login program that has a limited number of attempts
import os

users = {
    "popcornLVR84": "Butt3rS@uce",
    "thegr33nMILE": "1luvtr33$",
    "ceruleanfroggo123": "r1bb1t",
    "sunpioneer": "W1ldW3$t",
    "lightningSTORM": "thund3r123",
    #  "a": "a"
}

user = input("Please enter your username:")
passes = 3
while user not in users:
    print("Username incorrect!")
    user = input("\nPlease enter your username:")

pw = input("Please enter your password:")
while pw != users[user] and passes > 1:
    print("Wrong password!")
    passes -= 1
    print("\nYou have {} attempt(s) remaining".format(passes))
    pw = input("Please enter your password:")

if passes == 0 or pw != users[user]:
    print("You ran out of attempts. Exiting...")
else:
    os.system("clear")
    print("Welcome {}!".format(user))
    if user == "a":
        print("Quick Access user, not to be used in production!")
