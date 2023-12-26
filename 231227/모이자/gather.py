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