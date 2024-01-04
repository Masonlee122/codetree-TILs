N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

max = 0

for i in range(N):
    for j in range(N-2):
       cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2]
       if max < cnt :
           max = cnt


print(max)