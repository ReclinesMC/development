# Sean A
# Student Directory and logins
# Make the student directory work with files along with allowing the admin user to modify other users
import FileTools as ft
import time as t
import os as s

studentDirectory = {}
delay = 1.5


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
				return True
			except:
				print("Corrupt data!")
				return False


def login():
	print("[ Student Directory ]".center(50, "="))
	print(">> Login")
	try:
		userID = int(input("Enter your ID: "))
	except:
		print("You must enter a valid ID!")
		t.sleep(delay)
		s.system("clear")
		login()
	password = input("Enter your password: ")
	if validateLogin(userID, password):
		return userID
	else:
		print("Invalid Login!")
		t.sleep(delay)
		s.system("clear")
		login()


def validateLogin(username, password):
	try:
		studentDirectory[username]
	except:
		return False
	if studentDirectory[username][0] == password:
		return True
	else:
		return False


def userMenu(userID):
	admins = ["ADMIN"]
	if studentDirectory[userID][1] in admins:
		s.system("clear")
		print("[ Admin GUI ]".center(50, "="))
		print(f"Welcome {studentDirectory[userID][1]}!")
		print("What would you like to do?")
		print("1 - View Student Information")
		print("2 - Create a New Student")
		choice = input("Choose an option >> ")

		if choice == "1":
			try:
				studentID = int(input("Student ID:  "))
			except:
				print("Invalid Student ID!")
				t.sleep(delay)
				userMenu(userID)
			if studentID in studentDirectory:
				getStudentInfo(studentID)
			else:
				print("Invalid Student!")
				t.sleep(delay)
				userMenu(userID)
		elif choice == "2":
			createStudent()

		else:
			print("Invalid Choice!")
			t.sleep(delay)


def getStudentInfo(studentID):
	s.system("clear")
	print("[ Student Information ]".center(50, "="))
	print(f'\nFull Name: {studentDirectory[studentID][0]} {studentDirectory[studentID][1]} {studentDirectory[studentID][2]}')
	print(f"Student ID: {studentID}")
	print(f"DOB: {studentDirectory[studentID][3]}")
	print(f"Grade: {studentDirectory[studentID][4]}")
	print(f"GPA: {studentDirectory[studentID][5]}\n")


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
		userMenu(userID)
		writeOutStudentInfo()


if __name__ == "__main__":
	main()
