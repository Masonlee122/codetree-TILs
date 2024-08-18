n = int(input())

student = []
for i in range(n):
    name , h , a = input().split()
    h , a = int(h), int(a)
    student.append((name,h,a))

sorted_std = sorted(student,key=lambda x:x[1])

for i in range(n):
    print(*sorted_std[i])