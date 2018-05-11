# Cody Kovar '19
# McMurry University
# Saturday, May 5 2018
# SSPI Program for 2019 Thesis
#
# By creating a subGroup class, one can create any subgroup with a unique name and total number of voters within the
# group. The program creates every existing permutation of all the created groups. The program then calculates the
# pivot voter for each permutation. The program then prints percentage of times out of n! permutations, where n is the
# number of groups, that the given group was the pivot voter.

import math

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


# Identifies pivot voter and increments the number within the object
def getPivotVoter(plist):
    a = 0
    votes = 0
    while votes < required_votes:
        votes += int(plist[a].getCount())
        if votes < required_votes:
            a += 1
    plist[a].isPivotVoter()


# Recursive method that identifies permutations
def generatePermutations(clist, start_index, end_index):
    if start_index == end_index:
        getPivotVoter(clist)
    else:
        for i in range(start_index, end_index + 1):
            clist[start_index], clist[i] = clist[i], clist[start_index]
            generatePermutations(clist, start_index + 1, end_index)
            clist[start_index], clist[i] = clist[i], clist[start_index]


# main
# create file objects
in_file = open("demographics.txt", "r")
out_file = open("output.txt", "w")

# Creates coalitions
coalitions = []

# read in lines from file
for line in in_file:
    coalitions.append(subGroup(line.split("!")[0], line.split("!")[1]))

# Required votes formula
required_votes = 0
for subGroup in coalitions:
    required_votes += int(subGroup.count)

required_votes //= 2
required_votes += 1

generatePermutations(coalitions, 0, len(coalitions) - 1)
i = 0
for i in range(0, len(coalitions)):
    out_line = coalitions[i].getGroupName() + " Pivotal Vote %:\t\t"
    out_line += str(coalitions[i].pivotCount / math.factorial(len(coalitions)) * 100)
    out_line += "%\n"
    out_file.write(out_line)

