# Example 11

sym = 'a'

if 65 <= ord(sym) <= 90:
	print("{} is a capital letter".format(sym))
elif 97 <= ord(sym) <= 122:
	print("{} is a lowercase letter".format(sym))
else:
	print("{} is a symbol").format(sym)

# Example 12
vowels = ['a', 'e', 'i', 'o']

if 'a' not in vowels:
	print("The list is missing a")
elif 'e' not in vowels:
	print("The list is missing e")
elif 'i' not in vowels:
	print("The list is missing i")
elif 'o' not in vowels:
	print("The list is missing o")
else:
	print("The list is missing u")

# Example 13
vowels = []

if 'a' not in vowels:
	print("The list is missing a")
elif 'e' not in vowels:
	print("The list is missing e")
elif 'i' not in vowels:
	print("The list is missing i")
elif 'o' not in vowels:
	print("The list is missing o")
else:
	print("The list is missing u")

# Example 14
vowels = []

if 'a' not in vowels:
	print("The list is missing a")
if 'e' not in vowels:
	print("The list is missing e")
if 'i' not in vowels:
	print("The list is missing i")
if 'o' not in vowels:
	print("The list is missing o")
else:
	print("The list is missing u")

# Example 15 - Nested if-statements
num = input("Enter a single digit:")

if len(num) == 0:  # len() returns number of items in an object
	print("You must insert a value")

elif len(num) == 1:
	if 48 <= ord(num) <= 57:
		num = int(num)
		print("The sum of {} and 5 is {}".format(num, num + 5))

else:
	print("Your number is too large")
