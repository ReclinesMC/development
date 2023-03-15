# Sean A
# College Credit calssification
# Turn an amount of college credits into a grade level

numCredits = int(input("How many college credits do you have?"))
print()

if numCredits >= 0 and numCredits <= 6:
	print("You are currently a freshman. Good luck!")
elif numCredits >= 7 and numCredits <= 15:
	print("You are currently a Sophomore")
elif numCredits >= 16 and numCredits <= 25:
	print("You are currently a Junior")
elif numCredits >= 26:
	print("You are currently a Senior!")
else:
	print("How did you manage to get negative credits?!")
