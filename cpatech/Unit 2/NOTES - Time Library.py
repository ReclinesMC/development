# Sean A
# Working with the Time Library
# Import and use the time library to study how libraries work and how to use them

import time

print("The .time() function")
start = time.time()
print(start)

print("\nThe .localtime() function")
today = time.localtime()
print(today)

print("\nThe .sleep() function")
print("Hello!")
time.sleep(5)
print("World!")

end = time.time()
print("\nYour program ran for {} seconds".format(end-start))