# Sean A
# Dictionary Practice
# Practicing interactions with dictionaries to learn more about how they work

dictA = {}
dictB = {"Apple": "Red", "Banana": "Yellow"}

# Adding to A
# 3 lines
dictA["Dragon"] = "Purple"
dictA["Unicorn"] = "Rainbow"
dictA.update({"Werewolf": "Gray", "Yeti": "White", "Fairy": "Golden"})

# Adding to B
# 2 lines
dictB.update({"Blueberry": "Blue", "Orange": "Orange", "Pineapple": "Gold"})
dictB.update({"Watermelon": "Green", "Grape": "Purple", "Lime": "Lime"})

# Displaying
print(dictA)
print(dictB)
print()

# Changing B
dictB["Grape"] = "Light Green"

# Adding to B
dictB["hello world"] = "Python"

# Displaying Keys & Values
print(dictA.keys())
print(dictB.keys())
print()
print(dictA.values())
print(dictB.values())
print()

# Displaying
print(dictA)
print(dictB)
