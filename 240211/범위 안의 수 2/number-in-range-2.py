s = 0
cnt = 0

for i in range(10):
    k = int(input())
    if 0 <= k <= 200:
        s += k
        cnt += 1

print(s,round(s/cnt,1))