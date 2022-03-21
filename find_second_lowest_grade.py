# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.
#
# Example
#
# The ordered list of scores is , so the second lowest score is . There are two students with that score: .
# Ordered alphabetically, the names are printed as:
#
# alpha
# beta
# Input:
# 1. Contains number of students
# 2. The  subsequent lines describe each student over  lines.
#       - The first line contains a student's name.
#       - The second line contains their grade.
num = int(input("Enter the count: "))
list1 = []
for i in range(0, num):
    name = input("Enter the name: ")
    score = float(input(f"Enter the {name} score: "))
    list1.append([name, score])
    list2 = []
    for j in list1:
        list2.append(float(j[1]))


list2.sort()
list3 = []

for i in list2:
    if i not in list3:
        list3.append(i)
lowest = list3[1]
list4 = []
for i in list1:
    if i[1] == lowest:
        list4.append(i)

for i in sorted(list4):
    print(i[0])
