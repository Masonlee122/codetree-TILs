a,b ,c = map(int,input().split())

k = False
i = 1
while c <= b:
    c =c*i
    if a <= c <=b :
        k = True
        break
    i+=1

if k == False:
    print('YES')
else:
    print('NO')