student = []

for i in range(5):
    name, age = input().split()
    age = int(age)
    student.append((name,age))

student_sorted = sorted(student, key = lambda student: student[1])
print(*student_sorted[0])