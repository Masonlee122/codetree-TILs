n = int(input())

k = 0
p =1
for i in range(1,11):
    p *= i
    if p >=n:
        k = i
        break

print(k)