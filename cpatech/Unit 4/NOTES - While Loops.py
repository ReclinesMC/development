# Example 3
studentDirectory = {
	2345589: ["Willow", "Ivy", "Park", "3/21/2007", 10, 4.2],
	4017830: ["Augustus", "James", "Porter", "10/4/2009", 9, 3.78],
	6120173: ["Amity", "Marie", "Blight", "11/19/2007", 10, 4.4],
	7202742: ["Luz", "Rosa", "Noceda", "6/13/2007", 10, 3.4]
}

ID = int(input("Enter your student ID:"))

while ID not in studentDirectory:
	print("\nUnrecognized ID")
	ID = int(input("Please enter a valid student ID:"))

print("Welcome", studentDirectory[ID][0], ":)")