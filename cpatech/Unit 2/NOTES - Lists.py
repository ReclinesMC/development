wordList = []
letterList = []
numberList = [22, 6, 34]

print(wordList)
print(letterList)
print(numberList)
print()


wordList.append("Hello")
wordList.append("World")
letterList.extend(['a', 'b', 'c', 'd'])
numberList.extend([4, 191])

print(wordList)
print(letterList)
print(numberList)
print()


wordList.insert(1, "Python")
letterList.insert(2, 'd')
numberList.insert(4, 99)

print(wordList)
print(letterList)
print(numberList)
print()


print(wordList[0])
print(letterList[1])
print(numberList[2:5])
print()


print(wordList[-1])
print(letterList[-3])
print(numberList[-5])
print()


wordList[0] = "Blue"
letterList[3] = "h"
numberList[2] = 153

print(wordList)
print(letterList)
print(numberList)
print()


wordList.remove("World")
del letterList[3]
del numberList[1:2]

print(wordList)
print(letterList)
print(numberList)
print()
