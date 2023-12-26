# 기본 완전 탐색 문제로 for 문을 두 번 사용하여 풀었다
# n < 100 이기에 O(n^2) = 10000 으로 시간 복잡도에서 문제가 없을거라 판단하엿따.


n = int(input())

data = list(map(int,input().split()))
MAX = 1e9

min_distance = MAX

for i in range(len(data)):
    distance = 0
    for j in range(len(data)):
        if i == j :
            continue
        distance += abs(i-j)*data[j]

    if min_distance > distance:
        min_distance = distance


print(min_distance)
