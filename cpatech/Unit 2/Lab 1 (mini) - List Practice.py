# Sean A
# List Practice
# Creating and Editing lists to practice creating, modifying, and editing lists.

# Creating a List
listA = []
listB = ["Orange", "Yellow", "Green"]

# Adding to A
# 3 lines
listA.append("Siamese")
listA.insert(0, "Coon")
listA.extend(["Shorthair", "Chartreux", "Munchkin"])

# Adding to B
# 2 lines
listB.extend(["Blue", "Indigo", "Violet", "White", "Black"])
listB.insert(0, "Red")

# Displaying the list
print(listA)
print()
print(listB)
print()

# Sorting the list
listA.sort()
listB.sort()

# Displaying the list
print(listA)
print()
print(listB)
print()

# Inserting Hello World
listB.insert(3, "hello world")

# Displaying Index 5
print(listA[4])
print()

# Replacing with "pumpkin pie"
listB[0] = "pumpkin pie"

# Displaying the list
print(listA)
print()
print(listB)
