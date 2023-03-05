# Sean A
# Student Directory and logins
# Make the student directory work with files along with allowing the admin user to modify other users
import FileTools as ft
import time as t
import os as s

studentDirectory = {}


def sleep():
	t.sleep(1.5)


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


# noinspection PyStatementEffect
def login():
	print("[ Student Directory ]".center(50, "="))
	print(">> Login")
	try:
		userID = int(input("Enter your ID: "))

	except:
		print("You must enter a valid ID!")
		sleep()
		s.system("clear")
		return login()

	password = input("Enter your password: ")

	if validateLogin(userID, password):
		return userID

	else:
		print("Invalid Login!")
		sleep()
		s.system("clear")
		return login()


def validateLogin(username, password):
	if username in studentDirectory and studentDirectory[username][0] == password:
		return True

	else:
		return False


def userMenu(userID):
	studentInfo = studentDirectory[userID]
	admins = ["ADMIN"]

	if studentInfo[1] in admins:
		admin = userID
		s.system("clear")
		print("[ Admin GUI ]".center(50, "="))
		print(f"Welcome {studentInfo[1]}!")
		print("What would you like to do?")
		print("1 - View Student Information")
		print("2 - Create a New Student")
		print("3 - Exit")
		choice = input("Choose an option >> ")

		if choice == "1":
			try:
				studentID = int(input("Student ID:  "))

			except:
				print("Invalid Student ID!")
				sleep()
				return userMenu(userID)

			if studentID in studentDirectory and studentDirectory[studentID][1] not in admins:
				return getStudentInfo(studentID, admin)

			else:
				print("That is not a valid student!")
				sleep()
				return userMenu(userID)

		elif choice == "2":
			createStudent(admin)

		elif choice == "3":
			print("Goodbye!")
			sleep()
			s.system("clear")
			return True
		else:
			print("Invalid Choice!")
			sleep()
			return userMenu(userID)
	else:
		return getStudentInfo(userID)


def getStudentInfo(studentID, adminID=0):
	studentInfo = studentDirectory[studentID]
	s.system("clear")
	print("[ Student Information ]".center(50, "="))
	print(f'\nFull Name: {studentInfo[1]} {studentInfo[2]} {studentInfo[3]}')
	print(f"Student ID: {studentID}")
	print(f"DOB: {studentInfo[4]}")
	print(f"Grade: {studentInfo[5]}")
	print(f"GPA: {studentInfo[6]}\n")
	if adminID != 0:
		input("Press enter to return to the admin menu...")
		return userMenu(adminID)


def createStudent(adminID):
	s.system("clear")
	print("[ Student Creator ]".center(50, "="))
	print("Enter the following information:")
	try:
		studentID = int(input("Student ID: "))
	except:
		print("Invalid student ID!")
		# noinspection PyStatementEffect
		sleep()
		return createStudent(adminID)

	# I really need to start commenting my code better
	if studentID in studentDirectory:
		print("That student ID is already in use!")
		sleep()
		return createStudent(adminID)

	elif len(str(studentID)) != 7:
		print("Student ID must be 7 digits!")
		sleep()
		return createStudent(adminID)

	firstName = input("First Name: ")
	middleName = input("Middle Name: ")
	lastName = input("Last Name: ")
	dob = input("Date of Birth (MM/DD/YYYY): ")
	try:
		grade = int(input("Grade: "))
	except:
		print("Grade must be a number!")
		sleep()
		return createStudent(adminID)

	gpa = input("GPA: ")
	password = input("Password: ")
	studentDirectory[studentID] = [password, firstName, lastName, middleName, dob, str(grade), gpa]
	print("Please review the information above.")
	input("Press enter to continue...")
	print("Student created!")
	sleep()
	return userMenu(adminID)


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
		studentDirectory[userID]
		userMenu(userID)
		writeOutStudentInfo()


if __name__ == "__main__":
	main()
