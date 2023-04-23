# Sean A
# Working with tkinter

from tkinter import *
from tkinter import ttk as ttk

numFiles = 1000
externalRunAmount = 5
firstRunAmount = 1


def setVariables(numFile, externalRun, firstRun):
    global numFiles
    global externalRunAmount
    global firstRunAmount
    numFiles = numFilesText
    externalRunAmount = firstRunText
    firstRunAmount = firstRun

root = Tk()

root.title("Python Death")

numFilesText = Label(root, text="Number of Files")

firstRunText = Label(root, text="Files Generated on the First Run")

externalRunText = Label(root, text="File Multiplier")

startButton = Button(root, text="Begin", command=run) # padX and padY are the padding on the x and y axis
# I want to
defaultsButton = Button(root, text="Reset to Defaults", command=run

root.mainloop()


def run(textvariable=None):
    print("Running...")
    numFiles = None
    numFilesEntry = ttk.Entry(root, textvariable)
