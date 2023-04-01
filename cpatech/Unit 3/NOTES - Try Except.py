# Example 1
num1 = input("Enter an integer: ")
num2 = input("Enter another integer: ")

try:
    total = int(num1) + int(num2)
    print("{} + {} = {}".format(num1, num2, total))

except:
    print("One or more of your values is not an integer...")

# Example 2
studentDirectory = {
    2345589: ["Willow", "Ivy", "Park", "3/21/2007", 10, 4.2],
    4017830: ["Augustus", "James", "Porter", "10/4/2009", 9, 3.78],
    6120173: ["Amity", "Marie", "Blight", "11/19/2007", 10, 4.4],
    7202742: ["Luz", "Rosa", "Noceda", "6/13/2007", 10, 3.41],
}

id = input("Enter student ID: ")

try:
    id = int(id)
    info = studentDirectory[id]
    print("\nName: {} {} {}".format(info[0], info[1], info[2]))

except:
    print("\nInvalid student ID")
# Example 3
num = input("Enter a single digit: ")
try:
    if 48 <= ord(num) <= 57:
        print("Nice integer!")
    else:
        print("What is this???")

except:
    print("I asked for a SINGLE digit")
