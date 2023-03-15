# Sean A
# Converting messed up student info into a list
# The student directory was messed up and converted into a string, I need to convert it back


# student ID, first, middle, last, birthday, grade level, GPA
studentInfo = "2345589,.-+Willow,.-+Ivy,.-+Park,.-+3/21/2007,.-+10,.-+4.2"

# Fixing the "list"
studentInfo = studentInfo.split(',.-+')

# Printing Student Info
print("[ Student Information ]".center(50, "="))

print("\nFull Name: {} {} {}".format(studentInfo[1], studentInfo[2], studentInfo[3]))
print("Student ID: {}".format(studentInfo[0]))
print("DOB: {}".format(studentInfo[4]))
print("Grade: {}".format(studentInfo[5]))
print("GPA: {}\n".format(studentInfo[6]))
print("".center(50, "="))
