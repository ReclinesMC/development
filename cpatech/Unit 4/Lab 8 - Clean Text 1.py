# Sean A
# Text Cleaner
# Make a program to clean up messy text

unClean = input("Please enter the text you would like to be cleansed:")
unClean = list(unClean)

for text in range(len(unClean)):
	ascii = ord(unClean[text])
	if ascii >= 0 and ascii <= 64 and ascii != 32:
		unClean[text] = ""
	elif ascii >= 91 and ascii <= 96:
		unClean[text] = ""
	elif ascii >= 123:
		unClean[text] = ""

unClean = "".join(unClean).lower()
print("\nYour cleansed text is: {}".format(unClean))