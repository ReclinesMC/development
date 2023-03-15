# Sean A
# Student Info Program
# Work with dictionaries to create a new student and output its information


studentDirectory = {
	2345589: ["Willow", "Ivy", "Park", "3/21/2007", 10, 4.2],
	4017830: ["Augustus", "James", "Porter", "10/4/2009", 9, 3.78],
	6120173: ["Amity", "Marie", "Blight", "11/19/2007", 10, 4.4],
	7202742: ["Luz", "Rosa", "Noceda", "6/13/2007", 10, 3.4]
}

# Student Registration
print("< Student Registration >".center(50, "~"))
studentID = int(input("\nPlease enter the student ID (7 digits):"))
studentFirst = input("Student First Name:")
studentMid = input("Student Middle Name:")
studentLast = input("Student Last Name:")
studentDOB = input("Student DOB (m/d/yyyy):")

studentGrade = int(input("Student grade level:"))
studentGPA = float(input("Student GPA:"))
print()

print("< >".center(50, "~"))
newStudentInfo = {studentID: [studentFirst, studentMid, studentLast, studentDOB, studentGrade, studentGPA]}
studentDirectory.update(newStudentInfo)

# Grabbing ID
print("{ Student Directory }".center(50, "-"))
studentID = int(input("\nWhat is your student ID?:"))
print()
print("{  }".center(50, "-"))

# Printing Student Info
print("[ Student Information ]".center(50, "="))
print("\nFull Name: {} {} {}".format(studentDirectory[studentID][0], studentDirectory[studentID][1],
                                     studentDirectory[studentID][2]))
print("Student ID: {}".format(studentID))
print("DOB: {}".format(studentDirectory[studentID][3]))
print("Grade: {}".format(studentDirectory[studentID][4]))
print("GPA: {}\n".format(studentDirectory[studentID][5]))
print("".center(50, "="))
