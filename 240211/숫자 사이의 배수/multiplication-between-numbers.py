a,b = map(int,input().split())

s = 0
cnt = 0
for i in range(a,b+1):
    if i%5 ==0 or i%7 == 0:
        s += i
        cnt +=1

avg = float(s/cnt)

print(f'{s}{avg : .1f}')