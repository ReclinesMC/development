# Sean A
# Unit 6 Project
# Make a program to read, clean, and leetspeak a file
import random as r
import FileTools as ft
import time as t

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


if __name__ == "__main__":
	fileName = "EndGame"
	outputFile = f"{fileName}_leet"

	print("[ Leetspeak Converter ]".center(50, "="))
	print(f"Cleaning {fileName}.txt...")
	boringText = ft.handleFile(fileName, "clean")
	t.sleep(0.5)

	print("Converting to leetspeak...")
	leetText = leetConverter(boringText)
	t.sleep(0.5)

	print(f"Writing to {outputFile}.txt...")
	ft.handleFile(outputFile, "create", leetText)
	t.sleep(0.5)

	print(f"\nSuccess! {fileName} has been converted to leetspeak!")
