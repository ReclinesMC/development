# Sean A
# Finding the multiples of a number
# Use if and else statements to get the multiples of a number ad display them to the user

multiples = []

print("Welcome! Enter a number below to determine its multiples")
numInput = int(input("\nEnter your number here:"))

if numInput % 1 == 0:
	multiples.append("1")
if numInput % 2 == 0:
	multiples.append("2")
if numInput % 3 == 0:
	multiples.append("3")
if numInput % 4 == 0:
	multiples.append("4")
if numInput % 5 == 0:
	multiples.append("5")
if numInput % 6 == 0:
	multiples.append("6")
if numInput % 7 == 0:
	multiples.append("7")
if numInput % 8 == 0:
	multiples.append("8")
if numInput % 9 == 0:
	multiples.append("9")

print()
print("{} has the following multiples: {} ".format(numInput, ", ".join(multiples)))

