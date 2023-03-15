wordSet = set({})
letterSet = set({})
numberSet = set({})
otherSet = {'x', 2, "hello world"}

print(wordSet)
print(letterSet)
print(numberSet)
print(otherSet)
print()

wordSet.add("Python")
letterSet.add('a')
numberSet.add(5)
otherSet.add(3.14159)

print(wordSet)
print(letterSet)
print(numberSet)
print(otherSet)
print()

wordSet.update(["mouse", "cat"])
letterSet.update("create")
numberSet.update([6, 7, 8, 9])
otherSet.update([1, "gold"])

print(wordSet)
print(letterSet)
print(numberSet)
print(otherSet)
print()

wordSet.remove("Python")
letterSet.discard('a')
numberSet.clear()
# otherSet.remove('z') #Comment out this line to remove the error

print(wordSet)
print(letterSet)
print(numberSet)
print(otherSet)
print()

A = {'a', 'b', 'c', '1', '2', '3'}
B = {'1', '2', '3', '4', '5', '6'}
C = {'a', 'b', 'c', 'd', 'e', 'f'}

AminusB = A.difference(B)
BminusA = B.difference(A)

BunionC = B.union(C)

CintersectA = C.intersection(A)

print(AminusB)
print(BminusA)
print(BunionC)
print(CintersectA)
