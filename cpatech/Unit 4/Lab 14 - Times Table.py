# Sean A
# Times Table
# Create a neat and clean times table

print("{ Multiplication Table }".center(48, "-"), end="")

for i in range(1, 13):
    print()
    for e in range(1, 13):
        print(str(i * e).rjust(3), end=" ")

print()
