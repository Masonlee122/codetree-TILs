a = input()

cnt = 0

for i in range(len(a)):
    if a[i] == '(' and i != len(a):
        for j in a[i+1:]:
            if j == ')':
                cnt += 1

print(cnt)