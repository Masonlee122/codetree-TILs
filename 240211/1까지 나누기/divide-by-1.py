n = int(input())

cnt = 0
i = 1
while n > 1:
    if (n/i) > 1:
        n = int(n//i)
        i+=1
        cnt +=1 
        continue
    if (n/i) <= 1:
        cnt+=1
        break
    
print(cnt)