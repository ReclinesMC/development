myList = ["Hello", "taco", "kitten", "rabbit", "mouse"]

print("***WITHOUT***")
print(myList)
print(type(myList))

print("\n***WITH***")
print(','.join(myList))
print(type(myList))
print(type(','.join(myList)))
print('**'.join(myList))
print('~'.join(myList))