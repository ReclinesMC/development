# Sean A
# Leap Year
# Using the year given determine if it is a leap year or just a normal year

print("Leap Year Calculator".center(50))
print()

try:
	year = int(input("Enter a year number:"))
	print()
	if year % 100 == 0 and not year % 400 == 0:
		print("{} is not a leap year".format(year))
	elif year % 4 == 0:
		print("{} is a leap year!".format(year))
	else:
		print("{} is not a leap year".format(year))
except:
	print("Please enter a valid year")
