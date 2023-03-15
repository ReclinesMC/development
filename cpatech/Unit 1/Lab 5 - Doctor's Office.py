# Sean A
# Patient Tracking System
# Make a system to log patient information for the nurses and doctors to use.
import os

# Asking for the inputs
firstName = input("First Name:")
midName = input("Middle Name:")
lastName = input("Last Name:")
gender = input("Gender (M/F):")
height = input("Height in inches and feet (ex. 5'7):")
weight = input("Weight in pounds:")
allergies = input("Allergies (Seperated by commas):")
addressFirst = input("First address line:")
addressSecond = input("Second address line:")

# Printing the outputs
os.system('clear')
print("Patient Info".center(50))
print("".center(50, '*'))
print("Full Name: {} {} {}".format(firstName, midName, lastName) + "\n")
print("Height: {}".format(height) + "Weight: {}".rjust(15, ' ').format(weight))
print("Gender: {}".format(gender) + "\n")
print("Allergies: {}".format(allergies) + "\n")
print("Address: \n {} \n {}".format(addressFirst, addressSecond))

print("".center(50, '*'))
