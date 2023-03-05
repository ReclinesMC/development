fruitDict = {"apple":"red", "orange":"orange", "banana":"yellow"}
otherDict = {}

print(fruitDict)
print(otherDict)
print()

print(fruitDict["apple"])
print(fruitDict.get("banana"))
print()

fruitDict["grapes"] = "purple"
fruitDict.update({"kiwi":"green"})

print(fruitDict)
print()

fruitDict.pop("orange")
fruitDict.popitem()
del fruitDict["apple"]

print(fruitDict)
print()

print(fruitDict.keys())
print(fruitDict.values())