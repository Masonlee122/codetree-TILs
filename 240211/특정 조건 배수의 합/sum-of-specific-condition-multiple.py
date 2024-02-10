a,b = map(int, input().split())


max_ = max(a,b)
min_ = min(a,b)
s = 0

for i in range(min_,max_+1):
    if i%5==0:
        s+=i

print(s)