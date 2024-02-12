n = int(input())
cnt = 0
for i in range(2, int(n//2)+1):
    if n%i == 0:
        cnt +=1

if cnt == 0:
    print('P')
else:
    print('C')