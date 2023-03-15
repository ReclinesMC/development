# Sean A
# Student Information
# Refrencing dictionaries to grab student information to practice using dictionaries

studentInfo = {
	"ID": 4017830,
	"first": "Augustus",
	"middle": "James",
	"last": "Porter",
	"DOB": "10/4/2009",
	"Grade": 9,
	"GPA": 3.78
}

print("[ Student Information ]".center(50, "="))

print("\nFull Name: {} {} {}".format(studentInfo["first"], studentInfo["middle"], studentInfo["last"]))
print("Student ID: {}".format(studentInfo["ID"]))
print("DOB: {}".format(studentInfo["DOB"]))
print("Grade: {}".format(studentInfo["Grade"]))
print("GPA: {}\n".format(studentInfo["GPA"]))
print("".center(50, "="))
