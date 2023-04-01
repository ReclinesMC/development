# Example 6
x = "Hello"

if x == "Hello":
    print(x + " world!")

else:
    print("Hmmmmmmmm...")

# Example 7
x = "Python"

if x == "Hello":
    print(x + " world!")

else:
    print("Hmmmmmmmm...")

# Example 8
num = input("Enter a single digit:")

if 48 <= ord(num) <= 57:
    print("Nice integer!")

else:
    print("What is this?")

# Example 9
num = 21

if num % 2 == 0:
    print("{} is an even number".format(num))

else:
    print("{} is an odd number".format(num))

# Example 10
myList = ['a', 'b', 'c', 'd']

if 'e' in myList:
    print("e is is in the list")

else:
    myList.append('e')
    print("e was added to the list")
    print(myList)
