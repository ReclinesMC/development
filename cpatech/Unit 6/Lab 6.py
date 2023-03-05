# Sean A
# Student Directory and logins
# Make the student directory work with files along with allowing the admin user to modify other users
import FileTools as ft
import time as t
import os as s

studentDirectory = {}
errorDelay = 1.5


def formatStudentDirectory(directoryFile):
	directory = ft.handleFile(directoryFile, "parse")
	if directory:
		global studentDirectory
		for i in directory:
			i = i.split(",")
			try:
				user = int(i[0])
				studentDirectory[user] = []
				i.pop(0)
				for info in i:
					info = info.strip()
					studentDirectory[user].append(info)
			except:
				print("Corrupt data!")
				return False
	return True


def login():
	print("[ Student Directory ]".center(50, "="))
	print(">> Login")
	try:
		userID = int(input("Enter your ID: "))

	except:
		print("You must enter a valid ID!")
		t.sleep(errorDelay)
		s.system("clear")
		return login()

	password = input("Enter your password: ")

	if validateLogin(userID, password):
		return userID

	else:
		print("Invalid Login!")
		t.sleep(errorDelay)
		s.system("clear")
		return login()


def validateLogin(username, password):
	if username in studentDirectory and studentDirectory[username][0] == password:
		return True

	else:
		return False


def userMenu(userID, studentInfo):
	admins = ["ADMIN"]
	if studentInfo[1] in admins:
		s.system("clear")
		print("[ Admin GUI ]".center(50, "="))
		print(f"Welcome {studentInfo[1]}!")
		print("What would you like to do?")
		print("1 - View Student Information")
		print("2 - Create a New Student")
		choice = input("Choose an option >> ")

		if choice == "1":
			try:
				studentID = int(input("Student ID:  "))

			except:
				print("Invalid Student ID!")
				t.sleep(errorDelay)
				userMenu(userID, studentInfo)

			if studentID in studentDirectory and studentInfo[1] not in admins:
				getStudentInfo(studentID, studentInfo)

			else:
				print("That is not a valid student!")
				t.sleep(errorDelay)
				userMenu(userID, studentInfo)

		elif choice == "2":
			createStudent()

		else:
			print("Invalid Choice!")
			t.sleep(errorDelay)


def getStudentInfo(studentID, studentInfo):
	s.system("clear")
	print("[ Student Information ]".center(50, "="))
	print(f'\nFull Name: {studentInfo[0]} {studentInfo[1]} {studentInfo[2]}')
	print(f"Student ID: {studentID}")
	print(f"DOB: {studentInfo[3]}")
	print(f"Grade: {studentInfo[4]}")
	print(f"GPA: {studentInfo[5]}\n")


def createStudent():
	pass


def writeOutStudentInfo():
	outputFile = "StudentDirectory"
	contents = ""
	for i in studentDirectory:
		contents += f"{str(i)}, "
		contents += ', '.join(studentDirectory[i])
		contents += "\n"
	ft.handleFile(outputFile, "create", contents)
	print(contents)


def main():
	directoryFile = "StudentDirectory"
	formatted = formatStudentDirectory(directoryFile)
	if formatted:
		userID = login()
		studentInfo = studentDirectory[userID]
		userMenu(userID, studentInfo)
		writeOutStudentInfo()


if __name__ == "__main__":
	main()
