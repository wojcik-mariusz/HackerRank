python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
                   ['Akriti', 41], ['Harsh', 39]]
grades = []

for student in python_students:
    grades.append(student[1])

grades = list(set(grades))
grades.sort()
second_lowest = grades[1]

name = []
for i in python_students:
    if len(name) <= 2 and i[1] == second_lowest:
        name.append((i[0]))

name.sort()
for x in name:
    print(x)
