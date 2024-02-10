n = int(input())

s = 0

for _ in range(n):
    k = int(input())

    if k%3 == 0 and k%2 ==1:
        s += k 

print(s)