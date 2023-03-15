# Sean A
# Text Reverser
# Take in a string as an input and reverse it and print it back to the user

reverse = input("Enter the text you would like to reverse:")
print("\nYour reversed text is: ", end="")

for back in range(len(reverse) - 1, -1, -1):
	print(reverse[back], end="")

print(f"\n\nThe original text was: {reverse}")
