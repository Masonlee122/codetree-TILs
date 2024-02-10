n = int(input())

s = 0

for _ in range(n):
    k = int(input())

    if k%3 == 0:
        s += k 

print(s)