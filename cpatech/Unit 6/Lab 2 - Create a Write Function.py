# Sean A
# Create a write function
# Using the new operators we have learned, create a function that allows writing to a file
# Also we should not talk about the submission time of this project, I swear I was on task 🥲
import FileTools as fh


def main():
	delay = 3

	# while True:
	task = ""
	fileName = ""
	contents = None
	# s.system("clear")
	# print("1 - Invalid task, valid file")
	# print("2 - Valid task, invalid file")
	# print("3 - Parse \"The Raven\"")
	# print("4 - Read \"The Modest Proposal\"")
	# print("5 - Write a string")
	# print("6 - Write a list")
	# print("7 - Write an integer")
	# print("8 - Fix missing extension")
	# print("9 - Custom!")
	# print()

	# try:
	#   testNum = int(input("Which test would u like to use?"))
	# except:
	#   main()

	# if testNum > 9 and testNum < 1:
	#   main()

	testNum = 1
	while testNum < 9:
		print("-" * 40)
		print(f"\nTest #{testNum}\n")
		if testNum == 1:  # Test 1
			print("Task - \"abc\"")
			print("File - \"Dracula.txt\"")
			task = "abc"
			fileName = "Dracula.txt"

		elif testNum == 2:  # Test 2
			print("Task - \"read\"")
			print("File - \"balahsduhsdibu\"")
			task = "read"
			fileName = "balahsduhsdibu"

		elif testNum == 3:  # Test 3
			print("Task - \"parse\"")
			print("File - \"The_Raven.txt\"")
			task = "parse"
			fileName = "The_Raven.txt"

		elif testNum == 4:  # Test 4
			print("Task - \"read\"")
			print("File - \"A_notModest_Proposal.txt\"")
			task = "read"
			fileName = "A_notModest_Proposal.txt"

		elif testNum == 5:  # Test 5
			print("Task - \"write\"")
			print("File - \"test.txt\"")
			print("Contents - A string of text")
			task = "write"
			fileName = "test.txt"
			contents = "I like cheese!"

		elif testNum == 6:  # Test 6
			print("Task - \"write\"")
			print("File - \"a_b_c.txt\"")
			print("Contents - A list containg the alphabet")
			task = "write"
			fileName = "a_b_c.txt"
			contents = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "\nQ", "R", "S",
			            "T", "U", "V", "W", "X", "Y", "Z"]

		elif testNum == 7:  # Test 7
			print("Task - \"write\"")
			print("File - \"1_2_3.txt\"")
			print("Contents - An integer :)")
			task = "write"
			fileName = "1_2_3.txt"
			contents = 123

		elif testNum == 8:  # Test 8
			print("Task - \"write\"")
			print("File - \"test.t\"")
			print("Contents - A string of text")
			task = "write"
			fileName = "test.t"
			contents = "Now I LOVE cheese!"

		elif testNum == 9:  # Test 9 (custom)
			fh.main()
		if testNum != 9:
			print("\nResponse:")
			responded = fh.handleFile(fileName, task, contents)
			print()
			if responded:
				print("File output:")
				print(responded)
		testNum += 1


if __name__ == "__main__":
	main()
