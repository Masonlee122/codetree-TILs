a,b = map(int,input().split())

p =1
for i in range(1,b+1):
    if i%a ==0:
        p*=i

print(p)