# Sean A
# Grade Translator
# Translate a numerical grade into a letter grade using if statements

numGrade = float(input("What is your current grade?:"))
print()

if numGrade < 60 and numGrade >= 0:
	print("{} is an F, consider studying more :)".format(numGrade))
elif numGrade >= 60 and numGrade < 70:
	print("{} is a D, keep trying, you'll improve!".format(numGrade))
elif numGrade >= 70 and numGrade < 80:
	print("{} is a C, not bad!".format(numGrade))
elif numGrade >= 80 and numGrade < 90:
	print("{} is a B, great job!".format(numGrade))
elif numGrade >= 90 and numGrade <= 100:
	print("{} is an A, amazing work!".format(numGrade))
elif numGrade < 0:
	print("Your grade is below 0... must be cold down there!")
else:
	print("Wow! Your grade is above 100, you must be a magician!")
