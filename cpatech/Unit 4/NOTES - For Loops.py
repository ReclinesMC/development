# Example 3
factOf = 10
f = 1

for num in range(factOf, 0, -1):
    f *= num

print(f"{factOf}! is {f}")

# Example 4
packlist = ["socks", "underwear", "pants", "shirts", "toothbrush", "toothpaste", "soap"]
suitcase = []

for item in packlist:
    suitcase.append(item)
    print("You just packed some", item)
print("\nYou have finished packing")
print("Your suitcase contains:", ', '.join(suitcase))
