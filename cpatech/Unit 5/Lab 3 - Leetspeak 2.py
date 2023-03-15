# Sean A
# Leetspeak
# Turn normal chars into special chars from a user-inputted string
import random as r

print("[ Leetspeak Converter ]".center(50, "="))

charMap = {
	'a': ['4', '@', '/-\\'],
	'c': ['('],
	'd': ['|)'],
	'e': ['3'],
	'f': ["ph"],
	'h': ["]-[", "|-|"],
	'i': ['1', '!', '|'],
	'k': ["]<"],
	'o': ['0'],
	's': ['$', '5'],
	't': ['7', '+'],
	'u': ["|_|"],
	'v': ["\\/"]
}


def leetConverter(boringText):
	leetText = []
	for i in range(len(boringText)):
		if boringText[i].lower() in charMap:
			leetText.append(r.choice(charMap[boringText[i].lower()]))
		else:
			leetText.append(boringText[i])
	leetText = "".join(leetText)
	return leetText


boringText = input("Enter the text that you would like to convert into leetspeak:")
leetText = leetConverter(boringText)

print(f"\nYour leetspeak'd text is: {leetText}")
print(f"\nOriginal: {boringText} ")
