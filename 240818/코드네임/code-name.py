student = [tuple(input().split()) for _ in range(5)]

student = sorted(student, reverse= True, key = lambda x: student[1])
print(*student[0])