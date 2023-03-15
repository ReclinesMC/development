# Sean A
# Date Correction tool
# When a user enters a date, this program will correct it to be used
# mm/dd/yy


userBday = input("Please enter your birthday here:")
originBday = userBday.split('/')
bdaySplit = userBday.split('/')

if len(bdaySplit[0]) != 2:
	bdaySplit[0] = "0" + bdaySplit[0]
if len(bdaySplit[1]) != 2:
	bdaySplit[1] = "0" + bdaySplit[1]
if len(bdaySplit[2]) != 4:
	if int(bdaySplit[2]) >= 10 and int(bdaySplit[2]) <= 30:
		bdaySplit[2] = "20" + bdaySplit[2]
	elif int(bdaySplit[2]) >= 31 and int(bdaySplit[2]) <= 99:
		bdaySplit[2] = "19" + bdaySplit[2]
	elif int(bdaySplit[2]) >= 0 and int(bdaySplit[2]) <= 9:
		bdaySplit[2] = "200" + bdaySplit[2]

userBday = "{}/{}/{}".format(bdaySplit[0], bdaySplit[1], bdaySplit[2])
if len(originBday[0]) != 2 or len(originBday[1]) != 2 or len(originBday[2]) != 4:
	print("\nYour birthday was been corrected to: {}".format(userBday))
	print("It will now be stored in our records.")
else:
	print("\n{} will be stored in our records.".format(userBday))
