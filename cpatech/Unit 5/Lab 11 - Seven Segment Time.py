# Sean A
# Seven Segment Time
# Create a clock using the sevseg library

import os as s
import time as t

from sevseg import getSevSegStr as sev


def getTimeOffSet():
    invalidInput = True
    while invalidInput:
        try:
            hour = t.strftime("%H")
            min = t.strftime("%M")
            print(f"The current time in UTC is: {hour:02}:{min:02}")
            offset = int(input("By how many hours would you like to offset the clock?"))
            invalidInput = False
            return offset
        except:
            s.system("clear")
            print("Invalid input! Must be a positive or negative integer.")
            continue


def clock(offset):
    ticking = True
    while ticking:
        s.system("clear")
        hours = str(abs((int(t.strftime("%H")) + offset) % 24)).zfill(2)
        minutes = str(t.strftime("%M")).zfill(2)
        seconds = str(t.strftime("%S")).zfill(2)
        print(sev(hours + ":" + minutes + ":" + seconds))
        t.sleep(1)


def main():
    timeOffSet = getTimeOffSet()
    clock(timeOffSet)


if __name__ == "__main__":
    main()
