a,b = map(int,input().split())

max_ = max(a,b)
min_ = min(a,b)

for i in range(max_,min_-1,-1):
    print(i,end=' ')