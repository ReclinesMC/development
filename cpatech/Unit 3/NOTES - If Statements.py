# Example 1
x = "Hello"

if x == "Hello":
	print(x + "world!")

# Example 2
x = "Python"

if x == "Hello":
	print(x + " 5world!")

# Example 3
myList = [2, "Hello", 40.5, "Python"]

if "Python" in myList:
	print("Python was found")

# Example 4
num = input("Enter an integer:")

if type(num) == int:
	print("Nice integer!")

# Example 5
num = input("Enter a single digit:")

if 48 <= ord(num) <= 57:
	print("Nice integer!")
