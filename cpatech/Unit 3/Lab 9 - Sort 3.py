# Sean A
# Integer Sorting
# Sort three integers from greatest to least and then display them
from random import randint

# num1 = 13
# num2 = 9
# num3 = -19
num1 = randint(-90, 90)
num2 = randint(-90, 90)
num3 = randint(-90, 90)
print("Starting Numbers: \n{} {} {}".format(num1, num2, num3))

print("The numbers from greatest to least are:")
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("{} {} {}".format(num1, num2, num3))
    elif num3 >= num2:
        print("{} {} {}".format(num1, num3, num2))

elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("{} {} {}".format(num2, num1, num3))
    elif num3 >= num1:
        print("{} {} {}".format(num2, num3, num1))

elif num3 >= num1 and num3 >= num2:
    if num1 >= num2:
        print("{} {} {}".format(num3, num1, num2))
    elif num2 >= num1:
        print("{} {} {}".format(num3, num2, num1))
else:
    print("I'm not sure what numbers you put in, or how you managed to get here, but please report it to the devs.")
