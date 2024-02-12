a,b,c = map(int,input().split())

k = False
i = 1
while c <=b:
    c = c*i
    if  a<= c <= b:
        k = True
    
    
    i+=1

if k == True:
    print('YES')
else:
    print('NO')