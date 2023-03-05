# Sean A
# Create a read function
# Using the new operators we have learned, create a function that allows reading a file
import re
import os as s


def validateFileName(fileName):
	regex = re.match(r".*\.txt", fileName)
	if regex:
		if s.path.isfile(fileName):
			return True
		else:
			print("File does not exist")
			return False
	else:
		print("Invalid file name")
		return False


def readFile(fileName, task):
	if validateFileName(fileName):

		if task == "read":
			try:
				with open(fileName, 'r') as openFile:
					return openFile.read()
			except:
				return None
		elif task == "parse":
			try:
				with open(fileName, 'r') as openFile:
					return openFile.readlines()
			except:
				return None
		else:
			print("Invalid Task")
			return False
	else:
		return False


def main():
	testNum = int(input("Which test would u like to use?"))

	if testNum == 1:  # Test 1
		task = "abc"
		fileName = "Dracula.txt"

	elif testNum == 2:  # Test 2
		task = "read"
		fileName = "balahsduhsdibu"

	elif testNum == 3:  # Test 3
		task = "parse"
		fileName = "The_Raven.txt"

	elif testNum == 4:  # Test 4
		task = "read"
		fileName = "A_Modest_Proposal.txt"

	elif testNum == 5:  # Test 5 (custom)
		task = input("What task?")
		fileName = input("Which file?")

	file = readFile(fileName, task)
	if file:
		print(file)


if __name__ == "__main__":
	main()