# Sean A
# Text Cleaner
# Make a program to clean up messy text

def textCleaner(unClean):
    unClean = list(unClean)
    for text in range(len(unClean)):
        ascii = ord(unClean[text])
        if ascii >= 0 and ascii <= 64 and ascii != 32:
            unClean[text] = ""
        elif ascii >= 91 and ascii <= 96:
            unClean[text] = ""
        elif ascii >= 123:
            unClean[text] = ""
    clean = "".join(unClean).lower()
    return clean


unClean = input("Please enter the text you would like to be cleansed:")
clean = textCleaner(unClean)

print("\nYour cleansed text is: {}".format(clean))
