# Sean A
# Student Information
# When the student enters their id, give them their information, but if it is an incorrect id give them an error
from time import sleep

studentDirectory = {
    2345589: ["Willow", "Ivy", "Park", "3/21/2007", 10, 4.2],
    4017830: ["Augustus", "James", "Porter", "10/4/2009", 9, 3.78],
    6120173: ["Amity", "Marie", "Blight", "11/19/2007", 10, 4.4],
    7202742: ["Luz", "Rosa", "Noceda", "6/13/2007", 10, 3.4]
}

print("{ Student Directory }".center(50, "-"))
studentID = int(input("\nWhat is your student ID?:"))
print(studentID)
print()
print("{  }".center(50, "-"))

if studentID not in studentDirectory and len(str(studentID)) == 7:
    # Student Registration
    print("\nIt seems this ID is not currently in the directory")
    print("Starting Student Registration process...")
    print()
    sleep(2)
    print("< Student Registration >".center(50, "~"))
    print("\nStudent Registration ID: {}".format(studentID))
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
elif studentID not in studentDirectory:
    print("\nError: Student ID must be 7 digits long and cannot start with a 0")
else:
    print("\nPlease report this error to the program author")

# Printing the Information
if len(str(studentID)) == 7 and studentID in studentDirectory:
    print("[ Student Information ]".center(50, "="))
    print("\nFull Name: {} {} {}".format(studentDirectory[studentID][0], studentDirectory[studentID][1],
                                         studentDirectory[studentID][2]))
    print("Student ID: {}".format(studentID))
    print("DOB: {}".format(studentDirectory[studentID][3]))
    print("Grade: {}".format(studentDirectory[studentID][4]))
    print("GPA: {}\n".format(studentDirectory[studentID][5]))
    print("".center(50, "="))
