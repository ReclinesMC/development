# Sean
# Word Finder
# Using the new clean function I hath made, make a function to find a word in a file
import FileTools as ft


def findText(text, word):
    text = text.split()
    count = 0
    for i in text:
        if word == i:
            count += 1
    if word == " " and len(text) != 0:
        count = len(text) - 1
    return count


def main():
    fileName = input("Which file would you like to search?")
    if fileName == "":
        fileName = "Test_Case.txt"
    text = ft.handleFile(fileName, "clean")
    if text:
        word = input(f"\nWhich word would you like to find in the file {fileName}?").lower()
        count = findText(text, word)
        if count == 1:
            print(f"\n\"{word}\" was found {count} time in {fileName}")
        else:
            print(f"\n\"{word}\" was found {count} times in {fileName}")
    else:
        main()


if __name__ == "__main__":
    main()
