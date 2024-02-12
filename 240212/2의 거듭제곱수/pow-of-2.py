n = int(input())
x = 0
while True:
    k = 2**x
    if k == n:
        break

    x+=1

print(x)