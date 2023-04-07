#!/bin/python3

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]] 

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

gradebook[5] = ["visual arts", 98]

gradebook.remove(["poetry", 85])

gradebook.append(["poetry", "Pass"])

lastSemesterGradebook = [["biology", 95], ["Algebra 2", 90], ["history", 92], ["writing", 87], ["art", 99]]

fullGradebook = gradebook + lastSemesterGradebook

print(fullGradebook)
