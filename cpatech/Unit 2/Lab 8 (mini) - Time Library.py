# Sean A
# Working with the time library
# Use the time library to get and print information about the current state of time

from time import localtime

timeInfo = localtime()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday = weekdays[timeInfo[6]]

print("Today's date: {}/{}/{}".format(timeInfo[1], timeInfo[2], timeInfo[0]))
print("Weekday: {}\n".format(weekday))
print("Current time: {}:{}:{}".format(timeInfo[3], timeInfo[4], timeInfo[5]))
