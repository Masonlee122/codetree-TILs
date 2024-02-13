n = int(input())


for i in range(n,0,-1):
    for k in range(i):
        print('*'*i, end= ' ')
    print()