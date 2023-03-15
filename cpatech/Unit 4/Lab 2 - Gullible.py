# Sean A
# Keeping a gullible person busy
# Use a while loop to make a program that repeats a message until "no" is entered

answer = input("Want to know how to keep a gullible person busy? (y/n)").capitalize()

while answer != "No" and answer != "N":
	answer = input("\nWant to know how to keep a gullible person busy? (y/n)").capitalize()

print("\nOkay, Bye!")
