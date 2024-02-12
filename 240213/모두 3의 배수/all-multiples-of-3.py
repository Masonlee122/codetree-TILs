lst = list(map(int,input().split()))

c = 1
for i in lst:
    if i%3 != 0:
        c = 0

print(c)