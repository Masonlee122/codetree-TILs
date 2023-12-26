#완전 탐색 문제 3
#탐색 범위를 정할 때 끝함수를 주의함

n = int(input())
data = list(map(int,input().split()))


cnt = 0
for i in range(len(data)-2):
    for j in range(i+1,len(data)-1):
        for k in range(j+1,len(data)):
            if data[i] <= data[j] and data[j] <= data[k]:
                cnt+=1

print(cnt)
