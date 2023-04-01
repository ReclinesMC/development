# Sean A
# FileHandler
# This file's purpose is to handle a file name, and then read or write to that file.
# This was so painful to make 😭
import os as s
import re

verbose = True


def formatFileName(fileName):
    try:
        regex = re.match(r"([^ /\\:*?\"><|^&$@']+?)(|\.|\.t|\.tx|\.txt)$", fileName)
    except:
        print("File name must be a string!")
        return False, None
    if regex:

        if regex.group(2) == "":
            fileName += ".txt"
        elif regex.group(2) == ".":
            fileName += "txt"
        elif regex.group(2) == ".t":
            fileName += "xt"
        elif regex.group(2) == ".tx":
            fileName += "t"
        return True, fileName

    else:
        if verbose:
            print("Invalid File Name!")
        return False, None


def validateFileExists(fileName):
    if s.path.isfile(fileName):
        return True
    else:
        if verbose:
            print("File does not exist")
        return False


def readFile(fileName):
    with open(fileName, 'r') as openFile:
        return openFile.read()


# try:
# 	with open(fileName, 'r') as openFile:
# 		return openFile.read()
# except:
# 	print("An error occured while reading the file")
# 	return None


def parseFile(fileName):
    try:
        with open(fileName, 'r') as openFile:
            return openFile.readlines()
    except:
        print("An error occured while parsing the file")
        return None


def writeFile(fileName, contents):
    fileContents = ""
    if contents is not None:
        if isinstance(contents, int):
            contents = str(contents)
        elif isinstance(contents, float):
            contents = str(contents)
        try:
            with open(fileName, 'w') as openFile:
                for i in contents:
                    openFile.write(str(i))
                    fileContents += str(i)
                return fileContents
        except:
            if verbose:
                print("Invalid file contents")
            return None
    else:
        if verbose:
            print("Nothing was given to put into the file!")
        return None


def fileCleaner(unClean):
    if isinstance(unClean, int):
        unClean = str(unClean)
    elif isinstance(unClean, float):
        unClean = str(unClean)
    elif isinstance(unClean, list):
        unClean = ''.join(unClean)

    clean = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for text in unClean:
        if text.lower() in alphabet:
            clean += text.lower()
        elif text == " " and clean[-1] != " ":
            clean += " "
        elif text == "\n" and clean[-1] != " ":
            clean += " "
    return clean


def handleFile(fileName, task, contents=None, printData=False, validify=True):
    data = ""
    if validify:
        formatted, fileName = formatFileName(fileName)
    else:
        formatted = True

    if formatted:
        task = task.lower()
        if task == "read":
            if validateFileExists(fileName):
                data = readFile(fileName)

        elif task == "clean":
            if validateFileExists(fileName):
                unClean = readFile(fileName)
                data = fileCleaner(unClean)

        elif task == "parse":
            if validateFileExists(fileName):
                data = parseFile(fileName)

        elif task == "write":
            data = writeFile(fileName, contents)

        elif task == "create":
            data = writeFile(fileName, contents)

        elif task == "clean":
            contents = handleFile(fileName, "read")
            data = fileCleaner(contents)
        else:
            if verbose:
                print("Invalid Task")
            return False

        if printData:
            print(data)
        else:
            return data


def main():
    fileName = input("Choose a file name:")
    formatted, fileName = formatFileName(fileName)
    if formatted:
        if validateFileExists(fileName):
            task = input(f"What would you like to do with {fileName}? (read/parse/write):")
            if task == "write":
                contents = input("What would you like to write to this file?:")
                print("Successfully wrote:")
                handleFile(fileName, task, contents, True, False)
            else:
                handleFile(fileName, task, None, True, False)
        else:
            print("No worries! I can create a file for you.")
            contents = input("What would you like to put into your new file?")
            print("Creating file for you...")
            handleFile(fileName, "create", contents, False, False)
            print(f"The file {fileName} has been created with the following data:")
            print(readFile(fileName))


if __name__ == "__main__":
    main()
