# Sean A
# Student Login
# Allow for a student to login using their ID and password


studentDirectory = {
    2345589: ["Le@fyGr33ns", "Willow", "Ivy", "Park", "3/21/2007", 10, 4.2],
    4017830: ["Illus1onsRmyJ@m", "Augustus", "James", "Porter", "10/4/2009", 9, 3.78],
    6120173: ["Chaot1cAb0mination$", "Amity", "Marie", "Blight", "11/19/2007", 10, 4.4],
    7202742: ["Azur@Fan", "Luz", "Rosa", "Noceda", "6/13/2007", 10, 3.4]
}

try:
    studentID = int(input("Student ID:"))
    pw = input("Password:")
    print()

    if studentID in studentDirectory:
        if pw == studentDirectory[studentID][0]:
            print("[ Student Information ]".center(50, "="))
            print("\nFull Name: {} {} {}".format(studentDirectory[studentID][1], studentDirectory[studentID][2],
                                                 studentDirectory[studentID][3]))
            print("Student ID: {}".format(studentID))
            print("DOB: {}".format(studentDirectory[studentID][4]))
            print("Grade: {}".format(studentDirectory[studentID][5]))
            print("GPA: {}\n".format(studentDirectory[studentID][6]))
            print("".center(50, "="))
        else:
            print("Invalid Student ID or password")
    else:
        print("Invalid Student ID or password")
except:
    print("\nStudent ID is invalid")
