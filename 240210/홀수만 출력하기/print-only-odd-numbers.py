n = int(input())

lst = []

for i in range(n):
    k = int(input())
    lst.append(k)

for x in lst:
    if x%3 == 0 and x%2 == 1:
        print(x)