# Sean A
# Milk bottle counter
# Count down bottles of milk from 99 to 0

for bottles in range(99, -1, -1):
  if bottles != 1 and bottles != 99:
    print(f"{bottles} bottles of milk!\n")
  elif bottles == 1:
    print(f"{bottles} bottle of milk!\n")
  if bottles > 1:
    print(f"{bottles} bottles of milk on the wall,")
    print(f"{bottles} bottles of milk.")
    print("Take one down, pass it around,")
  elif bottles == 1:
    print(f"{bottles} bottle of milk on the wall,")
    print(f"{bottles} bottle of milk.")
    print("Take one down, pass it around,")
