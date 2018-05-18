# Cody Kovar '19
# McMurry University
# Friday, May 18 2018
# SSPI Program for 2019 Thesis
#
# By creating a subGroup class, one can create any subgroup with a unique name and total number of voters within the
# group. The program creates every existing permutation of all the created groups. The program then calculates the
# pivot voter for each permutation. The program then prints percentage of times out of n! permutations, where n is the
# number of groups, that the given group was the pivot voter.

import math
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os

# Creates a subGroup class with multiple accessors and mutators for the minimum requirements of a group
class subGroup:
    pivotCount = 0.0

    def __init__(self, group_name, count):
        self.group_name = group_name
        self.count = count

    def isPivotVoter(self):
        self.pivotCount += 1

    def getCount(self):
        return self.count

    def getGroupName(self):
        return self.group_name

    def getPivotCount(self):
        return self.pivotCount


def onOutputPress():
    out_file = open("output.txt", "w")
    for line in str.splitlines(text_box.get("1.0", END)):
            out_file.write(line+"\n")
    if os.name == "nt":
        os.system("notepad.exe output.txt")
    # if os.name == "mac":
    #     os.system("open -a TextEdit output.txt")


def onCalculatePress():
    coalitions.clear()

    for line in str.splitlines(text_box.get("1.0", END)):
        if line.find(" -> ") != -1:
            coalitions.append(subGroup(line.split(" -> ")[0], line.split(" -> ")[1]))

    text_box.delete(1.0, END)
    required_votes = 0
    for group in coalitions:
        required_votes += int(group.getCount())

    required_votes //= 2
    required_votes += 1

    generatePermutations(coalitions, 0, len(coalitions) - 1, required_votes)
    i = 0
    for i in range(0, len(coalitions)):
        out_line = coalitions[i].getGroupName() + " Pivotal Vote %:\t\t"
        out_line += str(coalitions[i].pivotCount / math.factorial(len(coalitions)) * 100)
        out_line += "%\n"
        text_box.insert(END, out_line)


# Method for browsing for text file
def onBrowsePress():
    # Sets Read In File
    in_file = open(filedialog.askopenfile(initialdir=os.path.realpath(__file__)).name, "r")

    # Removes Current data from Text Field
    text_box.delete(1.0, END)

    # Prints Read In File contents
    for line in in_file:
        if line.find(" -> ") != -1:
            text_box.insert(END, line)


# Identifies pivot voter and increments the number within the object
def getPivotVoter(plist, required_votes):
    a = 0
    votes = 0
    while votes < required_votes:
        votes += int(plist[a].getCount())
        if votes < required_votes:
            a += 1
    plist[a].isPivotVoter()


# Recursive method that identifies permutations
def generatePermutations(clist, start_index, end_index, rv):
    if start_index == end_index:
        getPivotVoter(clist, rv)
    else:
        for i in range(start_index, end_index + 1):
            clist[start_index], clist[i] = clist[i], clist[start_index]
            generatePermutations(clist, start_index + 1, end_index, rv)
            clist[start_index], clist[i] = clist[i], clist[start_index]


# main
in_file = ""
coalitions = []

# GUI
root = Tk()
root.title("SSPI Calculator")
import_file_button = Button(root, text="Import From txt File", command=lambda: onBrowsePress())
import_file_button.pack()
text_box = Text(root, width=80)
text_box.focus_force()
text_box.pack()
text_box.insert(END, "Example Coalition - Example Vote Count\n")
text_box.insert(END, "Caucasian Democrats -> 5\n")
calculate_file_button = Button(root, text="Calculate SSPI", command=lambda: onCalculatePress())
calculate_file_button.pack(side=LEFT)
output_results_button = Button(root, text="Output to txt", command=lambda: onOutputPress())
output_results_button.pack(side=RIGHT)
mainframe = ttk.Frame(root)
if os.name == 'nt':
    root.lift()
if os.name == 'posix':
    root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()
