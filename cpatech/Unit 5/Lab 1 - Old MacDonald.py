# Sean A
# Old MacDonald
# Using functions, sing the old MacDonald song

import time as t


def sing(animal, sound, delay):
    print("Old MAcDonald had a farm")
    t.sleep(delay)
    print("EE I EEE I OOO")
    t.sleep(delay)
    print(f"And on his farm he had some {animal}")
    t.sleep(delay)
    print("EE I EEE I OOOO")
    t.sleep(delay)
    print(f"With a {sound} {sound} here")
    t.sleep(delay)
    print(f"And a {sound} {sound} there")
    t.sleep(delay)
    print(f"Here a {sound}, there a {sound}")
    t.sleep(delay)
    print(f"Everywhere a {sound} {sound}")
    t.sleep(delay)
    print("Old MAcDonald had a farm")
    t.sleep(delay)
    print("EE I EEE I OOO")
    t.sleep(delay)


animals = {
    "cows": "moo",
    "chicks": "cluck",
    "pigs": "oink",
    "sheep": "baa",
    "horses": "neigh"
}

delay = 0.8

for i in animals:
    animal = i
    sound = animals[i]
    sing(animal, sound, delay)
