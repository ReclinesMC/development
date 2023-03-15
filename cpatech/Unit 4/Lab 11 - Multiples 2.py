# Sean A
# Number Factors
# Get the factors of a number

numbers = []

number = input("Please enter a positive number to get the factors of:")
try:
	number = int(number)
except:
	print("You must enter a valid integer")

while type(number) != int:
	try:
		number = input("Please enter a positive number to get the factors of:")
		number = int(number)
	except:
		print("Your number must be a valid integer")

if number > 10000000:
	print("\nPlease wait...")

for i in range(number, 0, -1):
	if number % i == 0:
		numbers.append(str(i))

if number != 0 and number > 0:
	print(f"The factor(s) of {number} are: {', '.join(numbers)}")
elif number == 0:
	print("Every number is a factor of 0.")
else:
	print("You must enter a valid, positive integer")
