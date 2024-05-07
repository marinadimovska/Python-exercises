students = []
for _ in range(int(input())):
    name = input()    #marina
    score = float(input())#6
    students.append([name, score])

students.sort(key=lambda x: x[1])
second_lowest_grade = sorted(set([score for name, score in students]))[1]

# Get names of students with the second lowest grade
second_lowest_students = [name for name, score in students if score == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print the names of students with the second lowest grade
for name in second_lowest_students:
    print(name)
