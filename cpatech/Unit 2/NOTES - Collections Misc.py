aSet = {3, 6, 12, "hello", 'x'}
aList = ["purple", "apple", 34, 6]
aTuple = (3, 6, 1)
aDict = {"name": "Jane", "apple": "green", "cost": 15, 2: 100}

print(aSet)
print(aList)
print(aTuple)
print(aDict)
print()

print(len(aSet))
print(len(aList))
print(len(aTuple))
print(len(aDict))
print()

print('x' in aSet)
print(10 in aList)
print(6 in aTuple)
print("name" in aDict)
print("Jane" in aDict)
print()

del aList[3]
del aDict["name"]
del aTuple

print(aList)
# print(aTuple) # Comment to fix error
print(aDict)
