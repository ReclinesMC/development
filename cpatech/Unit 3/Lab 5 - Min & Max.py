# Sean A
# Determine integer sizes
# Using the two numbers the user has given, determine which number is bigger than the other


numInput = int(input("Enter the first number you would like to compare:"))
numInput2 = int(input("Enter the first number you would like to compare:"))

if numInput > numInput2:
  print("{} is larger than {}!".format(numInput, numInput2))
else:
  print("{} is smaller than {}!".format(numInput, numInput2))