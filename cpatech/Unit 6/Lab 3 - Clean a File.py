# Sean A
# File Cleaner
# Take in a file and clean it of all special characters
import FileTools as fh

fileName = "christmas"
cleanFile = "cleansed"


def fileCleaner(unClean):
    clean = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for text in unClean:
        if text.lower() in alphabet:
            clean += text.lower()
        elif text == "\n" and clean[-1] != " ":
            clean += " "

    return clean


def main():
    unClean = fh.handleFile(fileName, "read")
    if unClean:
        cleanText = fileCleaner(unClean)
        fh.handleFile(cleanFile, "write", cleanText)

        print(f"{fileName} has been cleaned and outputted into cleansed.txt")


if __name__ == "__main__":
    main()
